# Project Summary: Jaguar Word Sense Disambiguation (WSD)

## Use Case
The goal of this project is to build a Machine Learning system that can disambiguate the word "**jaguar**" in a given sentence. Specifically, it predicts whether the word refers to the **Animal** or the **Car** brand.

## System Design (Based on your notes)
This system avoids using Generative LLMs (like GPT) and instead relies on a robust, hybrid approach combining traditional NLP features with modern contextual embeddings.

### 1. Data Pipeline
- **Input**: Raw sentences containing the word "jaguar".
- **Preprocessing**:
  - Tokenization
  - Lowercasing
  - Stopword removal
  - Lemmatization (optional)

### 2. Feature Engineering (Hybrid Approach)
The system combines two types of features to capture both syntax and semantics:
- **Traditional Features**:
  - **TF-IDF**: Captures keyword importance (Bag of Words).
  - **POS Tagging**: Identifies grammatical roles (e.g., "jaguar" as a Noun).
  - **Dependency Parsing**: Captures relationships (e.g., "drove" -> "jaguar").
- **Modern Embeddings**:
  - **BERT Embeddings**: Uses a pre-trained BERT model (`bert-base-uncased`) to generate 768-dimensional contextual vectors for the sentence.

### 3. Modeling
- **Feature Combination**: Concatenates TF-IDF vectors, POS tags, and BERT embeddings.
- **Dimensionality Reduction**: (Optional) PCA to reduce vector size if needed.
- **Classifier**: A **Random Forest Classifier** is trained on the combined feature set.
  - *Alternative*: BiLSTM + Attention (for more complex sequence modeling).

### 4. Deployment
- **API**: A **FastAPI** application serves the model.
- **Endpoint**: `/predict` accepts a sentence and returns the predicted class ("Animal" or "Car") and confidence score.
- **Optimization**: ONNX Runtime can be used for faster CPU inference.

---

## Project Structure
I have generated the following codebase for you:

1.  `requirements.txt`: Dependencies.
2.  `src/preprocessing.py`: NLP cleaning and feature extraction.
3.  `src/model_train.py`: Script to train the hybrid model using a dummy dataset (for demonstration).
4.  `src/app.py`: FastAPI server for inference.
