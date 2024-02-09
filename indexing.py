#-------------------------------------------------------------------------
# AUTHOR: Darren Nguyen
# FILENAME: indexing.py
# SPECIFICATION: Output tf-idf document-term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'her', 'They', 'their'}
for i in range(len(documents)):
    documents[i] = ' '.join([w for w in documents[i].split() if w not in stopWords])
print(documents)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "loves": "love",
    "cats": "cat",
    "dogs": "dog"
}
for i in range(len(documents)):
    documents[i] = ' '.join([documents[i].replace(k, stemming[k]) if k in stemming else k for k in documents[i].split()])
# for k in stemming:
#     for i in range(len(documents)):
#         if k in documents[i]:
#             documents[i] = documents[i].replace(k, stemming[k])

#Identifying the index terms.
#--> add your Python code here
terms = list(set([w for sentences in documents for w in sentences.split()]))
print(terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
def findTF(terms, documents):
    return [[]]

#Printing the document-term matrix.
#--> add your Python code here