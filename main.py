from docx import Document


name = input("Insert document name here: ")
document = Document(name)

word_questions=[]
for paragraf in document.paragraphs:
    word_questions.append(paragraf.text.strip())

# print(word_questions)

def validate(question):
    if not question["question"]:
        print(f"ERROR: Question {question['num']} has no text.")
        return False

    if len(question["answers"])<2 or len(question["answers"])>4:
        print(f"ERROR: Question {question_number} has {len(answers)} answers.")
        return False

    correct_answers = 0

    for ans in question["answers"]:

        if "[0]" not in ans and "[1]" not in ans:
            print(f"ERROR: Missing [0]/[1] marker in question {question['num']}.")
            return False
        marker = ans.split("[")[1].split("]")[0]
        if marker not in ("0", "1"):
            print("Invalid marker")
            return False
        text = ans.replace("[0]", "").replace("[1]", "").strip()
        if len(text)<=3:
            print(f"ERROR: Empty answer in question {question['num']}.")
            return False
        if "[1]" in ans:
            correct_answers+=1

    if correct_answers == 0:
        print(f"Question {question['num']} has no correct answer.")
        return False
    if correct_answers>1:
        print(f"Question {question['num']} has more then one correct answer.")
        return False
    return True



questions = []

current_question = None
question_number = None
answers = []

for line in word_questions:
    if "[MC]" in line:
        if current_question:
            qu = {
                "num": question_number,
                "question": current_question,
                "answers": answers,
            }
            if validate(qu):
                questions.append(qu)
        answers = []
        question_number = line.split(".")[0]
        current_question = line.split("]")[1].strip()

    elif line.startswith(("a", "b", "c", "d", "A", "B", "C", "D")):
        answers.append(line.strip())

# Adding the last question

qu = {
    "num": question_number,
    "question": current_question,
    "answers": answers,
}

if validate(qu):
    questions.append(qu)




# GIFT

gift = ""
for q in questions:
    gift += f"// question: {q["num"]}\n"
    gift += f"::::[choice]<p>{q['question']}</p>{{\n"

    for answer in q["answers"]:
        if "[1]" in answer:
            gift += f"\t=%100%{answer[7:]}#Correct!\n"
        else:
            gift += f"\t~%0%{answer[7:]}#Incorrect!\n"
    gift+="\n}\n"


with open("quiz.gift", "w", encoding="utf-8") as file:
    file.write(gift)










