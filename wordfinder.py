import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    def __init__(self, file_path):
        self.words = self.read_words("words.txt")

    def read_words(self, file_path):
        with open("words.txt", 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words

    def random(self):
        if self.words:
            return random.choice(self.words)
        else:
            return None

    def __str__(self):
        return f"{len(self.words)} words read"
    
class SpecialWordFinder(WordFinder):
    def read_words(self, file_path):
        with open("words.txt", 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words

wf = WordFinder("words.txt")
print(wf.random())

swf = SpecialWordFinder("words.txt")
print(swf.random())
