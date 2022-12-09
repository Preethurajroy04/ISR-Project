import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.

        self.stopword_file = open(Path.StopwordDir, "r", encoding="utf8") # opening the file in read mode

        self.stop_words = self.stopword_file.readlines()     # read all lines into a list containing stop words

        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.

        for index in range(0, len(self.stop_words)):
            self.stop_words[index] = self.stop_words[index].strip()  # striping whitespaces in each stop word

        if word in self.stop_words:
            # if stop word in stop_words list return True, else False
            return True
        return False
