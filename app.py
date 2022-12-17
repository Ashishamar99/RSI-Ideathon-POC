from flask import Flask, jsonify, request
import json
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

print('db.json' in os.listdir('.'))
if 'db.json' in os.listdir('.'):
    fullPath = os.path.join(os.getcwd(), 'db.json')
    with open(fullPath, 'rt') as dbFile:
        data = json.load(dbFile)

def calculateFuzzyRatios(frontEndInput, matchingQuestions):
    for item in data:
        originalRecord = item["question"].lower()
        similarityRatio = fuzz.ratio(originalRecord, frontEndInput)
        tokenSortRatio = fuzz.token_sort_ratio(originalRecord, frontEndInput)
        averageRatio = sum([similarityRatio, tokenSortRatio])/2
        print("Average Ratio::", averageRatio, "Original Question:: ", originalRecord)
        if(averageRatio >= 80):
            matchingQuestions[originalRecord] = averageRatio
    print(matchingQuestions)

@app.route('/')
def index():
    return "Welcome to /"

@app.route('/getAllData', methods=['GET'])
@cross_origin()
def getAllData():
    response = jsonify({"DataFromDB":data})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/ask/', methods=['GET'])
def getAnswer():
    question = request.args.get('question')
    # question = request.data.decode()
    question = question.strip()
    question = question.lower()
    notExists = True
    matchingQuestions = dict()
    calculateFuzzyRatios(question, matchingQuestions)
    queryQuestion = str()
    if len(matchingQuestions) == 1:
        notExists = False
        queryQuestion = list(matchingQuestions.keys())[0]
    elif len(matchingQuestions) > 1:
        notExists = False
        maxMatchedValue = max(matchingQuestions.values())
        for key in matchingQuestions.keys():
            if matchingQuestions[key] == maxMatchedValue:
                queryQuestion = key
                notExists = False
    
    if notExists:
        response = jsonify({"answer":"I'm sorry, but it looks like the message you have sent is not in a recognizable language or beyond my knowledge. Can you please provide a question or statement in a language that I can understand so that I can better assist you?", "link":"No Link Found"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    else:
        for item in data:
            if item["question"].lower() == queryQuestion:
                response = jsonify({"answer":item["answer"], "link":item["link"]})
                response.headers.add("Access-Control-Allow-Origin", "*")
                return response

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=4005, debug=True)