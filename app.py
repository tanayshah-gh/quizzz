import csv
import glob
import os

QUIZ_FOLDER = 'quizzes'

def find_quiz_files():
    search_path = os.path.join(QUIZ_FOLDER, '*.csv')
    quiz_files = glob.glob(search_path)
    return quiz_files


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


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()