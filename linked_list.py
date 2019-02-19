# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:15:40 2019

@author: harshal
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data),end='')

        node = node.next

        if node:
            print(sep,end='')

# Complete the insertNodeAtPosition function below.
def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if not position:
        node.next = head
        head = node
        return head
    else:
        temp = head
        for _ in range(position-1):
            head = head.next
        node.next = head.next
        head.next = node
        return temp
    
#def insertNodeAtPosition(head, data, position):
#    node = SinglyLinkedListNode(data)
#    if not position:
#        node.next = head
#        head = node
#        return head
#    else:
#        temp = head
#        for _ in range(position):
#            temp = temp.next
#        node.next = temp
#        temp = node
#        return head





if __name__ == '__main__':
    
    llist_count = 3
    NN = [16,13,7]

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = NN[i]
        llist.insert_node(llist_item)

    data = 1

    position = 1

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')
    
