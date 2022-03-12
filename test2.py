from fileinput import filename
import json

filename = 'JeopardyQuestions.json'
with open(filename) as f:
    questions = json.load(f)

print(questions[0]['Question'])