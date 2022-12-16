from flask import Flask, jsonify, request

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

def notifyCSupport(question):
    print("Customer Support will update from here.")

@app.route('/')
def index():
    return "Welcome to /"

@app.route('/getAllData', methods=['GET'])
def getAllData():
    return jsonify({"DataFromDB":data})

@app.route('/ask/', methods=['GET'])
def getAnswer():
    question = request.data.decode()
    question = question.strip()
    notExists = True
    for item in data:
        if question==item["question"]:
            notExists = False
            return item["answer"]
    if notExists:
        newQuestionTemplate = {"question": question,
                                "answer": "Yet to answer"}
        data.append(newQuestionTemplate)
        notifyCSupport(question)
        return "New Question, please wait for customer support to answer"

if __name__ =="__main__":
    app.run(debug=True)