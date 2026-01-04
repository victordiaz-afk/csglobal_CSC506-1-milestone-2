import random 
import time 
import sys


class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)

        if self.head is None: 
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
           
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        

    
    def delete(self): 
        print('delete')
        if self.head is not None :
             self.length =- 1 
             self.head = self.head.next  
        else: 
             raise IndexError(" linked list is empty ") 
        
    def search(self, target):
       curr = self.head
       while curr is not None:
           if curr.data == target:
               return True
           curr = curr.next
        
       return False   


    def display(self):
        print('display')
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
          
        

    def Analyze(self):
        print("=== Stack Operation Analysis ===\n")
        
        # Theoretical Complexity
        print("Theoretical Time & Space Complexity:")
        print("• Push (add):     O(1) time, O(1) space")
        print("• Pop (delete):   O(1) time, O(1) space")
        print("• Search:         O(n) time, O(1) space")
        print("• Overall for n=100 operations: O(n) time, O(n) space\n")

        # Reset stack
        self.__init__()
        start_time = time.perf_counter()

        #insertion
        for e in range(1000):
            self.insert(random.randint(1,1000))
        add_time_ = time.perf_counter() - start_time 

        

        #serach
        target  = random.randint(1,1000)

        start_time = time.perf_counter()
        answer =  self.search(target)
        search_time_ = time.perf_counter() - start_time 

        
        start_time = time.perf_counter()
        self.delete()
        def_time_ = time.perf_counter() - start_time 

        single_node_size = sys.getsizeof(Node(0)) + sys.getsizeof(0) + sys.getsizeof(None)
        estimated_total = single_node_size * self.length

        
        return add_time_, answer, search_time_, def_time_ ,estimated_total 


        

        
        