import nltk 
import PyPDF2
import os
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
import string


def create_index (data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            index[token].append(i)
    return index

# List all files in a directory using scandir()
basepath = 'data/'

file_names =[]
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            file_names.append(entry.name)


ps = PorterStemmer()
punc = string.punctuation
stop_words = set(stopwords.words('english'))


print(file_names)
inverted_index = {}
for file in file_names:
    print(file,end="")
    pdfFileObj = open(os.path.join(basepath,file), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    num = pdfReader.numPages
    pageText = []
    for i in range(num):
        if(i%50==0):
            print("=",end="")
        pageObj = pdfReader.getPage(i)
        a = word_tokenize(pageObj.extractText())
        pageText += a
    # print(pageText[0])

    for word in pageText:
        if word not in stop_words and word not in punc:
            word = ps.stem(word)
            if word in inverted_index:
                posting_list = inverted_index[word]
                if file in posting_list:
                    posting_list[file] = posting_list[file] + 1
                else:
                    posting_list[file] = 1
            else:
                inverted_index[word] = {file:1}
    print("Complete")
    
    pdfFileObj.close()


count = 0
for i in inverted_index:
    if(count>10):
        break
    else:
        print(i)
        for j in range(20):
            print("-",end="")
        print()
        print(inverted_index[i])
        print("\n\n")
        
        count+=1    