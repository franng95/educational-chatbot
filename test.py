"""
Comprehensive Test and Evaluation 
COMP1827 - Introduction to Artificial Intelligence
"""

from chatbot import EducationalChatbot
import json
import os
from datetime import datetime
from typing import List, Dict, Tuple


class ChatbotTester:
    """Comprehensive chatbot testing framework."""
    
    def __init__(self):
        """Initialize tester."""
        self.chatbot = EducationalChatbot()
        self.test_results = []
        self.validation_errors = []
        
    def run_all_tests(self):
        """Run complete test suite."""
        print("="*80)
        print("COMPREHENSIVE CHATBOT TESTING SUITE - COMP1827")
        print("="*80)
        print(f"Test started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Run all test categories
        self.test_greetings_farewells()
        self.test_nlp_concepts()
        self.test_its_concepts()
        self.test_tools_programming()
        self.test_course_information()
        self.test_ethics_lsepi()
        self.test_advanced_topics()
        self.test_chatbot_mechanics()
        self.test_abbreviations()
        self.test_edge_cases()
        
        # Generate comprehensive report
        self.generate_report()
        self.export_results()
        
        print("\n" + "="*80)
        print("TESTING COMPLETE")
        print("="*80)
    
    def test_query(self, query: str, expected_topic: str, 
                   min_confidence: float, test_category: str) -> Dict:
        """Test a single query with validation."""
        response = self.chatbot.get_response(query)
        
        passed = response["confidence"] >= min_confidence
        
        result = {
            "category": test_category,
            "query": query,
            "expected_topic": expected_topic,
            "min_confidence": min_confidence,
            "actual_confidence": response["confidence"],
            "answer": response["answer"],
            "source": response.get("source", "unknown"),
            "method": response.get("method", "unknown"),
            "passed": passed,
            "timestamp": datetime.now().isoformat()
        }
        
        self.test_results.append(result)
        
        # Validation
        if not passed:
            self.validation_errors.append({
                "query": query,
                "expected": f"≥{min_confidence}",
                "actual": response["confidence"],
                "category": test_category
            })
        
        return result
    
    def test_greetings_farewells(self):
        """Test greeting and farewell responses."""
        print("\n🎯 Testing: GREETINGS & FAREWELLS")
        print("-" * 80)
        
        tests = [
            ("hello", "exact_match", 1.0),
            ("hi", "exact_match", 1.0),
            ("hey", "exact_match", 1.0),
            ("good morning", "exact_match", 1.0),
            ("good afternoon", "exact_match", 1.0),
            ("how are you", "exact_match", 1.0),
            ("bye", "exact_match", 1.0),
            ("goodbye", "exact_match", 1.0),
            ("see you", "exact_match", 1.0),
            ("thanks", "exact_match", 1.0),
            ("thank you", "exact_match", 1.0),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Greetings")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_nlp_concepts(self):
        """Test NLP concept questions."""
        print("\n🎯 Testing: NLP CONCEPTS")
        print("-" * 80)
        
        tests = [
            ("what is NLP?", "NLP Basics", 0.85),
            ("what is natural language processing?", "NLP Basics", 0.85),
            ("explain NLP", "NLP Basics", 0.55),
            ("what is tokenization?", "NLP Concepts", 0.85),
            ("explain tokenization", "NLP Concepts", 0.85),
            ("how does tokenization work?", "NLP Concepts", 0.85),
            ("what are word embeddings?", "NLP Concepts", 0.80),
            ("explain word embeddings", "NLP Concepts", 0.65),
            ("what are vectors?", "NLP Concepts", 0.75),
            ("how does semantic similarity work?", "NLP Concepts", 0.85),
            ("explain semantic similarity", "NLP Concepts", 0.85),
            ("what is semantic similarity?", "NLP Concepts", 0.85),
            ("what is cosine similarity?", "NLP Concepts", 0.85),
            ("explain cosine similarity", "NLP Concepts", 0.80),
            ("what is lemmatization?", "NLP Concepts", 0.80),
            ("what is POS tagging?", "NLP Concepts", 0.75),
            ("what is named entity recognition?", "NLP Concepts", 0.85),
            ("explain NER", "NLP Concepts", 0.60),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "NLP")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_its_concepts(self):
        """Test Intelligent Tutoring Systems questions."""
        print("\n🎯 Testing: INTELLIGENT TUTORING SYSTEMS")
        print("-" * 80)
        
        tests = [
            ("what is an intelligent tutoring system?", "ITS", 0.85),
            ("what is ITS?", "ITS", 0.85),
            ("explain intelligent tutoring systems", "ITS", 0.80),
            ("components of ITS", "ITS", 0.85),
            ("what are ITS components?", "ITS", 0.80),
            ("personalized learning", "ITS", 0.70),
            ("what is personalized learning?", "ITS", 0.75),
            ("adaptive education", "ITS", 0.70),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "ITS")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_tools_programming(self):
        """Test tools and programming questions."""
        print("\n🎯 Testing: TOOLS & PROGRAMMING")
        print("-" * 80)
        
        tests = [
            ("what is spaCy?", "Tools", 0.70),
            ("tell me about spaCy", "Tools", 0.70),
            ("explain spaCy", "Tools", 0.60),
            ("what is Flask?", "Tools", 0.75),
            ("tell me about Flask", "Tools", 0.75),
            ("what is Python?", "Programming", 0.80),
            ("what is python programming?", "Programming", 0.80),
            ("what is an API?", "Programming", 0.80),
            ("explain API", "Programming", 0.65),
            ("what is JSON?", "Programming", 0.70),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Tools")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_course_information(self):
        """Test course-specific questions."""
        print("\n🎯 Testing: COURSE INFORMATION")
        print("-" * 80)
        
        tests = [
            ("when is the deadline?", "Course Info", 0.80),
            ("what is the deadline?", "Course Info", 0.80),
            ("when is the presentation due?", "Course Info", 0.75),
            ("when is the report due?", "Course Info", 0.75),
            ("what is COMP1827?", "Course Info", 0.80),
            ("what is COMP1827 about?", "Course Info", 0.80),
            ("tell me about the course", "Course Info", 0.75),
            ("what should the report include?", "Course Info", 0.85),
            ("report requirements", "Course Info", 0.75),
            ("how many words should the report be?", "Course Info", 0.80),
            ("harvard referencing", "Course Info", 0.60),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Course")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_ethics_lsepi(self):
        """Test ethics and LSEPI questions."""
        print("\n🎯 Testing: ETHICS & LSEPI")
        print("-" * 80)
        
        tests = [
            ("what is LSEPI?", "Ethics", 0.80),
            ("explain LSEPI", "Ethics", 0.80),
            ("what is bias in AI?", "Ethics", 0.80),
            ("explain bias in AI", "Ethics", 0.75),
            ("what are ethical concerns?", "Ethics", 0.80),
            ("ethical concerns with AI", "Ethics", 0.80),
            ("AI ethics", "Ethics", 0.75),
            ("what is privacy in AI?", "Ethics", 0.80),
            ("privacy issues", "Ethics", 0.85),
            ("data protection", "Ethics", 0.60),
            ("what is transparency?", "Ethics", 0.75),
            ("accountability in AI", "Ethics", 0.75),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Ethics")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_advanced_topics(self):
        """Test advanced AI topics."""
        print("\n🎯 Testing: ADVANCED TOPICS")
        print("-" * 80)
        
        tests = [
            ("what is RAG?", "Advanced NLP", 0.80),
            ("explain RAG", "Advanced NLP", 0.60),
            ("retrieval augmented generation", "Advanced NLP", 0.75),
            ("what is an LLM?", "Advanced NLP", 0.70),
            ("what are large language models?", "Advanced NLP", 0.70),
            ("what is GPT?", "Advanced NLP", 0.70),
            ("what is BERT?", "Advanced NLP", 0.80),
            ("what are transformers?", "Advanced NLP", 0.85),
            ("explain transformers", "Advanced NLP", 0.70),
            ("what is machine learning?", "AI Basics", 0.80),
            ("what is artificial intelligence?", "AI Basics", 0.85),
            ("what is deep learning?", "AI Basics", 0.80),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Advanced")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_chatbot_mechanics(self):
        """Test chatbot self-awareness questions."""
        print("\n🎯 Testing: CHATBOT MECHANICS")
        print("-" * 80)
        
        tests = [
            ("how do you work?", "Chatbot Info", 0.80),
            ("how does this chatbot work?", "Chatbot Info", 0.85),
            ("explain how you work", "Chatbot Info", 0.80),
            ("what are your limitations?", "Chatbot Info", 0.80),
            ("what are the limitations?", "Chatbot Info", 0.80),
            ("how was this chatbot created?", "Chatbot Info", 0.80),
            ("who created you?", "Chatbot Info", 0.70),
            ("are you human?", "Casual", 0.70),
            ("what is your name?", "Casual", 0.70),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Mechanics")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_abbreviations(self):
        """Test single-word abbreviation expansion."""
        print("\n🎯 Testing: ABBREVIATION EXPANSION")
        print("-" * 80)
        
        tests = [
            ("nlp", "NLP Basics", 0.85),
            ("ai", "AI Basics", 0.80),
            ("ml", "AI Basics", 0.75),
            ("its", "ITS", 0.85),
            ("rag", "Advanced NLP", 0.85),
            ("llm", "Advanced NLP", 0.75),
            ("api", "Programming", 0.90),
            ("json", "Programming", 0.75),
            ("python", "Programming", 0.80),
            ("flask", "Tools", 0.75),
            ("spacy", "Tools", 0.70),
        ]
        
        for query, expected_topic, min_conf in tests:
            result = self.test_query(query, expected_topic, min_conf, "Abbreviations")
            status = "✓" if result["passed"] else "✗"
            print(f"  {status} '{query}' → {result['actual_confidence']} (expected ≥{min_conf})")
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        print("\n🎯 Testing: EDGE CASES")
        print("-" * 80)
        
        # Empty input
        result = self.chatbot.get_response("")
        status = "✓" if result["confidence"] == 0.0 else "✗"
        print(f"  {status} Empty input → {result['confidence']} (expected 0.0)")
        self.test_results.append({
            "category": "Edge Cases",
            "query": "[EMPTY]",
            "expected_topic": "validation",
            "min_confidence": 0.0,
            "actual_confidence": result["confidence"],
            "passed": result["confidence"] == 0.0,
            "method": result.get("method", "unknown")
        })
        
        # Gibberish
        gibberish_tests = [
            "asdfghjkl",
            "qwertyuiop",
            "zxcvbnm",
            "!@#$%^&*()",
            "12345678",
        ]
        
        for gibberish in gibberish_tests:
            result = self.chatbot.get_response(gibberish)
            status = "✓" if result["confidence"] < 0.60 else "✗"
            print(f"  {status} '{gibberish}' → {result['confidence']} (expected <0.60)")
            self.test_results.append({
                "category": "Edge Cases",
                "query": gibberish,
                "expected_topic": "fallback",
                "min_confidence": 0.0,
                "actual_confidence": result["confidence"],
                "passed": result["confidence"] < 0.60,
                "method": result.get("method", "unknown")
            })
        
        # Whitespace only
        whitespace_tests = ["   ", "\t", "\n"]
        for ws in whitespace_tests:
            result = self.chatbot.get_response(ws)
            status = "✓" if result["confidence"] == 0.0 else "✗"
            print(f"  {status} Whitespace → {result['confidence']} (expected 0.0)")
    
    def generate_report(self):
        """Generate comprehensive test report."""
        print("\n" + "="*80)
        print("COMPREHENSIVE TEST REPORT")
        print("="*80)
        
        # Overall statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r["passed"])
        failed_tests = total_tests - passed_tests
        pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"  Total Tests: {total_tests}")
        print(f"  Passed: {passed_tests} ({pass_rate:.1f}%)")
        print(f"  Failed: {failed_tests} ({100-pass_rate:.1f}%)")
        
        # Confidence statistics
        confidences = [r["actual_confidence"] for r in self.test_results]
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0
        max_confidence = max(confidences) if confidences else 0
        min_confidence = min(confidences) if confidences else 0
        
        print(f"\n📈 CONFIDENCE STATISTICS:")
        print(f"  Average: {avg_confidence:.2f}")
        print(f"  Maximum: {max_confidence:.2f}")
        print(f"  Minimum: {min_confidence:.2f}")
        
        # Confidence distribution
        high_conf = sum(1 for c in confidences if c >= 0.80)
        medium_conf = sum(1 for c in confidences if 0.60 <= c < 0.80)
        low_conf = sum(1 for c in confidences if c < 0.60)
        
        print(f"\n📊 CONFIDENCE DISTRIBUTION:")
        print(f"  🟢 High (≥80%): {high_conf} ({high_conf/total_tests*100:.1f}%)")
        print(f"  🟡 Medium (60-79%): {medium_conf} ({medium_conf/total_tests*100:.1f}%)")
        print(f"  🔴 Low (<60%): {low_conf} ({low_conf/total_tests*100:.1f}%)")
        
        # Category breakdown
        print(f"\n📋 RESULTS BY CATEGORY:")
        categories = {}
        for result in self.test_results:
            cat = result["category"]
            if cat not in categories:
                categories[cat] = {"total": 0, "passed": 0}
            categories[cat]["total"] += 1
            if result["passed"]:
                categories[cat]["passed"] += 1
        
        for cat, stats in sorted(categories.items()):
            pass_rate = (stats["passed"] / stats["total"] * 100) if stats["total"] > 0 else 0
            status = "✓" if pass_rate >= 90 else "⚠" if pass_rate >= 70 else "✗"
            print(f"  {status} {cat:20} {stats['passed']}/{stats['total']} ({pass_rate:.1f}%)")
        
        # Failed tests
        if self.validation_errors:
            print(f"\n❌ FAILED TESTS ({len(self.validation_errors)}):")
            for error in self.validation_errors[:10]:  # Show first 10
                print(f"  • '{error['query']}' [{error['category']}]")
                print(f"    Expected: {error['expected']}, Got: {error['actual']}")
        else:
            print(f"\n✅ ALL TESTS PASSED!")
        
        # Method breakdown
        print(f"\n🔍 MATCHING METHOD BREAKDOWN:")
        methods = {}
        for result in self.test_results:
            method = result.get("method", "unknown")
            methods[method] = methods.get(method, 0) + 1
        
        for method, count in sorted(methods.items()):
            percentage = (count / total_tests * 100) if total_tests > 0 else 0
            print(f"  {method:20} {count:3} ({percentage:.1f}%)")
        
        # Quality assessment
        print(f"\n⭐ QUALITY ASSESSMENT:")
        if pass_rate >= 95:
            print("  🏆 EXCELLENT - Production ready!")
        elif pass_rate >= 90:
            print("  ✅ VERY GOOD - Minor improvements needed")
        elif pass_rate >= 80:
            print("  👍 GOOD - Some improvements recommended")
        elif pass_rate >= 70:
            print("  ⚠️  ACCEPTABLE - Significant improvements needed")
        else:
            print("  ❌ NEEDS WORK - Major issues to address")
    
    def export_results(self):
        """Export results to files."""
        os.makedirs('logs', exist_ok=True)
        
        # Export detailed results
        with open('logs/comprehensive_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(self.test_results, f, indent=2)
        print(f"\n📄 Detailed results: logs/comprehensive_test_results.json")
        
        # Export validation errors
        if self.validation_errors:
            with open('logs/validation_errors.json', 'w', encoding='utf-8') as f:
                json.dump(self.validation_errors, f, indent=2)
            print(f"📄 Validation errors: logs/validation_errors.json")
        
        # Export summary
        summary = {
            "test_date": datetime.now().isoformat(),
            "total_tests": len(self.test_results),
            "passed": sum(1 for r in self.test_results if r["passed"]),
            "failed": sum(1 for r in self.test_results if not r["passed"]),
            "pass_rate": (sum(1 for r in self.test_results if r["passed"]) / len(self.test_results) * 100) if self.test_results else 0,
            "avg_confidence": sum(r["actual_confidence"] for r in self.test_results) / len(self.test_results) if self.test_results else 0,
            "categories": {}
        }
        
        # Category summary
        for result in self.test_results:
            cat = result["category"]
            if cat not in summary["categories"]:
                summary["categories"][cat] = {"total": 0, "passed": 0}
            summary["categories"][cat]["total"] += 1
            if result["passed"]:
                summary["categories"][cat]["passed"] += 1
        
        with open('logs/test_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        print(f"📄 Test summary: logs/test_summary.json")
        
        # Export chatbot query log
        self.chatbot.export_query_log()


def main():
    """Main test execution."""
    tester = ChatbotTester()
    tester.run_all_tests()


if __name__ == "__main__":
    main()