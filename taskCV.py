#!/usr/bin/python2.7 -tt

#In this section import the libraries in done
import urllib2
import os,sys
import nltk
import bs4
from bs4 import BeautifulSoup
from nltk import word_tokenize, pos_tag

#Storing the link in a variable
hackernews="https://news.ycombinator.com/"
page=urllib2.urlopen(hackernews)
soup=BeautifulSoup(page, "html.parser")
page_content=soup.prettify()
#Storing the file in a variable
sent = open("filename.txt").read()
#Tokenizing the words stored in the file
words=nltk.word_tokenize(sent)
#Tagging the words of the files based on the parts of speech
tags=nltk.pos_tag(words)
#Taking input from the user
word_key=raw_input("Enter the any keyword to be searched : ")
#Searching the nouns(keywords) from the file
nouns=[word for word,pos in tags \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
#Checking wether the keyword entered by the user is present in the file
with open("filename.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if word_key in part:
				all_links=soup.find_all("a")
				for link in all_links:
   					 print link.get("href")
#Creating a new file and storing in a variable 
output=open("output.txt","w")	
print >>output, nouns
output.close()