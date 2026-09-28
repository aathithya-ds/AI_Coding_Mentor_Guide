import json
import os
from datetime import datetime


class ProgressTracker:

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        """Load student data from JSON file."""

        if not os.path.exists(self.filename):
            return {}

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError):
            return {}

    def save_data(self):
        """Save student data to JSON file."""

        with open(
            self.filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.students,
                file,
                indent=4
            )

    def create_student(self, student_id, name):
        """Create a new student profile."""

        if student_id not in self.students:

            self.students[student_id] = {
                "name": name,
                "sessions": 0,
                "concepts_learned": [],
                "problems_solved": [],
                "score": 0,
                "created_at": datetime.now().isoformat(),
                "last_active": None
            }

            self.save_data()

            return "Student profile created successfully."

        return "Student profile already exists."

    def start_session(self, student_id):
        """Record a mentor session."""

        if student_id not in self.students:
            return "Student not found."

        self.students[student_id]["sessions"] += 1

        self.students[student_id]["last_active"] = (
            datetime.now().isoformat()
        )

        self.save_data()

        return "Learning session recorded."

    def add_concept(self, student_id, concept):
        """Record a learned concept."""

        if student_id not in self.students:
            return "Student not found."

        concept = concept.lower().strip()

        if concept not in self.students[student_id]["concepts_learned"]:
            self.students[student_id]["concepts_learned"].append(
                concept
            )

        self.save_data()

        return f"Concept '{concept}' added."

    def add_problem(self, student_id, problem, score=10):
        """Record a solved practice problem."""

        if student_id not in self.students:
            return "Student not found."

        self.students[student_id]["problems_solved"].append(
            problem
        )

        self.students[student_id]["score"] += score

        self.save_data()

        return "Practice problem recorded."

    def calculate_progress(self, student_id):
        """Calculate student progress percentage."""

        if student_id not in self.students:
            return 0

        student = self.students[student_id]

        concepts = len(student["concepts_learned"])
        problems = len(student["problems_solved"])

        progress = (
            concepts * 10 +
            problems * 10 +
            min(student["score"], 100) * 0.5
        )

        return min(round(progress, 2), 100)

    def get_report(self, student_id):
        """Generate a student progress report."""

        if student_id not in self.students:
            return "Student not found."

        student = self.students[student_id]

        progress = self.calculate_progress(student_id)

        report = []

        report.append("=" * 45)
        report.append("        STUDENT LEARNING REPORT")
        report.append("=" * 45)

        report.append(
            f"\nStudent ID : {student_id}"
        )

        report.append(
            f"Name       : {student['name']}"
        )

        report.append(
            f"Sessions   : {student['sessions']}"
        )

        report.append(
            f"Concepts   : {len(student['concepts_learned'])}"
        )

        report.append(
            f"Problems   : {len(student['problems_solved'])}"
        )

        report.append(
            f"Score      : {student['score']}"
        )

        report.append(
            f"Progress   : {progress}%"
        )

        report.append(
            f"Last Active: {student['last_active']}"
        )

        report.append("\nConcepts Learned:")

        if student["concepts_learned"]:

            for concept in student["concepts_learned"]:
                report.append(f"✓ {concept}")

        else:
            report.append("No concepts learned yet.")

        report.append("\nProblems Solved:")

        if student["problems_solved"]:

            for problem in student["problems_solved"]:
                report.append(f"✓ {problem}")

        else:
            report.append("No problems solved yet.")

        report.append("\n" + "=" * 45)

        return "\n".join(report)


def main():

    tracker = ProgressTracker()

    student_id = "DAS004308"

    print(tracker.create_student(
        student_id,
        "AATHITHYA G"
    ))

    print(tracker.start_session(student_id))

    print(tracker.add_concept(
        student_id,
        "Python Functions"
    ))

    print(tracker.add_concept(
        student_id,
        "Loops"
    ))

    print(tracker.add_problem(
        student_id,
        "Write a function to add two numbers",
        10
    ))

    print("\n")

    print(tracker.get_report(student_id))


if __name__ == "__main__":
    main()