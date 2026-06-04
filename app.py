"""
Flask Web Application for Educational Chatbot
COMP1827 - Introduction to Artificial Intelligence
"""

from flask import Flask, render_template, request, jsonify
from chatbot import EducationalChatbot

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print("\n" + "="*60)
print("STARTING EDUCATIONAL CHATBOT WEB APPLICATION")
print("="*60 + "\n")

chatbot = EducationalChatbot()

print("="*60)
print("✅ Flask server ready!")
print("🌐 Open: http://127.0.0.1:5000")
print("="*60 + "\n")


@app.route('/')
def home():
    """Render main chat interface."""
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    """Handle user questions."""
    try:
        data = request.get_json()
        user_query = data.get('question', '').strip()
        
        if not user_query:
            return jsonify({
                "answer": "Please ask me a question!",
                "confidence": 0.0,
                "source": "error"
            })
        
        response = chatbot.get_response(user_query)
        return jsonify(response)
    
    except Exception as e:
        print(f"❌ Error in /ask endpoint: {e}")
        return jsonify({
            "answer": "Sorry, I encountered an error. Please try again.",
            "confidence": 0.0,
            "source": "error"
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    stats = chatbot.get_statistics()
    return jsonify({
        "status": "running",
        "model": "en_core_web_md",
        "statistics": stats
    })


@app.route('/stats')
def stats():
    """Get chatbot statistics."""
    return jsonify(chatbot.get_statistics())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)