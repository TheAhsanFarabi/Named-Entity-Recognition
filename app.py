from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_lg")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def ner():
    text = request.json.get('text')
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True)
