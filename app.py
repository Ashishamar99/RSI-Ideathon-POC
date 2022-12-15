from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        'question': 'What are the policies of the organization ?',
        'answer': 'In the box URL'
    },
    {
        'question': 'Where is the holiday calendar stored ?',
        'answer': 'In the box URL'
    }
        ]

@app.route('/')
def index():
    return "Welcome to /"

@app.route('/getAllData', methods=['GET'])
def getAllData():
    return jsonify({"DataFromDB":data})

if __name__ =="__main__":
    app.run(debug=True)