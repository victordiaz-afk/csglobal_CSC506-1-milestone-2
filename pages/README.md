# CSC506 — Assignment 4 (pages)

This folder contains small demo scripts used for Assignment 4: a threaded producer/consumer demo and simple data-structure functionality tests.

Files of interest
- algorithms.py — Producer/consumer demo + TextEditor class that uses Deque and Stack for undo/redo-like behavior. Demonstrates threading, a shared Queue, and a STOP sentinel for clean shutdown.
- funtionality_test.py — Quick smoke tests for the project's data structures (Stack, Deque, LinkedList, Queue). Uses randomized inserts/removes and prints results for manual inspection.

Prerequisites
- Python 3.7+
- Project must include the data_types implementations referenced by the scripts:
  - data_types/queue.py
  - data_types/dequeue.py
  - data_types/stack.py
  - data_types/linked_list.py

Quick usage
1. From the repository root (or this folder), run:
   python algorithms.py
   - This runs a demo that spawns a producer and consumer thread, fills a shared queue with story lines (placeholders replaced by random words), and demonstrates delete/undo flows via a TextEditor instance.
2. To run the unit-like smoke tests:
   python funtionality_test.py
   - Prints push/pop/enqueue/dequeue/display operations and results.

What each script demonstrates
- algorithms.py
  - TextEditor: uses a Deque (for ordered paragraphs) and a Stack (undo history).
  - producer(): splits a multiline story, fills `{}` placeholders with random words, and enqueues each line with a small delay to simulate streaming input.
  - consumer(): dequeues items in a loop, appends them to TextEditor, and exits on seeing a unique STOP sentinel.
  - Thread-safe access to a shared queue is gated by a Lock.
- funtionality_test.py
  - Exercises data-structure methods (push, pop, addFront/addRear, removeFront/removeRear, insert/delete/search for linked list) and prints state for manual verification.

Notes & known issues
- algorithms.py expects a Queue implementation with enqueue() and dequeue(); Deque implementation should provide addFront/addRear/removeFront/removeRear/display.
- funtionality_test.py uses random values; test outputs vary by run.
- The demo uses a unique STOP sentinel object (not a string) to avoid collision with real payloads.
- Both scripts print to stdout for manual inspection; consider adapting them to return structured results for automated testing.

Suggested improvements
- Add unit tests (pytest) for each data structure.
- Make analyze/demo output return structured data (dicts) rather than printing — easier to assert in tests.
- Add optional CLI flags (argparse) to control test sizes and delays.

Author / Purpose
Academic demo for CSC506 — Assignment 4.
