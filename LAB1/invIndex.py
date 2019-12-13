import nltk 
nltk.download('gutenberg')
nltk.download('stopwords')
from nltk.corpus import gutenberg
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

ps = PorterStemmer()
file_names = gutenberg.fileids()
# print(file_names)

stop_words = set(stopwords.words('english'))
# print(stop_words)

indexer = 0
filename_map = {}
for book_name in file_names:
    filename_map[book_name] = indexer
    indexer = indexer+1

punc = string.punctuation

inverted_index = {}

for book_name in file_names:
    for word in gutenberg.words(book_name):
        if word not in stop_words and word not in punc:
            word = ps.stem(word)
            if word in inverted_index:
                posting_list = inverted_index[word]
                if book_name in posting_list:
                    posting_list[book_name] = posting_list[book_name] + 1
                else:
                    posting_list[book_name] = 1
            else:
                inverted_index[word] = {book_name:1}

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
        print()
        count+=1                