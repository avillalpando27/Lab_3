#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: Main.py
Name: Angel Villalpando
Date: 11/03/2018
Course: CS 2302 - Data Structures
Description: Program checks the number of anagrams for a user-specified word in a user provided file and also checks
the file for the word with the the greatest number of anagrams.
"""

from RedBlackTree import RedBlackTree, RBTNode
from AVLTree import AVLTree, Node

anagramCount = 0 # global variable for anagram count to make counting easier in recursive methods

def rb_loader(file): # this method loads the user provided file into a RB Tree
    rb_Tree = RedBlackTree()

    for line in file:
        word = line.strip('\n').lower()
        rb_Tree.insert(word)
    file.close()

    return rb_Tree


def avl_loader(file): # this method simply loads the user provided file into an AVL Tree
    avl_Tree = AVLTree()

    for line in file:
        word = line.strip('\n').lower()
        avl_Tree.insert(Node(word))
    file.close()

    return avl_Tree


def print_Tree(root): # while not used in this particular lab, this method prints tree in post order
    if root == None:
        return None
    print(root.key)
    print_Tree(root.left)
    print_Tree(root.right)


def count_anagrams(word, word_list, prefix=""): # this is the modified method that now counts number of anagrams
    global anagramCount
    if len(word) <= 1:
        str = prefix + word

        if word_list.search(str):
            anagramCount += 1
    else:
        for i in range(len(word)):
            curr = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if curr not in before:
                count_anagrams(before + after, word_list, prefix + curr)

    return anagramCount  # while a global variable need not be returned it is done for assignment purposes


def max_anagram(file, word_list): # method determines the words with the most anagrams given a user file
    global anagramCount

    usrFile = open(file, "r") #re-opens file to scan every element in the file and compare against data structure
    maxCount = 0
    count = 0
    maxWord = ""

    for line in usrFile:
        word = line.strip('\n').lower()
        count = count_anagrams(word, word_list) # each iteration of the file read gives count a new value
        if count > maxCount:
            maxCount = count
            maxWord = word
        anagramCount = 0 # global variable updated, in order to provide new count value in count_anagrams method return
        count = 0
    usrFile.close()

    print("Word with the most anagrams is: ",maxWord, "\nThe number of anagrams it has is: ", maxCount)


def main():

    global anagramCount

    userFile = input("\n\nPlease provide the file name for anagram analysis: ") ## user file request prompt
    file = open(userFile, "r")

    usrChoice = input("\nPlease choose a Data Structure:\n1. AVL Tree\n2. Red-Black Tree\n") ## data structure prompt

    if int(usrChoice) == 1:
        english_words = avl_loader(file)
        usrAnagram = input("\nWhat word would you like to permute and check against the AVL Tree? ")
        print("The word '",usrAnagram,"' has a total of ", count_anagrams(usrAnagram, english_words), " anagrams.")
        anagramCount = 0
    elif int(usrChoice) == 2:
        english_words = rb_loader(file)
        usrAnagram = input("\nWhat word would you like to permute and check against the Red-Black Tree? ")
        print("The word '",usrAnagram,"' has a total of ", count_anagrams(usrAnagram, english_words), " anagrams.")
        anagramCount = 0
    else:
        print("Invalid Selection. Good Bye.")

    usrChoice2 = input("\nWould you like to analyze the given file for the word with most anagrams? (Enter Y or N): ")

    if usrChoice2 == "Y" or usrChoice2 == "y":
        max_anagram(userFile, english_words)
    else:
        print("Goodbye! ")


main()