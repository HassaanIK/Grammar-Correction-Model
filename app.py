from flask import Flask, render_template, request
from model import GrammarChecker

app = Flask(__name__)
spell_checker_module = GrammarChecker()

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell',methods=['POST','GET'])
def spell():
    if request.method=='POST':
        text = request.form['text']
        corrected_grammar = spell_checker_module.correct_grammar(text)
    return render_template('index.html', corrected_grammar=corrected_grammar)
    
@app.route('/grammar',methods=['POST','GET'])
def grammar():
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        corrected_file_grammar = spell_checker_module.correct_grammar(readable_file)
    return render_template('index.html', corrected_file_grammar=corrected_file_grammar)

# python main
if __name__ == "__main__":
    app.run(debug=True)