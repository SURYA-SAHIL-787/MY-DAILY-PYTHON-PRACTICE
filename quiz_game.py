QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["list", "dict", "set", "tuple"],
        "answer": "D"
    },
    {
        "question": "What does len() return?",
        "options": [
            "Memory address",
            "Object type",
            "Number of items",
            "Variable name"
        ],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "B"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "C"
    }
]


def display_question(question_data, number):
    print(f"\nQuestion {number}: {question_data['question']}")

    labels = ["A", "B", "C", "D"]

    for label, option in zip(labels, question_data["options"]):
        print(f"{label}. {option}")


def get_answer():
    valid_answers = {"A", "B", "C", "D"}

    while True:
        answer = input("Enter answer A/B/C/D: ").strip().upper()

        if answer in valid_answers:
            return answer

        print("Invalid answer. Choose A, B, C, or D.")


def calculate_percentage(score, total):
    if total == 0:
        return 0

    return (score / total) * 100


def show_result(score, total):
    percentage = calculate_percentage(score, total)

    print("\n===== QUIZ RESULT =====")
    print(f"Correct Answers: {score}")
    print(f"Total Questions: {total}")
    print(f"Percentage     : {percentage:.2f}%")

    if percentage == 100:
        print("Grade: Perfect")
    elif percentage >= 80:
        print("Grade: Excellent")
    elif percentage >= 60:
        print("Grade: Good")
    elif percentage >= 40:
        print("Grade: Average")
    else:
        print("Grade: Needs Improvement")


def run_quiz():
    score = 0
    total = len(QUESTIONS)

    for index, question_data in enumerate(QUESTIONS, start=1):
        display_question(question_data, index)
        user_answer = get_answer()

        if user_answer == question_data["answer"]:
            print("Correct.")
            score += 1
        else:
            correct = question_data["answer"]
            print(f"Wrong. Correct answer is {correct}.")

    show_result(score, total)


def menu():
    while True:
        print("\n===== QUIZ GAME =====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Exiting Quiz Game.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
