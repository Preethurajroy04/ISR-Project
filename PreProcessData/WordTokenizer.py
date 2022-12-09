import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.

class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.

        self.doc_content = content.split(" ")                          # split content into list of words on whitespaces

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document. 

        try:                           
            # pop first word of list and remove char except alphabets
                                     
            self.word = self.doc_content.pop(0)                        
            self.word = re.sub('[.*-.*]', ' ', self.word) 
            self.word = re.sub('[^a-zA-Z]+', '', self.word) 

            self.word = self.word.strip()
            # print(self.doc_content)

        except:
            # if no more elements/ words left in list to pop, return null
            return None

        return self.word
