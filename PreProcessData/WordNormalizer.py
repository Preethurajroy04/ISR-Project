import Classes.Path as Path
# import nltk
# nltk.download('all')
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class WordNormalizer:

    def __init__(self, content):

        stemmer = PorterStemmer()                        # initializing stemmer object

        self.doc_content = word_tokenize(content)        # tokenize content into tokens
        # print(self.doc_content)
        return


    def lowercase(self, word):
        # Return the next word in the document.
        # Return null, if it is the end of the document. 

        try:                           
            # pop first word of list and remove char except alphabets
                                     
            self.word = self.doc_content.pop(0)   
            print(self.word) 

            # Transform the word uppercase characters into lowercase.                    
            self.word = self.word.lower() 
            self.word = self.word.strip()

            print(self.word)

        except:
            # if no more elements/ words left in list to pop, return null
            return None

        return self.word


    def stopword(self, word):
        # Return the stemmed word with PorterStemmer imported previously.


        word = stemmer.stem(word) 

        return word


    def tokenize(self, word):
        # Return the stemmed word with PorterStemmer imported previously.

        

        word = stemmer.stem(word) 

        return word


    def stem(self, word):
        # Return the stemmed word with PorterStemmer imported previously.

        stemmer = PorterStemmer()   # initializing stemmer object

        word = stemmer.stem(word) 

        return word