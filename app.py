from flask import Flask, jsonify, request
import json
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os

app = Flask(__name__)

print('db.json' in os.listdir('.'))
if 'db.json' in os.listdir('.'):
    fullPath = os.path.join(os.getcwd(), 'db.json')
    with open(fullPath, 'rt') as dbFile:
        data = json.load(dbFile)

def calculateFuzzyRatios(originalRecord, frontEndInput):
    similarityRatio = fuzz.ratio(originalRecord, frontEndInput)
    tokenSortRatio = fuzz.token_sort_ratio(originalRecord, frontEndInput)
    averageRatio = sum([similarityRatio, tokenSortRatio])/2
    print("Average Ratio::", averageRatio, "Original Question:: ", originalRecord)
    if(averageRatio >= 78):
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
    question = request.args.get('question')
    # question = request.data.decode()
    question = question.strip()
    question = question.lower()
    notExists = True
    for item in data:
        if calculateFuzzyRatios(item["question"].lower(), question.lower()):
            notExists = False
            response = jsonify({"answer":item["answer"], "link":item["link"]})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
    if notExists:
        return "I'm sorry, but it looks like the message you have sent is not in a recognizable language or beyond my knowledge. Can you please provide a question or statement in a language that I can understand so that I can better assist you?"

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=4005, debug=True)