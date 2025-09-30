import random
question = {"capital od ]f india?":"Delhi",
            "2+2=?":"4",
            "colour of the sky?":"Blue",
           " largest planet in the solar system?":"jupitar",
           "python is ______ language? ":"programming"}
quiz = list(question.items())
random.shuffle(quiz)
score = 0
for q,a in quiz:
    user = input(q).strip().lower()
    if user == a.lower():
        print("correct!")
        score += 1
    else:  print(f"correct answer : {a}")
total = len(question)
percentage = (score/total)*100
print(f"your score:{score}/{total},percentage = {percentage: .1f}%")  
