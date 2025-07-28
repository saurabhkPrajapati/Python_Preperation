class FrenchLocalizer:
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg


# Define the Creator (Factory) class
class Factory:

    @staticmethod
    def language_factory(language1):
        """Factory_Method"""
        localizers = {
            "French": FrenchLocalizer,
            "English": EnglishLocalizer,
            "Spanish": SpanishLocalizer,
        }

        return localizers[language1]()


if __name__ == "__main__":

    f = Factory.language_factory("French")
    e = Factory.language_factory("English")
    s = Factory.language_factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
