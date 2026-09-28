import re
from collections import Counter


class NLPProcessor:
    def __init__(self):
        self.stop_words = {
            "the", "is", "a", "an", "and", "or",
            "to", "of", "in", "on", "for", "with",
            "this", "that", "are", "was", "were"
        }

    def clean_text(self, text):
        """Clean user input text."""

        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            text
        )

        words = text.split()

        words = [
            word for word in words
            if word not in self.stop_words
        ]

        return words

    def extract_keywords(self, text, top_n=5):
        """Extract important keywords from text."""

        words = self.clean_text(text)

        if not words:
            return []

        frequency = Counter(words)

        return [
            word
            for word, count in frequency.most_common(top_n)
        ]

    def detect_intent(self, text):
        """Detect the user's basic coding-related intent."""

        text = text.lower()

        if any(word in text for word in [
            "explain", "meaning", "what is", "definition"
        ]):
            return "Concept Explanation"

        if any(word in text for word in [
            "error", "bug", "wrong", "not working", "issue"
        ]):
            return "Error Detection"

        if any(word in text for word in [
            "practice", "question", "problem", "exercise"
        ]):
            return "Practice Problem"

        if any(word in text for word in [
            "improve", "optimization", "better", "quality"
        ]):
            return "Code Improvement"

        if any(word in text for word in [
            "progress", "score", "performance"
        ]):
            return "Progress Tracking"

        return "General Coding Help"

    def generate_response(self, text):
        """Generate a basic mentor response."""

        intent = self.detect_intent(text)
        keywords = self.extract_keywords(text)

        responses = {
            "Concept Explanation":
                "I can explain the programming concept step by step.",

            "Error Detection":
                "I can analyze your code and identify possible errors.",

            "Practice Problem":
                "I can generate a programming practice problem for you.",

            "Code Improvement":
                "I can suggest ways to improve your code quality.",

            "Progress Tracking":
                "I can show your learning progress and score.",

            "General Coding Help":
                "I can help you learn Python and solve coding problems."
        }

        return {
            "intent": intent,
            "keywords": keywords,
            "response": responses[intent]
        }


def main():

    nlp = NLPProcessor()

    user_input = (
        "Can you explain Python functions "
        "and give me a practice problem?"
    )

    result = nlp.generate_response(user_input)

    print("=" * 45)
    print("          NLP PROCESSOR TEST")
    print("=" * 45)

    print("\nUser Input:")
    print(user_input)

    print("\nDetected Intent:")
    print(result["intent"])

    print("\nKeywords:")
    print(", ".join(result["keywords"]))

    print("\nAI Mentor Response:")
    print(result["response"])

    print("=" * 45)


if __name__ == "__main__":
    main()