class Tokenizer:
    def __init__(self, text, **kwargs):
        print('Tokenizer.__init__()')
        self.tokens = text.split()


class WordCounter(Tokenizer):
    def __init__(self, text, **kwargs):
        print('WordCounter.__init__()')
        super().__init__(text, **kwargs)
        self.word_count = len(self.tokens)


class Vocabulary(Tokenizer):
    def __init__(self, text, lang='en', **kwargs):
        print('Vocabulary.__init__()')
        super().__init__(text, **kwargs)
        self.lang = lang
        self.vocab = set(self.tokens)


class TextDescriber(WordCounter, Vocabulary):
    def __init__(self, text, **kwargs):
        print('TextDescriber.__init__()')
        super().__init__(text, **kwargs)


td = TextDescriber("hello hello world", lang="en")
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)