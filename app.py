from flask import Flask, jsonify, request
import json

app = Flask(__name__)

dbFile = open('/Users/ashish.amar/Documents/Ideathon Chatbot/RSI-Ideathon-POC/db.json')
data = json.load(dbFile)

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