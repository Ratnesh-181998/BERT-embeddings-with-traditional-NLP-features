import torch
from transformers import BertTokenizer, BertModel
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os
try:
    from .preprocessing import TextPreprocessor
except ImportError:
    from preprocessing import TextPreprocessor

class JaguarClassifier:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.tfidf = TfidfVectorizer(max_features=100) # Keep small for demo
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        
        # Load BERT (using a smaller model for speed if preferred, but notes said BERT)
        print("Loading BERT model... (this may take a moment)")
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.bert_model = BertModel.from_pretrained('bert-base-uncased')
        self.bert_model.eval() # Set to evaluation mode

    def get_bert_embeddings(self, texts):
        """
        Extracts BERT embeddings (CLS token) for a list of texts.
        """
        embeddings = []
        for text in texts:
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=64)
            with torch.no_grad():
                outputs = self.bert_model(**inputs)
            # Use the [CLS] token embedding (first token)
            cls_embedding = outputs.last_hidden_state[:, 0, :].numpy().flatten()
            embeddings.append(cls_embedding)
        return np.array(embeddings)

    def train(self, texts, labels):
        """
        Trains the hybrid model.
        """
        print("Preprocessing data...")
        cleaned_texts, pos_features = self.preprocessor.preprocess_batch(texts)
        
        print("Extracting TF-IDF features...")
        tfidf_features = self.tfidf.fit_transform(cleaned_texts).toarray()
        
        print("Extracting BERT embeddings...")
        bert_features = self.get_bert_embeddings(cleaned_texts)
        
        # Combine features: TF-IDF + POS + BERT
        # Shape: (n_samples, 100 + 3 + 768)
        combined_features = np.hstack((tfidf_features, pos_features, bert_features))
        
        print(f"Training Random Forest on feature vector of shape {combined_features.shape}...")
        self.classifier.fit(combined_features, labels)
        print("Training complete.")

    def predict(self, text):
        """
        Predicts class for a single text.
        """
        cleaned_texts, pos_features = self.preprocessor.preprocess_batch([text])
        tfidf_features = self.tfidf.transform(cleaned_texts).toarray()
        bert_features = self.get_bert_embeddings(cleaned_texts)
        
        combined_features = np.hstack((tfidf_features, pos_features, bert_features))
        prediction = self.classifier.predict(combined_features)[0]
        probabilities = self.classifier.predict_proba(combined_features)[0]
        
        return prediction, probabilities

    def save_model(self, path="model_artifacts"):
        if not os.path.exists(path):
            os.makedirs(path)
        joblib.dump(self.classifier, os.path.join(path, "rf_classifier.joblib"))
        joblib.dump(self.tfidf, os.path.join(path, "tfidf.joblib"))
        print(f"Model artifacts saved to {path}")

    def load_model(self, path="model_artifacts"):
        self.classifier = joblib.load(os.path.join(path, "rf_classifier.joblib"))
        self.tfidf = joblib.load(os.path.join(path, "tfidf.joblib"))
        print("Model artifacts loaded.")

# --- Dummy Training Script ---
if __name__ == "__main__":
    # Dummy Dataset
    # 0 = Animal, 1 = Car
    train_texts = [
        "The jaguar is a solitary predator native to the Americas.",
        "Jaguars are known for their beautiful spotted coats.",
        "The big cat, the jaguar, hunts at night.",
        "I saw a jaguar in the zoo today.",
        "The jaguar runs very fast in the jungle.",
        
        "I test drove the new Jaguar F-Type yesterday.",
        "The Jaguar sedan offers a luxurious ride.",
        "Jaguar cars are known for their speed and elegance.",
        "The dealer showed me the latest Jaguar model.",
        "My neighbor bought a vintage Jaguar E-Type."
    ]
    train_labels = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    model = JaguarClassifier()
    model.train(train_texts, train_labels)
    
    # Test
    test_sentence = "The jaguar speeds through the rainforest."
    pred, prob = model.predict(test_sentence)
    print(f"\nTest Sentence: '{test_sentence}'")
    print(f"Prediction: {'Car' if pred == 1 else 'Animal'}")
    print(f"Confidence: {max(prob):.2f}")

    test_sentence_2 = "The jaguar speeds down the highway."
    pred, prob = model.predict(test_sentence_2)
    print(f"\nTest Sentence: '{test_sentence_2}'")
    print(f"Prediction: {'Car' if pred == 1 else 'Animal'}")
    print(f"Confidence: {max(prob):.2f}")
    
    model.save_model()
