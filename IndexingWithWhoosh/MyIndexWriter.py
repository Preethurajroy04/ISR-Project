import os
import Classes.Path as Path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import RegexTokenizer, StemmingAnalyzer


# Efficiency and memory cost should be paid with extra attention.
class MyIndexWriter:

    writer = []

    def __init__(self, type):
        
        path_dir = Path.IndexImdb
        
        os.makedirs(path_dir, exist_ok=True)
        schema = Schema(doc_no=ID(stored=True),doc_title=STORED,
                        doc_content=TEXT(analyzer=StemmingAnalyzer(), stored=True))
        indexing = index.create_in(path_dir, schema)
        self.writer = indexing.writer()
        return

    # This method build index for each document.
    # NT: in your implementation of the index, you should transform your string docno into non-negative integer docids,
    # and in MyIndexReader, you should be able to request the integer docid for each docno.
    def index(self, docNo, title, content):
        self.writer.add_document(doc_no = docNo, doc_title = title, doc_content = content)
        return

    # Close the index writer, and you should output all the buffered content (if any).
    def close(self):
        self.writer.commit()
        return
