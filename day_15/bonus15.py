import json


with open("questions15.json", 'r') as file:
    content = file.read()

data = json.loads(content)

# print(type(content))
# print(type(data))
score = 0
for question in data:
    print(question["question_text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(f"{index + 1}-{alternatives}")

    user_choice = int(input("Enter the number you think that is answer : "))
    question["user_choice"] = user_choice

    if question['user_choice'] == question['correct_answer']:
        print("correct ans")
    else:
        print("wrong ans")
score = score = 1
for index, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        result = "correct answer"
    else:
        result = "wrong answer"

    message = f"{index + 1}-{result} :- your answer is : {question['user_choice']}, correct answer : {question['correct_answer']}" \

    print(message)
# print(score, "/", 1len(data))