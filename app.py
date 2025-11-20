import csv
import glob
import os

QUIZ_FOLDER = 'quizzes'

def find_quiz_files():
    search_path = os.path.join(QUIZ_FOLDER, '*.csv')
    quiz_files = glob.glob(search_path)
    return quiz_files

def load_questions(filepath):
    questions = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    question_text = row[0].strip()
                    answer_text = row[1].strip()
                    questions.append({'question': question_text, 'answer': answer_text})
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred loading the file: {e}")
        return None
        
    return questions

def start_quiz(questions):
    if not questions:
        print("No questions loaded. The quiz cannot start.")
        return

    score = 0
    total_questions = len(questions)

    print("\n--- Quiz Starting! ---")

    for index, q_data in enumerate(questions):
        question = q_data['question']
        correct_answer = q_data['answer']
        
        print(f"\nQuestion {index + 1} of {total_questions}: {question}")
        
        user_answer = input("Your Answer (Type 'quit' or 'exit' to stop): ")
        
        if user_answer.strip().lower() in ('quit', 'exit'):
            print(f"\n--- Quiz Stopped by User! ---")
            print(f"Your score at the time of exit is: {score} out of {index + 1} questions attempted.")
            return 

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {correct_answer}")

    print("\n--- Quiz Complete! ---")
    print(f"Your final score is: {score} out of {total_questions}")

def main():
    print("Welcome to the Command-Line Quiz Engine!")

    quiz_files = find_quiz_files()
    if not quiz_files:
        print(f"No quiz files (.csv) found in the '{QUIZ_FOLDER}' directory.")
        print("Please create some quiz files and try again.")
        return

    print("Available quizzes:")
    for index, filepath in enumerate(quiz_files):
        filename = os.path.basename(filepath)
        topic_name = os.path.splitext(filename)[0]
        print(f"  {index + 1}: {topic_name.capitalize()}")

    choice = -1
    while choice < 1 or choice > len(quiz_files):
        try:
            choice_input = input(f"\nEnter the number of the quiz you want to take (1-{len(quiz_files)}): ")
            choice = int(choice_input)
            if not (1 <= choice <= len(quiz_files)):
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_filepath = quiz_files[choice - 1]
    print(f"Loading '{selected_filepath}'...")

    questions = load_questions(selected_filepath)

    if questions:
        print(f"Successfully loaded {len(questions)} questions. Ready to start quiz.")
        start_quiz(questions)


if __name__ == "__main__":
    main()