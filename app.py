from flask import Flask, render_template, request
from grammar import correct_grammar
from happytransformer import HappyTextToText, TTSettings
import difflib

app = Flask(__name__)

# Load the grammar correction model
# grammar_model = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

# Load the saved model
model = HappyTextToText("T5", "model1.safetensors")
beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text, corrected_words, count = correct_grammar(text, model, beam_settings)
        return render_template('result.html', correct_text=corrected_text, corrected_words=corrected_words, count=count)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
