"""
FAQ Chatbot NLP Matching Engine
===============================
Preprocesses college FAQs and uses TF-IDF + Cosine Similarity for query resolution.
Author: Jenicadeva Christa S
"""

import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Import local FAQ dataset
from faqs import FAQ_DATA

# Auto-download required NLTK resource packages quietly on first import
try:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)
except Exception as e:
    print(f"Warning: NLTK downloading error: {e}. If offline, ensure resources are in nltk_data folder.")

class FAQChatbot:
    def __init__(self):
        """
        Initializes chatbot, pre-processes the FAQ dataset, and trains the TF-IDF vectorizer.
        """
        self.faqs = FAQ_DATA
        self.fallback_message = (
            "I'm sorry, I couldn't find a matching answer for that question. "
            "Could you please rephrase or try asking about admission deadlines, fees, hostel rooms, or course lists?"
        )
        self.vectorizer = TfidfVectorizer()
        
        # Preprocess all FAQ questions on initialization
        self.preprocessed_questions = [self.preprocess(faq["question"]) for faq in self.faqs]
        
        # Fit vectorizer and calculate TF-IDF matrix of questions
        self.tfidf_matrix = self.vectorizer.fit_transform(self.preprocessed_questions)

    def preprocess(self, text):
        """
        Tokenizes, cleans stopwords, punctuation, and lemmatizes the input text.
        """
        if not text:
            return ""
        
        # Lowercase
        text = text.lower()
        
        # Tokenization
        tokens = word_tokenize(text)
        
        # Stopwords & punctuation filters
        stop_words = set(stopwords.words('english'))
        punctuation = set(string.punctuation)
        
        cleaned_tokens = [
            token for token in tokens
            if token not in stop_words and token not in punctuation
        ]
        
        # Lemmatization (nouns & verbs)
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in cleaned_tokens]
        
        return " ".join(lemmatized_tokens)

    def get_response(self, user_input):
        """
        Computes TF-IDF vector similarity and returns the best matching FAQ response.
        Returns fallback if similarity is below 0.2.
        """
        if not user_input or not user_input.strip():
            return "Please type a question, and I'll do my best to answer it!"

        # Clean user query
        preprocessed_query = self.preprocess(user_input)
        
        # Edge case: query contains only stopwords/punctuation
        if not preprocessed_query.strip():
            return self.fallback_message

        try:
            # Transform user query using pre-fitted vectorizer
            query_vector = self.vectorizer.transform([preprocessed_query])
            
            # Compute cosine similarities against all preprocessed FAQ questions
            similarities = cosine_similarity(query_vector, self.tfidf_matrix)[0]
            
            # Identify index of the highest similarity score
            best_match_idx = np.argmax(similarities)
            best_score = similarities[best_match_idx]
            
            # Return result or fallback based on 0.2 threshold
            if best_score >= 0.2:
                return self.faqs[best_match_idx]["answer"]
            else:
                return self.fallback_message
                
        except Exception as e:
            # Fallback on any mathematical or vector parsing exceptions
            print(f"Error during response matching: {e}")
            return self.fallback_message
