from converters.devanagari_brahmi import TextProcessor


class PrakritBrahmiConverter:

    @staticmethod
    def convert(text):

        text = text.strip()

        return TextProcessor.devanagari_to_brahmi(text)