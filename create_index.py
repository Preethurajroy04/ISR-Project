import IndexingWithWhoosh.PreProcessedCorpusReader as PreprocessedCorpusReader
import IndexingWithWhoosh.MyIndexWriter as MyIndexWriter
import IndexingWithWhoosh.MyIndexReader as MyIndexReader
import SearchWithWhoosh.QueryRetreivalModel as QueryRetreivalModel


def WriteIndex():
    # Initiate pre-processed collection file reader.
    corpus = PreprocessedCorpusReader.PreprocessedCorpusReader()
    # Initiate the index writer.
    indexWriter = MyIndexWriter.MyIndexWriter()
    # Build index of corpus document by document.
    while True:
        doc = corpus.nextDocument()
        if doc == None:
            break
        #print(doc[0])
        indexWriter.index(doc[0], doc[1], doc[2])
        
    indexWriter.close()
    return

def ReadIndex():
    # Initiate the index file reader.
    index = MyIndexReader.MyIndexReader()
    search = QueryRetreivalModel.QueryRetrievalModel(index)
    extractor = ExtractQuery.ExtractQuery()
    query= extractor.getQuries()
    results = search.retrieveQuery(query, 20)