# Grammar Correction Web App

### Overview
This project implements a web-based tool for correcting grammatical errors in text using the pretrained `vennify/t5-base-grammar-correction` model. The tool allows users to input text, which is then processed by the model to correct grammar and provide a count of corrected words.

### Uses of the Model
The primary use case for this model is to enhance the grammatical correctness of input text. It serves as a valuable tool for content creators, writers, and individuals seeking to improve the quality of written content. The model is particularly useful in applications where clear and error-free communication is essential, such as in document preparation, content editing, and educational materials.

### Project Structure
- `app.py`: Flask application for the web interface.
- `model.py`: Contains the `correct_grammar` function for grammar correction.
- `templates/index.html`: HTML template for the input form.
- `templates/result.html`: HTML template for displaying the correction result.

### How to use
1. Clone the repository `git clone https://github.com/your-username/grammar-correction-tool.git`.
2. Install the dependencies `pip install -r requirements.txt`.
3. Run the Flask application `python app.py`.

### Functionality
- The `correct_grammar` function in model.py takes input text and uses the `vennify/t5-base-grammar-correction` model to correct grammar.It returns the corrected text, a list of corrected words, and the count of corrected words.
- The main functionality of the model.py includes:
  - Initializing the T5 grammar correction model (`vennify/t5-base-grammar-correction`) using `HappyTransformer`.
  - Defining the `correct_grammar` function, which takes input text, the initialized model, and beam settings as arguments.
  - Generating corrected text from the grammar model using the `generate_text` method.
  - Extracting original and corrected text, calculating differences between them, and extracting corrected words.
  - Returning the corrected text, corrected words, and count of corrected words.

## Usage

```python
from transformers import pipeline
# Load the Grammar Correction T5 Model from Hugging Face
grammar_correction_model = pipeline(task="text2text-generation", model="hassaanik/grammar-correction-model")
# Input text with grammatical errors
input_text = "They is going to spent time together."
# Get corrected output and details
result = grammar_correction_model(input_text, max_length=200, num_beams=5, no_repeat_ngram_size=2)
# Print the corrected output
print(result)
