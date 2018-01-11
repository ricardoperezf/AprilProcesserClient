from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/start')
def post_server():
    book = open('Ortega Y Gasset, José - El Sentido Histórico De La Teoría De Einstein.txt', 'r')
    word = book.read()
    post_request = requests.post('http://192.168.0.15:5000/api/v1/text', data={"text_file": str(word)})
    print(post_request.text)
    return render_template('./index.html', resultado=post_request.json())


@app.route('/result')
def get_final_result():
    get_request = requests.get('http://192.168.0.15:5000/api/v1/text')
    print(get_request.text)
    return render_template('./result.html', resultado=get_request.json())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
