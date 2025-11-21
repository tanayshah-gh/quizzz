# Command-Line Quiz Engine

A dynamic quiz application built in **Python** that runs entirely within the command line. It automatically loads questions and answers from external CSV files, providing a customizable tool for knowledge assessment.

## 🎯 Project Goal (SDG Alignment)

This project aligns with the **Sustainable Development Goal (SDG) 4: Quality Education** by offering a simple, accessible, and easily customizable tool for interactive learning and knowledge assessment. The use of easily editable CSV files allows for rapid creation and deployment of new educational content.

-----

## ✨ Key Features

  * **Dynamic Loading:** Discovers and loads multiple quiz topics from the dedicated `./quizzes` folder.
  * **CSV Parsing:** Robustly parses question and answer pairs from CSV files with built-in error handling.
  * **Robust Input:** Handles user answers with case-insensitivity and ignores leading/trailing whitespace.
  * **Score Tracking:** Provides a final score summary upon quiz completion.
  * **Force Exit:** Allows users to gracefully **exit the quiz** at any time by typing 'quit' or 'exit' and displays their current score upon forced termination.

-----

## 🚀 Getting Started

### Prerequisites

To run this project, you only need **Python 3** and **Git** installed on your system.

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/quiz_engine.git
    cd quiz_engine
    ```
2.  **Verify Setup:** Ensure your current directory contains `quiz_engine.py` and the `quizzes` folder.

### How to Run the Quiz

Execute the main script using the Python interpreter from the project's root directory:

```bash
python quiz_engine.py
```

The script will launch, display a list of available quizzes, and prompt you to select one by number.

-----

## 📂 Quiz File Structure

The application requires all quiz data to be stored in the `./quizzes` directory using the **CSV format** (`.csv`). The file name (without the `.csv` extension) becomes the quiz topic name.

Each quiz file must follow a strict two-column structure:

| Column 1 | Column 2 |
| :--- | :--- |
| **Question** | **Correct Answer** |

**Example: `./quizzes/history_basics.csv`**

```csv
What is the capital of France?,Paris
In what year did the Titanic sink?,1912
```

-----

## 🧑‍💻 Technical Details (Development History)

The core logic is built using a **procedural modeling style** and emphasizes reliable **File Handling** using Python's standard library modules (`csv`, `os`, `glob`).

The project's commit history demonstrates a clear, staged development process, covering:

1.  Project Initialization and File Structure.
2.  Quiz File Discovery and Selection Logic.
3.  Robust CSV Data Loading and Parsing.
4.  Core Question Iteration and User Interaction.
5.  Refinement of Answer Comparison and Input Validation.
6.  Final Code Structure Review and Readiness.
7.  Addition of Sample Quiz Data.
8.  **Implementation of the Force-Exit Feature.**

-----

## 📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.