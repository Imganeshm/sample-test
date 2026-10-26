def run_quiz():
    # 1. Setup the quiz data (Questions, Options, and Answers)
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pt", "B) .pyt", "C) .py", "D) .python"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["A) function", "B) def", "C) fun", "D) define"],
            "answer": "B"
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
            "answer": "B"
        },
        {
            "question": "What is a correct syntax to output 'Hello World' in Python?",
            "options":["A) print('Hello World')", "B) p('Hello World')", "C) echo'Hello World'", "D) echo('Hello World');"],
            "answer": "A"
        },
        {
            "question": "In Python, 'Hello', is the same as 'Hello'?",
            "options": ["A) False", "B) True"],
            "answer" : "B"
        },
        {
            "question": "Which operator is used to multiply numbers?",
            "options" : ["A) *", "B) %", "C) x", "D) #"],
            "answer" : "A"
        },
        {
            "question": "Which operator can be used to compare two values?",
            "options" : ["A) <>", "B) ==","C) ><", "D) ="],
            "answer" : "B"
        },
        {
            "question" : "Which collection does not allow duplicate members?",
            "options" : ["A) Set", "B) List", "C) Tuple", "D) Dictionary"],
            "answer" : "A"
        },
        {
            "question" : "Which statement is used to stop a loop?",
            "options" : ["A) Return", "B) break","C) exit", "D) stop"],
            "answer" : "B"
        },
        {
            "question" : "Which collection is ordered, changeable, and allows duplicate members?",
            "options" : ["A) List", "B) Tuple", "C) Set", "D) Dictionary"],
            "answer" : "A"
        },
    ]

    score = 0
    print("--- Welcome to the Python Mini Quiz! --- \n")

    # 2. Loop through each question
    for index, q in enumerate(questions, start=1):
        print(f"Question {index}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Take input and normalize it to uppercase
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # 3. Check the answer
        if user_answer == q['answer']:
            print("✨ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {q['answer']}.\n")

    # 4. Display Final Results
    print("--- Quiz Finished! ---")
    print(f"Your final score is: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Grade: {percentage:.1f}%")

if __name__ == "__main__":
    run_quiz()
