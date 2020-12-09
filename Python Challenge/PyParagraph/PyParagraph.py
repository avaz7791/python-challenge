""" 
Dev: Amir Vazquez
Date: 12/08/2020
Project: PyParagraph
Description: Import a text file filled with a paragraph of your choosing.
    - Assess the passage for each of the following:
    - Approximate word count
    - Approximate sentence count
    - Approximate letter count (per word)
    - Average sentence length (in words)
"""

#add libraries
import os, csv
import re
import string

from collections import Counter

cwd = os.getcwd()
FileName= 'Python Challenge\PyParagraph\Resources\paragraph_2.txt'
txt_file =os.path.join(cwd, FileName)

def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(txt_file, "r") as txtfile:
        return txtfile.read().lower()


#Grab the text for a paragraph file
word_list = load_file(txt_file)

Just_Words = word_list.split(" ")       # collect only words separated by space
word_cnt = len(Just_Words)              # Count words
sentences  = re.split("\. ", word_list) # A sentence ends with a period
sentence_cnt = len(sentences)           # Count sentences

letters=0   #used to count letters in words
for i in range(word_cnt):           
    letters +=  len(Just_Words[i])      # counting the letters in each word

avg_letters = letters / word_cnt        # average of letters in the paragraph

#print(f'Total Votes: {len(tot_votes)}') 
print(f'Paragraph Analysis')
print(f'--------------------------------------------')
print (f'Approximate Word Count: {word_cnt}')
print (f'Approximate Sentence Count: ', sentence_cnt)
print (f'Average Letter Count: {avg_letters:.1f}')
print (f'Average Sentance Length : {word_cnt/sentence_cnt} ')

#print (letters)
