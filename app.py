from flask import Flask, jsonify, request
import json
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

app = Flask(__name__)

dbFile = open('/Users/ashish.amar/Documents/Ideathon Chatbot/RSI-Ideathon-POC/db.json')
data = json.load(dbFile)

def notifyCSupport(question):
    print("Customer Support will update from here.")

def calculateFuzzyRatios(originalRecord, frontEndInput):
    similarityRatio = fuzz.ratio(originalRecord, frontEndInput)
    tokenSortRatio = fuzz.token_sort_ratio(originalRecord, frontEndInput)
    averageRatio = sum([similarityRatio, tokenSortRatio])/2
    print("Average Ratio::", averageRatio, "Question:: ", originalRecord)
    if(averageRatio > 80):
        return True

@app.route('/')
def index():
    return "Welcome to /"

@app.route('/getAllData', methods=['GET'])
def getAllData():
    response = jsonify({"DataFromDB":data})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/ask/', methods=['GET'])
def getAnswer():
    question = request.data.decode()
    question = question.strip()
    question = question.lower()
    notExists = True
    for item in data:
        if calculateFuzzyRatios(item["question"].lower(), question.lower()):
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