import Classes.Path as Path

class PreprocessedCorpusReader:

    corpus = 0

    def __init__(self, type):
        self.corpus = open(Path.Result, "r", encoding="utf8")

    def nextDocument(self):
        line = self.corpus.readline().split('|').strip()
        docNo = line[0]
        title = line[1]
        content = line[2]
        if docNo=="":
            self.corpus.close()
            return
        
        return [docNo, title, content]
