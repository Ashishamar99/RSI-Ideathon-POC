import json
from gtts import gTTS
import os

with open('db.json', 'rt') as dbFile:
    data = json.load(dbFile)

os.chdir("audio files")
for item in data:
    fileName = item["question"] + ".mp3"
    print("File name :: ", fileName)
    textToConvert = item["answer"]
    audioFile = gTTS(text=textToConvert, lang='en', slow=False)
    audioFile.save(fileName)
