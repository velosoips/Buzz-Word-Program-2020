#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:34:57 2022

@author: ingridveloso
"""
#BUZZ WORD PROGRAM: Comparing Trending Words from Tweets in 2018 and 2020
import string #to call in string functions
def tweetprocess(tweet, wordcounter): #function to edit each line of csv tweet files for analysis/sorting
    tweet = tweet.strip() #to remove spaces at beginning and end of tweets
    wordlisting = tweet.split() #to split tweet words by spaces
    for word in wordlisting:
        word = word.lower() #convert words to lowercase
        word = word.strip(string.punctuation) #remove punctuation in words
        word = word.strip(string.digits) #remove numbers from words
        wordadd(word, wordcounter)

def wordadd(word, wordcounter): #function to call word and the number of times it has appeared
    key = frozenset(wordcounter.items())
    if key in wordcounter:
        wordcounter[word] += 1 #to count words that are already in wordcounter list
    else:
        wordcounter[word] = 1 #to add new words that are not in list yet
            
def listprint(wordcounter): #function to format word count list
    valuesandkeys = [] #new list for value (number of times a word appears) and key (the word)
    for key,val in wordcounter.items(): #taking items from wordcounter
        valuesandkeys.append((val,key))
    valuesandkeys.sort(reverse = True) #order is from largest to smallest
    print('{:10s}{:10s}'.format('Word', 'Count')) #formatting output
    print('_'*18)
    for val,key in valuesandkeys:
        print('{:11s} {:<3d}'.format(key,val))
        
from collections import Counter
def top5(wordcounter):
    valuesandkeys = []
    for key,val in valuesandkeys:
        topoccurances = Counter.most_common(5)
        print(topoccurances)
     
import json #start reading json files of Oct 1, 2020 tweets
data = []
wordcounter = {}
with open('oct12020.json') as f:
    for jsonObj in f:
        lines = json.loads(jsonObj)
        data.append(lines)
for tweet in data:
    x = tweet["text"]
    if type(x) != "<class 'str'>": #to get rid of tweets with field "text" that are not strings
        continue
    else:
        print(tweet["text"]) #string "text"s get printed and processed
        tweetprocess(tweet, wordcounter)        
wordadd(tweet, wordcounter) #adding words
top5(listprint(wordcounter)) #printing top 5 most used words from data

import json #start reading json files of Oct 2, 2020 tweets
data = []
wordcounter = {}
with open('oct22020.json') as f:
    for jsonObj in f:
        lines = json.loads(jsonObj)
        data.append(lines)
for tweet in data:
    x = tweet["text"]
    if type(x) != "<class 'str'>": #to get rid of tweets with field "text" that are not strings
        continue
    else:
        print(tweet["text"]) #string "text"s get printed and processed
        tweetprocess(tweet, wordcounter)        
wordadd(tweet, wordcounter) #adding words
top5(listprint(wordcounter)) #printing top 5 most used words from data