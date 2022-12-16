import json
import urllib.parse
import os

with open('q&a.json', 'rt') as dbFile:
    data = json.load(dbFile)

for item in data:
    item['link'] = urllib.parse.quote(os.path.join(os.getcwd(), 'audio files', item['question'] + '.mp3'))

with open('db.json', 'w', encoding='utf-8') as dbFile:
    json.dump(data, dbFile, ensure_ascii=False, indent=4)