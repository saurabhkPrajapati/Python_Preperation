class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)


"""
td = TextDescriber('row row row your boat')

This calls TextDescriber.__init__()
Which calls super().__init__() → goes to WordCounter.__init__()
WordCounter.__init__() calls super().__init__() → next in MRO is Vocabulary.__init__()
Vocabulary.__init__() calls super().__init__() → now goes to Tokenizer.__init__()

So Tokenizer.__init__() is called once, as expected. 
It's just that both WordCounter and Vocabulary inherit from Tokenizer,
but Python avoids multiple calls to Tokenizer.__init__() due to cooperative multiple inheritance using super()
"""