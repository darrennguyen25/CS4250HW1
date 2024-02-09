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
print("Documents after stopword removal:", documents)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "loves": "love",
    "cats": "cat",
    "dogs": "dog"
}
for i in range(len(documents)):
    documents[i] = ' '.join([documents[i].replace(w, stemming[w]) for w in stemming if w in documents[i].split()])
# for k in stemming:
#     for i in range(len(documents)):
#         if k in documents[i]:
#             documents[i] = documents[i].replace(k, stemming[k])
print("Documents after stemming removal", documents)

#Identifying the index terms.
#--> add your Python code here
terms = list(set([w for sentences in documents for w in sentences.split()]))
terms.sort(reverse=True)
print("Index terms:", terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

#Calculating the term frequency (tf) for each document-term pair.
def findtf(t, d):
    tf = {}
    for w in t:
        tf[w] = d.count(w)
    return tf

doc1tf = findtf(terms, documents[0])
doc2tf = findtf(terms, documents[1])
doc3tf = findtf(terms, documents[2])
print(doc1tf)
print(doc2tf)
print(doc3tf)


#Printing the document-term matrix.
#--> add your Python code here