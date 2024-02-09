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
print("stopword removal:", documents)

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "loves": "love",
    "cats": "cat",
    "dogs": "dog"
}
for i in range(len(documents)):
    documents[i] = ' '.join([documents[i].replace(w, stemming[w]) for w in stemming if w in documents[i].split()])
print("stemming removal", documents)

#Identifying the index terms.
#--> add your Python code here
terms = list({w for d in documents for w in d.split()})
print("index terms:", terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

tf = [{w: d.split().count(w) for w in set(d.split())} for d in documents]
print("tf for documents:", tf)

idf = []
for w in terms:
    df = sum([1 for d in documents if w in d.split()])
    idf += [math.log10(len(documents)/df)]
print("idf for terms:", idf)

#Printing the document-term matrix.
#--> add your Python code here