# Intelligent Tutoring System - Educational Chatbot

An educational chatbot built in Python to answer student questions from a curated knowledge base. The project combines spaCy NLP, a Flask web server, structured Q&A data, and an automated test suite to evaluate answer accuracy and confidence.

## Overview

The chatbot is designed as a small intelligent tutoring system. It matches student questions against stored educational Q&A pairs, returns the most relevant answer, and reports confidence scores so the system can be evaluated and improved.

## Features

- Natural-language question matching using spaCy
- 58 curated Q&A pairs stored in JSON
- Flask web app entry point for browser-based interaction
- Command-line chatbot entry point for local testing
- Automated test suite with 108 test cases
- Logged evaluation results for accuracy and confidence
- Clear separation between chatbot logic, web app, data, and tests

## Results

| Metric | Result |
| --- | --- |
| Accuracy | 99.1% |
| Passed tests | 107 / 108 |
| Average confidence | 81% |
| NLP model | spaCy `en_core_web_md` with 300D floret embeddings |
| Dataset | 58 Q&A pairs |

## Tech Stack

- Python
- spaCy NLP
- Flask
- JSON data storage
- Automated testing with Python test files

## Project Structure

```text
educational-chatbot/
├── chatbot.py          # Main chatbot implementation
├── app.py              # Flask web server
├── test.py             # Automated test suite
├── requirements.txt    # Python dependencies
├── templates/          # Flask HTML templates
├── data/
│   └── qa_pairs.json   # Curated educational Q&A data
└── logs/               # Evaluation logs and test results
```

## Quick Start

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
python chatbot.py
```

## Run the Web App

```bash
python app.py
```

Then open the local Flask URL shown in the terminal.

## Run Tests

```bash
python test.py
```

## What I Learned

- Building a question-answering workflow with NLP similarity matching
- Structuring chatbot knowledge in a maintainable JSON format
- Evaluating an AI-style project with repeatable test cases
- Using confidence scores to understand answer quality
- Connecting Python chatbot logic to a Flask web interface

## Future Improvements

- Add a richer frontend chat interface
- Store conversation history for learning analytics
- Add fallback responses for low-confidence questions
- Expand the Q&A dataset by topic and difficulty
- Deploy the Flask app online for demo access

## Author

Francisco Navarro Gil  
University of Greenwich