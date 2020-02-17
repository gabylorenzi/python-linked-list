#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: gabylorenzi
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        #8 to print instances of node
        return str(self.data)
    
    def __repr__(self):
        #use this in linked list repr
        return repr(self.data)
        
class LinkedList:
    def __init__(self, pythonList = None):
        #new_node = Node(data)
        if pythonList == None:
            self.first = None
            self.last = None
            self.len = 0
        else:
            self.first = Node(pythonList[0]) #first eelment in list
            self.last = Node(pythonList[-1]) #last elem in list 
            #print(self.last)
            current = self.first 
            for i in pythonList[1:]:
                if(i == pythonList[-1]): #if its the last one treat diff than others
                    current.next = self.last
                    self.last.next = None
                else:
                    current.next = Node(i) #make node with new value 
                    current = current.next
            #self.last = None
            self.len = len(pythonList)

    # 3
    def append(self, data):
        #print("hey")
        if self.first == None: #if the list is empty 
            new = Node(data)
            self.first = new
            self.last = new
        else: #if the list has elements 
            current = Node(data)
            self.last.next = current
            self.last = current
        self.len +=1 


    # 4
    def prepend(self, data):
        if self.first == None:
            self.append(data)
        self.len+=1
        insert = Node(data)
        insert.next = self.first
        self.first = insert


    # 6
    def __len__(self):
        return self.len 

    # 7
    def __eq__(self, other):
        #print(other)
        curr_one = self.first
        curr_two = other.first
        while curr_one and curr_two:
            if curr_one.data != curr_two.data:
                return False
            curr_one = curr_one.next
            curr_two = curr_two.next

        return (curr_one == None and curr_two == None)

    # 9
    def __str__(self):
        node_list = []
        current = self.first
        while current != None:
            node_list.append(repr(current))
            current = current.next
        s = " -> "
        s = "["+ s.join(node_list) + " -> ]" #build string
        return s

    # 10
    def __repr__(self):
        s = '' #build string on s 
        count = 0
        current = self.first
        while count < self.len:
            s += repr(current.data) #add nodes data
            current = current.next #move along 
            count += 1
            if count != self.len:
                s += ', '
            if current == None:
                break
        s = 'LinkedList([' + s + '])'
        return str(s)
#        node_list = []
#        s = ''
#        current = self.first
#        while current != None:
#            node_list.append(repr(current.data))
#            #print("bleh")
#            current = current.next
#        s = ', '
#        return repr('LinkedList(['+ s.join(node_list) + '])')

    # 11
    def insert(self, data, idx):
        if idx < 0:
            return None
        if idx == 0:
            self.prepend(data)
            return
        if idx == len(self):
            self.append(data)
        else:
            insert = Node(data)
            self.len +=1
            current = self.first
            index = idx
            while current.next and index >1:
                current = current.next
                index -= 1
            insert.next = current.next
            current.next = insert
