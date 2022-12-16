import json
from gtts import gTTS
import os

dbFile = open('RSI-Ideathon-POC/db.json')
data = json.load(dbFile)

os.chdir("RSI-Ideathon-POC/audio files")
for item in data:
    fileName = item["question"] + ".mp3"
    print("File name :: ", fileName)
    textToConvert = item["answer"]
    audioFile = gTTS(text=textToConvert, lang='en', slow=False)
    audioFile.save(fileName)
