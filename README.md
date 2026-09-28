# 🤖 AI Coding Mentor Guide

### AI-Powered Personalized Coding Learning Assistant

An intelligent coding mentor application designed to help students learn programming, understand code, detect errors, practice coding problems, and track their learning progress.

This project was developed as part of the **Data Alcott Systems AI & Data Science Internship**.

---

## 🚀 Project Overview

The **AI Coding Mentor Guide** is an AI-assisted learning platform that provides personalized programming guidance to students.

The system combines:

- Python
- Natural Language Processing
- Machine Learning
- AST-based Code Analysis
- Flask
- JSON-based Data Storage
- Interactive Web Interface

The application acts as a virtual coding mentor that helps students understand programming concepts and improve their coding skills.

---

## ✨ Key Features

### 🧑‍💻 AI Coding Mentor

Provides an interactive interface where students can enter Python code and receive coding guidance.

### 🔍 Code Analysis

Analyzes Python source code and provides information such as:

- Syntax status
- Lines of code
- Functions
- Classes
- Loops
- Conditions
- Imports
- Code quality score

### 💡 Code Explanation

Identifies important programming structures and explains the code in a simple way.

### 🚨 Error Detection

Detects common Python coding problems and provides useful suggestions.

### 📚 Concept Learning

Provides explanations and examples for programming concepts such as:

- Variables
- Functions
- Loops
- Lists
- Dictionaries
- Classes
- Exception Handling
- Machine Learning
- NLP

### 🧩 Practice Problems

Generates programming practice questions based on concepts and difficulty levels.

### 🧠 NLP Processing

Processes student questions and identifies programming-related intents and keywords.

### 📊 Learning Progress

Tracks:

- Learning sessions
- Concepts learned
- Problems solved
- Student score
- Overall progress

### 💻 Interactive Web Interface

The project includes a Flask-based web interface with dedicated pages for:

- Home
- AI Mentor
- Concepts
- Progress

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| NLTK | Natural Language Processing |
| Pandas | Data processing |
| Scikit-learn | Machine Learning |
| Python AST | Code analysis |
| HTML5 | Web structure |
| CSS3 | User interface design |
| JavaScript | Interactive functionality |
| JSON | Lightweight data storage |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     Student/User    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Flask Web UI      │
                    │ HTML + CSS + JS     │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌────────────┐    ┌────────────┐    ┌────────────┐
      │ AI Mentor  │    │ NLP Engine │    │ Code       │
      │            │    │            │    │ Analyzer   │
      └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Progress Tracker    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ JSON Data Storage   │
                    └─────────────────────┘
