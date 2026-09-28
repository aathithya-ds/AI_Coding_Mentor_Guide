import random
from datetime import datetime


class AICodingMentor:
    def __init__(self):
        self.concepts = {
            "variable": {
                "explanation": (
                    "A variable is a name used to store a value in a program."
                ),
                "example": "name = 'Aathithya'\nage = 21",
                "difficulty": "Beginner",
                "keywords": ["variable", "value", "assignment"]
            },

            "function": {
                "explanation": (
                    "A function is a reusable block of code that performs a "
                    "specific task."
                ),
                "example": (
                    "def add(a, b):\n"
                    "    return a + b"
                ),
                "difficulty": "Beginner",
                "keywords": ["function", "def", "return"]
            },

            "loop": {
                "explanation": (
                    "A loop is used to execute a block of code repeatedly."
                ),
                "example": (
                    "for i in range(5):\n"
                    "    print(i)"
                ),
                "difficulty": "Beginner",
                "keywords": ["loop", "for", "while", "iteration"]
            },

            "list": {
                "explanation": (
                    "A list is an ordered collection that can store multiple "
                    "values."
                ),
                "example": (
                    "fruits = ['apple', 'banana', 'orange']"
                ),
                "difficulty": "Beginner",
                "keywords": ["list", "append", "remove"]
            },

            "dictionary": {
                "explanation": (
                    "A dictionary stores data using key-value pairs."
                ),
                "example": (
                    "student = {'name': 'Aathithya', 'age': 21}"
                ),
                "difficulty": "Intermediate",
                "keywords": ["dictionary", "key", "value"]
            },

            "class": {
                "explanation": (
                    "A class is a blueprint used to create objects in "
                    "object-oriented programming."
                ),
                "example": (
                    "class Student:\n"
                    "    def __init__(self, name):\n"
                    "        self.name = name"
                ),
                "difficulty": "Intermediate",
                "keywords": ["class", "object", "OOP"]
            },

            "exception": {
                "explanation": (
                    "Exception handling is used to handle runtime errors "
                    "without crashing the program."
                ),
                "example": (
                    "try:\n"
                    "    result = 10 / 0\n"
                    "except ZeroDivisionError:\n"
                    "    print('Cannot divide by zero')"
                ),
                "difficulty": "Intermediate",
                "keywords": ["exception", "try", "except", "error"]
            }
        }

        self.student_progress = {}

    def learn_concept(self, concept_name):
        """Return information about a programming concept."""

        concept_name = concept_name.lower().strip()

        if concept_name not in self.concepts:
            available = ", ".join(self.concepts.keys())

            return (
                f"Concept '{concept_name}' was not found.\n"
                f"Available concepts: {available}"
            )

        concept = self.concepts[concept_name]

        return f"""
========================================
        AI CODING MENTOR
========================================

Concept      : {concept_name.capitalize()}
Difficulty   : {concept['difficulty']}

Explanation:
{concept['explanation']}

Example:
{concept['example']}

Keywords:
{', '.join(concept['keywords'])}

========================================
"""

    def explain_code(self, code):
        """Provide a basic explanation of Python code."""

        explanation = []

        if "def " in code:
            explanation.append(
                "✓ Function definition detected."
            )

        if "class " in code:
            explanation.append(
                "✓ Class definition detected."
            )

        if "for " in code or "while " in code:
            explanation.append(
                "✓ Loop detected. The code performs repetition."
            )

        if "if " in code:
            explanation.append(
                "✓ Conditional statement detected."
            )

        if "try:" in code and "except" in code:
            explanation.append(
                "✓ Exception handling detected."
            )

        if "import " in code:
            explanation.append(
                "✓ External module import detected."
            )

        if "return " in code:
            explanation.append(
                "✓ Return statement detected."
            )

        if "print(" in code:
            explanation.append(
                "✓ Print statement detected."
            )

        if not explanation:
            explanation.append(
                "The code contains basic Python statements."
            )

        return "\n".join(explanation)

    def detect_basic_errors(self, code):
        """Detect some common Python coding mistakes."""

        errors = []

        if "def " in code:
            lines = code.splitlines()

            for line in lines:
                stripped = line.strip()

                if stripped.startswith("def ") and not stripped.endswith(":"):
                    errors.append(
                        "❌ Function definition may be missing ':'"
                    )

        if "if " in code:
            lines = code.splitlines()

            for line in lines:
                stripped = line.strip()

                if stripped.startswith("if ") and not stripped.endswith(":"):
                    errors.append(
                        "❌ If statement may be missing ':'"
                    )

        if code.count("(") != code.count(")"):
            errors.append(
                "❌ Mismatched parentheses detected."
            )

        if code.count("[") != code.count("]"):
            errors.append(
                "❌ Mismatched square brackets detected."
            )

        if errors:
            return "\n".join(errors)

        return "✅ No obvious basic errors detected."

    def suggest_improvements(self, code):
        """Suggest simple improvements for Python code."""

        suggestions = []

        if len(code.splitlines()) > 15:
            suggestions.append(
                "💡 Consider dividing the code into smaller functions."
            )

        if "print(" in code:
            suggestions.append(
                "💡 Use print() for output and return values when "
                "building reusable functions."
            )

        if "#" not in code:
            suggestions.append(
                "💡 Consider adding comments to explain important logic."
            )

        if not suggestions:
            suggestions.append(
                "✅ Code looks reasonably simple. Keep practicing clean coding."
            )

        return "\n".join(suggestions)

    def get_practice_problem(self, concept, difficulty="Beginner"):
        """Generate a programming practice problem."""

        problems = {
            "Beginner": [
                "Write a function that adds two numbers.",
                "Create a list containing five fruits.",
                "Print numbers from 1 to 10 using a loop.",
                "Create a variable containing your name.",
                "Write a program to check whether a number is even or odd."
            ],

            "Intermediate": [
                "Write a function to check whether a number is prime.",
                "Create a dictionary containing student marks.",
                "Create a class representing a bank account.",
                "Write a program to count word frequency.",
                "Implement exception handling for division."
            ],

            "Advanced": [
                "Implement binary search using a Python function.",
                "Create a custom exception class.",
                "Implement a simple decorator for execution time.",
                "Build a basic recommendation system.",
                "Implement a small object-oriented application."
            ]
        }

        selected = random.choice(
            problems.get(difficulty, problems["Beginner"])
        )

        return f"""
========================================
        PRACTICE PROBLEM
========================================

Concept    : {concept}
Difficulty : {difficulty}

Problem:
{selected}

Hint:
Try to use the concept '{concept}' while solving this problem.

========================================
"""

    def start_session(self, student_id):
        """Start a mentor session for a student."""

        if student_id not in self.student_progress:
            self.student_progress[student_id] = {
                "concepts_learned": [],
                "problems_solved": [],
                "score": 0,
                "sessions": 0,
                "last_session": None
            }

        self.student_progress[student_id]["sessions"] += 1
        self.student_progress[student_id]["last_session"] = (
            datetime.now().isoformat()
        )

        return f"""
========================================
       AI CODING MENTOR GUIDE
========================================

Student ID : {student_id}

Welcome to your AI Coding Mentor!

Available features:

1. Learn programming concepts
2. Explain Python code
3. Detect basic coding errors
4. Generate practice problems
5. Suggest code improvements
6. Track learning progress

Session started successfully.

========================================
"""

    def get_progress(self, student_id):
        """Return student learning progress."""

        if student_id not in self.student_progress:
            return "No student progress found."

        progress = self.student_progress[student_id]

        return f"""
========================================
          STUDENT PROGRESS
========================================

Student ID        : {student_id}
Sessions          : {progress['sessions']}
Concepts Learned  : {len(progress['concepts_learned'])}
Problems Solved   : {len(progress['problems_solved'])}
Score             : {progress['score']}

Last Session:
{progress['last_session']}

========================================
"""


def main():
    mentor = AICodingMentor()

    student_id = "DAS004308"

    print(mentor.start_session(student_id))

    print("\n--- CONCEPT LEARNING ---")
    print(mentor.learn_concept("function"))

    print("\n--- CODE EXPLANATION ---")

    sample_code = """
def add(a, b):
    return a + b
"""

    print(sample_code)
    print(mentor.explain_code(sample_code))

    print("\n--- ERROR DETECTION ---")

    buggy_code = """
def add(a, b)
    return a + b
"""

    print(buggy_code)
    print(mentor.detect_basic_errors(buggy_code))

    print("\n--- CODE IMPROVEMENT ---")
    print(mentor.suggest_improvements(sample_code))

    print("\n--- PRACTICE PROBLEM ---")
    print(
        mentor.get_practice_problem(
            "function",
            "Beginner"
        )
    )

    print("\n--- STUDENT PROGRESS ---")
    print(mentor.get_progress(student_id))


if __name__ == "__main__":
    main()