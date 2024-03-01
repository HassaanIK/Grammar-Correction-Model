from happytransformer import HappyTextToText, TTSettings
import difflib

def correct_grammar(text, model, beam):
    # Generate corrected text from the grammar model
    matches = model.generate_text(text, args=beam)

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
