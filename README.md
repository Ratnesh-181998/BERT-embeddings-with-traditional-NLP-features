# Jaguar Word Sense Disambiguation (WSD) System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A Machine Learning system designed to disambiguate the word "**jaguar**" in text, classifying it as either an **Animal** or a **Car** brand based on context. This project demonstrates a hybrid approach combining **BERT embeddings** with traditional **NLP features** (TF-IDF, POS tagging).

## 🚀 Features

-   **Hybrid Model**: Combines deep learning embeddings (BERT) with linguistic features.
-   **Real-time Inference**: Fast predictions via a **FastAPI** server.
-   **Interactive Documentation**: Built-in Swagger UI for testing.
-   **Extensible**: Modular design for easy addition of new features or models.

## 📂 Project Structure

```
Jaguar_Project/
├── src/
│   ├── app.py              # FastAPI application server
│   ├── model_train.py      # Model training script & Classifier class
│   └── preprocessing.py    # Text cleaning and feature extraction
├── model_artifacts/        # Saved models (excluded from git)
├── requirements.txt        # Project dependencies
├── setup_github.ps1        # Helper script for GitHub upload
├── GITHUB_UPLOAD_GUIDE.md  # Instructions for uploading to GitHub
├── PROJECT_SUMMARY.md      # Detailed system design notes
└── README.md               # This file
```

## 🛠️ Setup & Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/Ratnesh-181998/BERT-embeddings-with-traditional-NLP-features.git
    cd BERT-embeddings-with-traditional-NLP-features
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Running the Project

### 1. Train the Model (Demo)
Train the model on a dummy dataset to generate artifacts:
```bash
python src/model_train.py
```

### 2. Start the API Server
Launch the FastAPI server:
```bash
python src/app.py
```
The server will start at `http://localhost:8000`.

### 3. Test the API
Open your browser and navigate to:
[http://localhost:8000/docs](http://localhost:8000/docs)

You can use the interactive Swagger UI to send test sentences like:
-   *"The jaguar runs fast in the jungle."* (Expected: Animal)
-   *"I bought a new Jaguar F-Type."* (Expected: Car)

## 🧠 Model Details

For a deep dive into the system design, feature engineering, and modeling approach, please refer to [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md).

-   **Embeddings**: `bert-base-uncased` (768 dims)
-   **Features**: TF-IDF + POS Counts
-   **Classifier**: Random Forest

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Ratnesh Kumar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Ratnesh-181998)

Feel free to reach out for questions, collaborations, or feedback!
