from happytransformer import HappyTextToText, TTSettings
import difflib

grammar_model = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

class GrammarChecker:
    def __init__(self):
        self.grammar_check = grammar_model

    def correct_grammar(self, text):
        # Generate corrected text from the grammar model
        matches = self.grammar_check.generate_text(text, args=beam_settings)

        # Extract original and corrected text
        original_text = text
        corrected_text = matches.text if matches and matches.text else text

        # Calculate the differences between original and corrected text
        differences = list(difflib.ndiff(original_text.split(), corrected_text.split()))

        # Extract corrected words
        corrected_words = [word[2:] for word in differences if word.startswith('+ ')]

        # Calculate the total count of found mistakes
        foundmistakes_count = len(corrected_words)

        return corrected_text, corrected_words, foundmistakes_count

if __name__ == "__main__":
    obj = GrammarChecker()
    message = "they is going to spent time together."
    corrected_text, corrected_words, count = obj.correct_grammar(message)

    print("Output Text:", corrected_text)
    print("Corrected Words:", corrected_words)
    print("Count of Corrected Words:", count)
