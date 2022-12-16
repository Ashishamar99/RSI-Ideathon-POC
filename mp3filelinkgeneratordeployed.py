import json
import urllib.parse
import os

print('q&a.json' in os.listdir('.'))
if 'q&a.json' in os.listdir('.'):
    fullPath = os.path.join(os.getcwd(), 'q&a.json')
    with open(fullPath, 'rt') as dbFile:
        data = json.load(dbFile)
basePath = 'https://www.pythonanywhere.com/user/MayaDak/files/home/MayaDak/'
for item in data:
    basePath + urllib.parse.quote('audio files' + item['question'] + '.mp3')
    item['link'] = basePath + urllib.parse.quote('audio files/' + item['question'] + '.mp3')

with open('db.json', 'w', encoding='utf-8') as dbFile:
    json.dump(data, dbFile, ensure_ascii=False, indent=4)