class Reverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        words.reverse()
        return " ".join(words)

r = Reverser("rolled rick get haaa")
print(r.reverse_words())
