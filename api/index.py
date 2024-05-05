from flask import Flask, request, jsonify
from api.gemini_chat import gemini

CORS(app)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/test')
def test():
    return 'this is the test route'


@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':

        promt = request.json.get('data', '')
        
        print(promt)
        print(type(promt))


        response = gemini(promt)

        return jsonify({"response": response}) 




if __name__ == '__main__':
    app.run(debug=True)