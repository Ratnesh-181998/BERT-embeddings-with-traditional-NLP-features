import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download necessary NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        # Custom stopwords can be added here if needed
        
    def clean_text(self, text):
        """
        Basic cleaning: lowercase, remove special chars.
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text

    def get_pos_tags(self, text):
        """
        Returns a simple count of Nouns and Verbs as features.
        In a full implementation, this would be a One-Hot encoded vector of all tags.
        """
        tokens = word_tokenize(text)
        tags = nltk.pos_tag(tokens)
        
        # Simple feature: count of Nouns (NN, NNS...) and Verbs (VB, VBD...)
        noun_count = sum(1 for word, tag in tags if tag.startswith('NN'))
        verb_count = sum(1 for word, tag in tags if tag.startswith('VB'))
        adj_count = sum(1 for word, tag in tags if tag.startswith('JJ'))
        
        return [noun_count, verb_count, adj_count]

    def preprocess_batch(self, texts):
        """
        Returns cleaned texts and POS feature vectors.
        """
        cleaned_texts = [self.clean_text(t) for t in texts]
        pos_features = [self.get_pos_tags(t) for t in texts]
        return cleaned_texts, np.array(pos_features)
