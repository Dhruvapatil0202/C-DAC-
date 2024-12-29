from flask import Flask, request, render_template
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
import joblib

app = Flask(__name__)

# define analyzer function
def clean_text(sent):
    tokens1 = word_tokenize(sent)
    tokens2 = [token for token in tokens1 if token.isalnum()]
    tokens3 = [token for token in tokens2 if token.lower() not in swords]
    tokens4 = [ps.stem(token) for token in tokens3]
    return tokens4

classifier = joblib.load('classifier.model')
tfidf = joblib.load('tfidf.model')


@app.route('/')
def spamdetector():
    return render_template('spamdetector.html')

@app.route('/spamdetector', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]
        return render_template('spamoutput.html', data = data)

if __name__ == '__main__':
    app.run()



