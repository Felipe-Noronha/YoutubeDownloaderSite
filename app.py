from flask import Flask, render_template, request
from pytube import YouTube
from pytube.exceptions import RegexMatchError

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form['link']
    if link:
        try:
            pasta = './'
            YouTube(link).streams.get_highest_resolution().download(pasta)
            return render_template('success.html')
        except RegexMatchError:
            return render_template('error.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
