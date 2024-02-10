#-------------------------------------------------------------------------
# AUTHOR: Darren Nguyen
# FILENAME: indexing.py
# SPECIFICATION: Output tf-idf document-term matrix from a collection of documents
# FOR: CS 4250- Assignment #1
# TIME SPENT: 5 hours
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

terms = []
[terms.append(w) for d in documents for w in d.split(' ') if w not in terms]
print("index terms:", terms)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

def findtf(t, d):
    return d.split(' ').count(t)/len(d.split(' '))

def findidf(t, D):
    df = sum([1 for d in D if t in d])
    return math.log10(len(D)/df)

def findtfidf(t, d, D):
    return round((findtf(t, d) * findidf(t, D)), 3)

docTermMatrix = [[findtfidf(t, d, documents) for t in terms] for d in documents]

#Printing the document-term matrix.
#--> add your Python code here
print("Document-Term Matrix:")
print("\tlove\tcat\tdog")
for i, d in enumerate(docTermMatrix):
    print(f"Doc{i+1}:", end="\t")
    for j, t in enumerate(d):
        print(f"{t:.3f}", end="\t")
    print()