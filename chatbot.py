"""
Educational Chatbot using Hybrid Matching (Rule-based + Semantic Similarity)
COMP1827 - Introduction to Artificial Intelligence
"""

import spacy
import json
import re
from typing import List, Dict, Optional
from datetime import datetime


class EducationalChatbot:
    """Hybrid educational chatbot with precise pattern matching."""

    def __init__(self, qa_file: str = "data/qa_pairs.json"):
        """Initialize chatbot."""
        print("🤖 Initializing Educational Chatbot...")
        print("📚 Loading spaCy model (en_core_web_md)...")
        
        try:
            self.nlp = spacy.load("en_core_web_md")
        except OSError:
            print("❌ Error: spaCy model not found!")
            print("Please run: python -m spacy download en_core_web_md")
            raise
        
        print("📖 Loading knowledge base...")
        self.knowledge_base = self.load_knowledge_base(qa_file)
        self.query_log = []
        self.exact_patterns = self._build_exact_patterns()
        
        print(f"✅ Chatbot initialized!")
        print(f"   - Knowledge base: {len(self.knowledge_base)} Q&A pairs")
        print(f"   - Exact patterns: {len(self.exact_patterns)} rules\n")

    def load_knowledge_base(self, filepath: str) -> List[Dict]:
        """Load Q&A pairs from JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Warning: {filepath} not found")
            return []

    def _build_exact_patterns(self) -> Dict[str, str]:
        """Build PRECISE exact pattern matching rules"""
        return {
            # Greetings (exact matches only)
            r'^(hello|hi|hey)$': 
                "Hello! 👋 I'm here to help you with COMP1827 - Introduction to Artificial Intelligence. What would you like to know?",
            
            r'^(good morning)$': 
                "Good day! 👋 How can I help you with your AI studies today?",
            
            r'^(good afternoon|good evening)$': 
                "Good day! 👋 How can I help you with your AI studies today?",
            
            r'^(how are you|how are you doing|how r u)$': 
                "I'm doing great, thanks for asking! I'm ready to help you with your coursework. What can I assist you with?",
            
            # Farewalls (exact matches only)
            r'^(bye|goodbye|farewell|see you|see ya|later)$':
                "Goodbye! Feel free to come back if you have more questions. Good luck with your studies! 📚",
            
            # Gratitude (exact matches only - won't interfere with questions)
            r'^(thank you|thanks|thx|ty)$': 
                "You're welcome! Happy to help. Is there anything else you'd like to know?",
            
            # Simple acknowledgments (exact matches only)
            r'^(yes|yeah|yep|sure)$': 
                "Great! What would you like to know more about?",
            
            r'^(ok|okay|alright)$': 
                "Great! What would you like to know more about?",
            
            r'^(no|nope|nah)$': 
                "No problem! Feel free to ask if you need anything else.",
            
            r'^(i see|i understand|got it|understood)$': 
                "Excellent! Do you have any other questions about AI or NLP?",
        }

    def _check_exact_match(self, query: str) -> Optional[str]:
        """Check if query matches exact patterns."""
        query_clean = query.lower().strip()
        
        for pattern, answer in self.exact_patterns.items():
            if re.search(pattern, query_clean, re.IGNORECASE):
                return answer
        
        return None

    def _preprocess_query(self, query: str) -> str:
        """Preprocess and expand query with PRECISE mappings."""
        query = query.strip().lower()
        
        # PRECISE expansions for single-word or short queries
        expansions = {
            # NLP & AI
            "nlp": "what is natural language processing",
            "ai": "what is artificial intelligence",
            "ml": "what is machine learning",
            
            # Tools & Libraries
            "python": "what is python programming language",
            "spacy": "what is spacy library",
            "flask": "what is flask web framework",
            "api": "what is an api application programming interface",
            "json": "what is json data format",
            
            # NLP Concepts
            "tokenization": "what is tokenization process",
            "tokenize": "what is tokenization process",
            "token": "what is tokenization process",
            "tokens": "what is tokenization process",
            "embedding": "what are word embeddings vectors",
            "embeddings": "what are word embeddings vectors",
            "vector": "what are word embeddings vectors",
            "similarity": "how does semantic similarity work measure",
            "cosine": "what is cosine similarity formula",
            "lemmatization": "what is lemmatization lemma stemming",
            "pos": "what is part of speech tagging",
            "ner": "what is named entity recognition",
            
            # ITS
            "its": "what is intelligent tutoring system",
            "personalization": "personalized learning adaptive education",
            
            # Advanced
            "chatbot": "how was this chatbot created built",
            "rag": "what is retrieval augmented generation",
            "llm": "what is large language model",
            "bert": "what is bert transformer model",
            "gpt": "what is gpt transformer model",
            "transformer": "what is transformer attention mechanism",
            
            # Ethics
            "ethics": "what are ethical concerns with ai education",
            "bias": "what is bias in ai fairness",
            "privacy": "privacy data protection student information",
            "gdpr": "privacy data protection gdpr regulation",
            "lsepi": "what is lsepi ethical legal social",
            
            # Course
            "deadline": "when is project deadline due date",
            "course": "what is comp1827 course about subject",
            "report": "what should report include requirements",
        }
        
        # Only expand if query is EXACTLY the key (prevents over-expansion)
        if query in expansions:
            return expansions[query]
        
        # For very short queries (1-2 words), check if key is IN query
        if len(query.split()) <= 2:
            for key, expansion in expansions.items():
                if key == query or query == key:
                    return expansion
        
        return query

    def get_response(self, user_query: str, threshold: float = 0.60) -> Dict:
        """Get response using hybrid approach"""
        if not user_query.strip():
            return {
                "answer": "Please ask me a question!",
                "confidence": 0.0,
                "source": "system",
                "method": "validation"
            }
        
        # STEP 1: Check exact patterns FIRST
        exact_answer = self._check_exact_match(user_query)
        if exact_answer:
            self._log_query(user_query, user_query, 1.0, "exact_match")
            return {
                "answer": exact_answer,
                "confidence": 1.0,
                "source": "exact_match",
                "method": "rule-based"
            }
        
        # STEP 2: Preprocess query (only for short queries)
        processed_query = self._preprocess_query(user_query)
        
        # STEP 3: Semantic similarity
        query_doc = self.nlp(processed_query)
        
        best_match = None
        best_similarity = 0.0
        
        for qa_pair in self.knowledge_base:
            question = qa_pair.get("question", "")
            question_doc = self.nlp(question.lower())
            similarity = query_doc.similarity(question_doc)
            
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = qa_pair
        
        self._log_query(user_query, processed_query, best_similarity, "semantic")
        
        if best_match and best_similarity >= threshold:
            return {
                "answer": best_match.get("answer", "I don't have an answer."),
                "confidence": round(best_similarity, 2),
                "source": best_match.get("topic", "general"),
                "method": "semantic_similarity",
                "matched_question": best_match.get("question", "")
            }
        else:
            suggestions = self._get_topic_suggestions()
            return {
                "answer": f"I'm not confident about that ({round(best_similarity * 100)}%). Try asking about: {suggestions}",
                "confidence": round(best_similarity, 2),
                "source": "fallback",
                "method": "semantic_similarity"
            }

    def _get_topic_suggestions(self) -> str:
        """Get topic suggestions from knowledge base."""
        topics = {qa.get("topic") for qa in self.knowledge_base if qa.get("topic") and qa.get("topic") != "Casual"}
        return ", ".join(sorted(topics)[:6])

    def _log_query(self, original: str, processed: str, confidence: float, method: str):
        """Log query for analysis."""
        self.query_log.append({
            "original": original,
            "processed": processed,
            "confidence": confidence,
            "method": method,
            "timestamp": datetime.now().isoformat()
        })

    def batch_evaluate(self, test_queries: List[str]) -> List[Dict]:
        """Evaluate chatbot on multiple queries."""
        results = []
        print(f"\n📊 Evaluating {len(test_queries)} queries...\n")
        
        for i, query in enumerate(test_queries, 1):
            response = self.get_response(query)
            results.append({"query": query, "response": response})
            
            status = "✓" if response["confidence"] >= 0.60 else "✗"
            method = response.get("method", "unknown")
            print(f"{status} [{method:15}] {query:20} → {response['confidence']}")
        
        confidences = [r["response"]["confidence"] for r in results]
        avg = sum(confidences) / len(confidences)
        above = sum(1 for c in confidences if c >= 0.60)
        
        print(f"\n📈 Avg confidence: {avg:.2f} | Success: {above}/{len(results)} ({above/len(results)*100:.1f}%)")
        return results

    def get_statistics(self) -> Dict:
        """Get chatbot usage statistics."""
        if not self.query_log:
            return {"queries": 0}
        
        confidences = [q["confidence"] for q in self.query_log]
        methods = [q["method"] for q in self.query_log]
        
        return {
            "total_queries": len(self.query_log),
            "avg_confidence": round(sum(confidences) / len(confidences), 2),
            "exact_matches": methods.count("exact_match"),
            "semantic_matches": methods.count("semantic"),
            "above_threshold": sum(1 for c in confidences if c >= 0.60)
        }

    def export_query_log(self, filepath: str = "logs/query_log.json"):
        """Export query log to JSON file."""
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.query_log, f, indent=2)
        print(f"📝 Query log exported to: {filepath}")


# Test harness for standalone execution
if __name__ == "__main__":
    print("="*60)
    print("EDUCATIONAL CHATBOT - TEST MODE")
    print("="*60)
    
    chatbot = EducationalChatbot()
    
    # Quick test queries
    test_queries = [
        "hello", "bye", 
        "what is NLP?", "explain tokenization",
        "nlp", "python", "deadline"
    ]
    
    print("\n🧪 Quick Test:\n")
    for query in test_queries:
        response = chatbot.get_response(query)
        print(f"Q: {query}")
        print(f"A: {response['answer'][:60]}...")
        print(f"Confidence: {response['confidence']}\n")