#------------------------------------------------------------------------------
# APA - Assignment 2
#
# This program opens a given input document, extract the chromosome, arm and
# position of each sequence and saves it in a linked list. Then, the linked
# list is sorted using an insertion sort algorithm. Lastly, the program computes
# the number of sequence pairs that are more close (euclidean distance) than a
# given threshold in each chromosome and arm and writes it in an output document.
#
# Due date: 11/10/2019                                     Joan Térmens Cascalló
#------------------------------------------------------------------------------

import numpy as np
from sys import argv
import re

#------------------- Create the Node & LinkedList classes ----------------------

class Node:

    def __init__(self,chr,arm,x,y): #Node initialization
        self.chr = chr #Chromosome
        self.arm = arm #Chromosomal arm
        self.x = x #x coordinate (position)
        self.y = y #y coordinate (position)
        self.next = None

    def __gt__(self,other): #Custom compairsons for chromosome and arm
        if (self.chr > other.chr) or ((self.chr == other.chr) and (self.arm > other.arm)):
            return True
        else:
            return False

    def __eq__(self,other):
        if (self.chr == other.chr) and (self.arm == other.arm) :
            return True
        else:
            return False

    @staticmethod #The euclidean distance is implemented as an static method
    def eucl_dist(x1,x2,y1,y2):
        '''This function returns the euclidean distance between a pair of
        2-dim points.'''
        return np.sqrt((x1-x2)**2+(y1-y2)**2)


class LinkedList:
    def __init__(self): #(single)Linked list class
        self.root = None #list's root

    def add_node(self,chr,arm,x,y):
        '''This method adds a node to the end of a linked list.'''
        new_node = Node(chr,arm,x,y)
        if self.root is None:
            self.root = new_node
            return
        else:
            new_node.next = self.root
            self.root = new_node
            return

    def display(self):
        '''This method displays a linked list. Usefull for testing the sorting.'''
        curr = self.root
        if self.root is None:
            print("Empty list")
            return
        while curr is not None:
            print("{}{} ({},{})".format(curr.chr,curr.arm,curr.x,curr.y))
            curr = curr.next
        return

    def insertion_sort(self):
        "This method implements the insertion sort algorithm on a linked list."
        root = self.root
        key = root
        while key.next is not None:
            if key.next > key: #If the element is sorted it passes to the next
                key = key.next
            else:
                temp = key.next
                key.next = temp.next
                if root > temp: #Inserts the key element at the begginig of
                    temp.next = root  #the list
                    self.root = temp
                    root = self.root
                else:
                    curr = root #Searches for the appropiate's key site
                    while temp > curr.next:
                        curr = curr.next
                    temp.next = curr.next
                    curr.next = temp

    def sort_count(self,file_name,threshold):
        '''This method sorts a given linked list using insertion sort and
        then counts the number of sequence pairs that are more close (euclidean
        distance) than a given threshold in each chromosome and arm and writes
        it in an output document.'''

        self.insertion_sort() #Insertion sort

        i =  self.root #different indexes to recurre the list
        j = i
        k = j.next
        count = 0

        with open(file_name +".txt", "w") as OutputFile:
            OutputFile.write("Location\tNumber\n")

            while i is not None: #Loop for each location
                while (i is not None) and (j is not None) and(i == j): #1st pair element
                    while (j is not None) and (k is not None) and (j == k): #2nd pair element
                        if Node.eucl_dist(j.x,k.x,j.y,k.y) <= threshold:
                            count += 1
                            k = k.next
                    j = j.next
                    if j is not None: #avoids "NoneClass" atribute errors
                        k = j.next
                OutputFile.write("{}{}\t{}\n".format(i.chr,i.arm,count))
                i = j
                count = 0

        OutputFile.close()


#------------------------------------------------------------------------------

script, file_path, k = argv #command prompt arguments

k = float(k)

output_name = "results1"

seq_list = LinkedList()

with open(file_path, "r") as InputFile: #opens the input doc
    for line in InputFile.readlines():
        seq,loci,posi = line.split()

        x,y = posi.split(",") #x and y coordinates extraction
        tmp,x = x.split("(")
        y,tmp = y.split(")")
        x = float(x)
        y = float(y)

        chr = ""
        for e in loci:     #Chromosome and arm extraction
            if e.isdigit():
                chr += e
            if e.isalpha():
                arm = e
                chr = int(chr)
                break
                
        seq_list.add_node(chr,arm,x,y)

InputFile.close()

seq_list.sort_count(output_name,k) #main algorithm
