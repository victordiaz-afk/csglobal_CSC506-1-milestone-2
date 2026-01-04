
import threading
import time
import random
import re

from data_types.queue import Queue
from data_types.dequeue import Deque
from data_types.stack import Stack


# -------------------------
# TextEditor (robust deletes/undo)
# -------------------------
class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.text_queue = Deque()

    def add_paragraph(self, text: str):
        # Deque API: prefer addRear if present; else enqueue
        if hasattr(self.text_queue, "addRear"):
            self.text_queue.addRear(text)
        else:
            self.text_queue.enqueue(text)
        print(f"[Add] Enqueued paragraph: {text}")

    def compile_paragraph(self):
        # Just displays in this simple demo
        if hasattr(self.text_queue, "display"):
            self.text_queue.display()
        else:
            print("[Compile] (No display method on Deque)")

    def delete(self):
        # Safely remove last item from Deque and push to Stack
        try:
            if hasattr(self.text_queue, "removeRear"):
                text = self.text_queue.removeRear()
            else:
                text = self.text_queue.dequeue()
        except IndexError:
            print("[Delete] Queue/Deque is empty; nothing to delete.")
            return

        self.undo_stack.push(text)
        print(f"[Delete] Removed from queue and pushed to undo: {text}")

    def undo_check(self):
        top = self.undo_stack.peek()
        if top is None:
            print("[Undo Check] Undo stack is empty.")
        else:
            print(f"[Undo Check] Next undo item: {top}")

    def undo(self):
        text = self.undo_stack.pop()
        if text is None:
            print("[Undo] Nothing to undo.")
            return
        try:
            if hasattr(self.text_queue, "addRear"):
                self.text_queue.addRear(text)
            else:
                self.text_queue.enqueue(text)
            print(f"[Undo] Restored paragraph back to queue: {text}")
        except Exception as e:
            print(f"[Undo] Failed to restore: {e}")


# -------------------------
# Shared queue + thread sync
# -------------------------
shared_queue = Queue()
lock = threading.Lock()

# Use a unique object sentinel: avoids collision with real data
STOP = object()

# -------------------------
# Words to fill the story
# -------------------------
random_words = [
    "crate", "dock", "pallet", "warehouse", "stack",
    "forklift", "loading", "cargo", "lift", "shift",
    "barcode", "shipping", "route", "crew", "ramp",
    "trolley", "inventory", "package", "schedule", "dispatch",
]


# -------------------------
# Helper: fill ALL '{}' with random words
# -------------------------
def fill_placeholders(line: str, words: list[str]) -> str:
    """
    Replace each '{}' placeholder in a line with a random word.
    If no '{}' are present, returns the line unchanged.
    """
    # Count how many '{}' placeholders are present
    count = len(re.findall(r"\{\}", line))
    if count == 0:
        return line
    # Pick 'count' random words and format
    chosen = [random.choice(words) for _ in range(count)]
    # Use .format(*chosen) after converting '{}' to '{0}', '{1}', ...
    # A simple way: replace '{}' with '{}' and format with positional args works:
    return line.format(*chosen)


# -------------------------
# Producer: split story and enqueue lines
# -------------------------
def producer(name: str, story_text: str, words: list[str], delay: float = 0.05):
    """
    Split a plain story into lines, fill placeholders, and enqueue each line.
    """
    lines = [l.strip() for l in story_text.splitlines() if l.strip()]
    for raw_line in lines:
        line = fill_placeholders(raw_line, words)
        time.sleep(delay)  # simulate staggered arrivals
        with lock:
            shared_queue.enqueue(line)
        print(f"[{name}] queued: {line}")


# -------------------------
# Consumer: dequeue safely and add to TextEditor
# -------------------------
def consumer(book: TextEditor, delay: float = 0.02):
    """
    Continuously dequeue items (catch IndexError when empty) and add to TextEditor.
    Stops when STOP sentinel is seen.
    """
    while True:
        with lock:
            try:
                item = shared_queue.dequeue()
            except IndexError:
                item = None  # nothing in the queue right now

        if item is None:
            time.sleep(0.02)
            continue

        if item is STOP:
            print("[Consumer] Stop received. Exiting.")
            break

        time.sleep(delay)
        book.add_paragraph(item)


# -------------------------
# DEMO / MAIN
# -------------------------
if __name__ == "__main__":
    # Create the book (uses Deque + Stack inside)
    book = TextEditor()

    # A simple, plain story (multiple lines with '{}' placeholders to be filled)
    STORY = """
Today was a {} day at the warehouse.
We moved {} and organized the dock.
The {} split up tasks to speed things up.
By the afternoon, the pallets were {}.
We loaded the truck and checked the {}.
Everything was ready before {} time.
The {} wrapped up and reviewed tomorrow’s plan.
"""

    # Start consumer
    c = threading.Thread(target=consumer, args=(book,), daemon=True)
    c.start()

    # Start producer — IMPORTANT: pass random_words
    p = threading.Thread(target=producer, args=("Producer-1", STORY, random_words), daemon=True)
    p.start()

    # Wait for producer to finish
    p.join()

    # Send stop sentinel so consumer exits cleanly
    with lock:
        shared_queue.enqueue(STOP)

    # Give the consumer a moment to flush and exit
    time.sleep(0.2)
    c.join(timeout=1)

    print("\n================ CURRENT BOOK (Deque) ================")
    book.compile_paragraph()

    # Demonstrate delete -> goes to Stack (undo history)
    print("\n================ DELETE (to Stack) ====================")
    book.delete()
    book.undo_check()
    print("\n[Book after delete]")
    book.compile_paragraph()

    # Demonstrate undo -> pops from Stack back to Deque
    print("\n==================== UNDO =============================")
    book.undo()
    print("\n[Book after undo]")
    book.compile_paragraph()
