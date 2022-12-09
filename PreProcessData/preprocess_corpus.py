import Classes.Path as Path
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.

class PreProcessCorpus:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

        self.text_file = open(Path.DataTextDir, "r", encoding="utf8") # opening the file in read mode

        

        return 

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        
        casts = ""
        content = ""

        # declaring docNo and content variables

        self.docNo = ""       # initializing var docNo
        self.title = ""       # initializing var title
        self.genre = ""       # initializing var genre
        self.language = ""    # initializing var language
        self.country = ""     # initializing var country
        self.cast = ""        # initializing var cast
        self.keywords = "" 

        count = 0
        for line in self.text_file:

            # if "</doc>" in line: 
            #     # breaks loop if </DOC> tag not found, meaning no more documents left
            #     break        

            if "<docid>" in line: 
                # fetching docNo from line containing "<DOCNO>"
                
                self.docNo = line.split("<docid>")[1].split("</docid>")[0]  
                # print(self.docNo)  

            if "<title>" in line: 
                # fetching title from line containing "<title>"
                
                self.title = line.split("<title>")[1].split("</title>")[0] 
                # print(self.title)

            if "<genre>" in line: 
                # fetching genre from line containing "<genre>"
                
                self.genre = line.split("<genre>")[1].split("</genre>")[0]    
                content = content + " " + self.genre 

            if "<keyword>" in line: 
                # fetching genre from line containing "<genre>"
                
                self.keywords = line.split("<keyword>")[1].split("</keyword>")[0]    
                content = content + " " + self.keywords

            if "<language>" in line: 
                # fetching language from line containing "<language>"
                
                self.language = line.split("<language>")[1].split("</language>")[0]
                content = content + " " + self.language   

            if "<country>" in line: 
                # fetching country from line containing "<country>"
                
                self.country = line.split("<country>")[1].split("</country>")[0]      
                content = content + " " + self.country   

                
            if "<actor>" in line and count <= 3:
                # concatenating all lines within a single doc

                # self.cast.append(line.split("<actor>")[1].split("</actor>")[0])   
                self.cast = line.split("<actor>")[1].split("</actor>")[0]
                content = content + " " + self.cast 
                count += 1
                

            if "<plot>" in line: 
                self.plot = line.split("<plot>")[1].split("</plot>")[0]   
                content = content + " " + self.plot 

                if "</doc>" in line:
                    break

            if line == None:
                self.text_file.close()      
          
        # print( self.docNo + "|" + self.title + "|" + content)

        return [self.docNo, self.title, content]
