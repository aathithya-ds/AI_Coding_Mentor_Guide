import ast


class CodeAnalyzer:
    def __init__(self):
        self.supported_languages = ["Python"]

    def analyze_code(self, code):
        """Analyze Python code using AST."""

        result = {
            "syntax_valid": False,
            "errors": [],
            "functions": 0,
            "classes": 0,
            "loops": 0,
            "conditions": 0,
            "imports": 0,
            "lines": len(code.splitlines()),
            "quality_score": 0
        }

        # Empty code check
        if not code.strip():
            result["errors"].append("Code is empty.")
            return result

        # Syntax analysis
        try:
            tree = ast.parse(code)
            result["syntax_valid"] = True
        except SyntaxError as error:
            result["errors"].append(
                f"Syntax Error: {error.msg} at line {error.lineno}"
            )
            return result

        # Analyze Python structures
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                result["functions"] += 1

            elif isinstance(node, ast.ClassDef):
                result["classes"] += 1

            elif isinstance(node, (ast.For, ast.While)):
                result["loops"] += 1

            elif isinstance(node, ast.If):
                result["conditions"] += 1

            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                result["imports"] += 1

        # Calculate code quality score
        score = 100

        if result["lines"] > 30:
            score -= 10

        if result["lines"] > 60:
            score -= 10

        if result["functions"] == 0 and result["lines"] > 15:
            score -= 10

        if "#" not in code and result["lines"] > 5:
            score -= 5

        if result["syntax_valid"]:
            score += 0

        result["quality_score"] = max(0, min(score, 100))

        return result

    def generate_report(self, code):
        """Generate a readable code analysis report."""

        result = self.analyze_code(code)

        report = []

        report.append("=" * 45)
        report.append("          AI CODE ANALYSIS REPORT")
        report.append("=" * 45)

        report.append(
            f"\nSyntax Status : "
            f"{'VALID' if result['syntax_valid'] else 'INVALID'}"
        )

        report.append(
            f"Lines of Code : {result['lines']}"
        )

        report.append(
            f"Functions     : {result['functions']}"
        )

        report.append(
            f"Classes       : {result['classes']}"
        )

        report.append(
            f"Loops         : {result['loops']}"
        )

        report.append(
            f"Conditions    : {result['conditions']}"
        )

        report.append(
            f"Imports       : {result['imports']}"
        )

        report.append(
            f"Quality Score : {result['quality_score']}/100"
        )

        if result["errors"]:
            report.append("\nErrors:")

            for error in result["errors"]:
                report.append(f"❌ {error}")

        else:
            report.append("\nErrors:")
            report.append("✅ No syntax errors detected.")

        report.append("\nRecommendations:")

        if result["functions"] == 0 and result["lines"] > 10:
            report.append(
                "💡 Consider dividing the code into reusable functions."
            )

        if result["classes"] == 0 and result["lines"] > 30:
            report.append(
                "💡 Consider using classes for larger applications."
            )

        if "#" not in code:
            report.append(
                "💡 Add comments to explain important logic."
            )

        if not result["errors"]:
            report.append(
                "✅ Code structure looks good."
            )

        report.append("\n" + "=" * 45)

        return "\n".join(report)


def main():

    analyzer = CodeAnalyzer()

    sample_code = """
def add(a, b):
    return a + b

for i in range(5):
    print(i)
"""

    print(analyzer.generate_report(sample_code))


if __name__ == "__main__":
    main()