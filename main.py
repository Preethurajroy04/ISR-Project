import PreProcessData.PreProcessCorpus as PreProcessCorpus
import Classes.Path as Path


def doc_preprocess():

    '''
    pre-process the whole corpus
    and write into a text file
    '''

    # intialize result file object
    result_file_obj = open(Path.result_path, "w", encoding="utf8")
    
    # intialize PreProcessCorpus class object
    collection = PreProcessCorpus.PreProcessCorpus()
    doc = []


    while True:
        
        doc = collection.parse_document()

        if doc == None or doc == ["", "", ""]:
            break
        
        # store results returned from parse_document() into variables
        docNo = doc[0]
        title = doc[1]
        content = doc[2]

        # write info retrieved from the corpus into a pipe delimited file
        result_file_obj.write(docNo + "|" + title + "|" + content + "\n")

    # close the file
    result_file_obj.close()
        

def main():

    '''
    call doc_preprocess() 
    '''

    doc_preprocess()
    

if __name__ == "__main__":
    main()