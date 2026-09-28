from flask import Flask, render_template, request, jsonify

from mentor import AICodingMentor
from code_analyzer import CodeAnalyzer
from nlp_processor import NLPProcessor
from progress_tracker import ProgressTracker


app = Flask(__name__)

mentor = AICodingMentor()
analyzer = CodeAnalyzer()
nlp = NLPProcessor()
tracker = ProgressTracker()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/mentor")
def mentor_page():
    return render_template("mentor.html")


@app.route("/concepts")
def concepts_page():
    return render_template("concepts.html")


@app.route("/progress")
def progress_page():
    return render_template("progress.html")


@app.route("/api/explain", methods=["POST"])
def explain_code():

    data = request.get_json()

    code = data.get("code", "")

    explanation = mentor.explain_code(code)

    analysis = analyzer.analyze_code(code)

    return jsonify({
        "explanation": explanation,
        "analysis": analysis
    })


@app.route("/api/analyze", methods=["POST"])
def analyze_code():

    data = request.get_json()

    code = data.get("code", "")

    result = analyzer.generate_report(code)

    return jsonify({
        "report": result
    })


@app.route("/api/concept", methods=["POST"])
def learn_concept():

    data = request.get_json()

    concept = data.get("concept", "")

    result = mentor.learn_concept(concept)

    return jsonify({
        "result": result
    })


@app.route("/api/nlp", methods=["POST"])
def process_nlp():

    data = request.get_json()

    text = data.get("text", "")

    result = nlp.generate_response(text)

    return jsonify(result)


@app.route("/api/practice", methods=["POST"])
def practice_problem():

    data = request.get_json()

    concept = data.get(
        "concept",
        "Python"
    )

    difficulty = data.get(
        "difficulty",
        "Beginner"
    )

    problem = mentor.get_practice_problem(
        concept,
        difficulty
    )

    return jsonify({
        "problem": problem
    })


@app.route("/api/progress", methods=["POST"])
def progress():

    data = request.get_json()

    student_id = data.get(
        "student_id",
        "DAS004308"
    )

    name = data.get(
        "name",
        "AATHITHYA G"
    )

    if student_id not in tracker.students:
        tracker.create_student(
            student_id,
            name
        )

    return jsonify({
        "report": tracker.get_report(student_id)
    })


@app.route("/api/mentor-session", methods=["POST"])
def mentor_session():

    data = request.get_json()

    student_id = data.get(
        "student_id",
        "DAS004308"
    )

    if student_id not in tracker.students:
        tracker.create_student(
            student_id,
            "AATHITHYA G"
        )

    tracker.start_session(student_id)

    return jsonify({
        "message": "Mentor session started successfully.",
        "student_id": student_id
    })


@app.route("/api/health")
def health():

    return jsonify({
        "status": "online",
        "application": "AI Coding Mentor Guide",
        "domain": "AI & Data Science"
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )