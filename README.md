# Intelligent Tutoring System - Educational Chatbot

## Quick Start
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
python chatbot.py
```

## Files
- `chatbot.py` - Main chatbot implementation
- `app.py` - Flask web server
- `test_chatbot.py` - Test suite (108 tests)
- `data/qa_pairs.json` - 58 Q&A pairs
- `logs/` - Test results (99.1% accuracy)

## Results
- Accuracy: 99.1% (107/108 tests)
- Average Confidence: 81%
- Technology: spaCy NLP with 300D floret embeddings

## Author
Francisco Navarro Gil
University of Greenwich
