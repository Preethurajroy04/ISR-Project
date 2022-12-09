import PreProcessData.preprocess_corpus as PreProcessCorpus
# # import PreProcessData.StopWordRemover as StopWordRemover
# import PreProcessData.WordNormalizer as WordNormalizer
# import PreProcessData.WordTokenizer as WordTokenizer
import Classes.Path as Path
import datetime

 # !!! YOU CANNOT CHANGE ANYTHING IN THIS CLASS !!! This is for INFSCI 2140 in Fall 2022

def PreProcess():

    wr = open(Path.ResultHM1, "w", encoding="utf8")
    doc = []
    
    # Initialize essential objects.

    collection = PreProcessCorpus.PreProcessCorpus()

    while True:
        doc = collection.nextDocument()
        if doc == None or doc == ["", "", ""]:
            break

        docNo = doc[0]
        title = doc[1]
        content = doc[2]

        wr.write(docNo + "|" + title + "|" + content + "\n")

        # print(docNo + "|" + title + "|" + content)

    wr.close()
        
    #     normalizer = WordNormalizer.WordNormalizer(content)

    # while True:
    #     word = normalizer.lowercase()
    #     if word == None:
    #         break
    #     word = normalizer.stopword(word)
    #     word = normalizer.tokenize(word)


    #     # Output the docNo.
    #     wr.write(docNo+"\n")
    #     wr.write(normalizer.stem(word) + " ")


def main():
    PreProcess()
    

if __name__ == "__main__":
    main()