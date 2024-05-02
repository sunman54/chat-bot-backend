from flask import Flask, request, jsonify
from gemini_chat import gemini



app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

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