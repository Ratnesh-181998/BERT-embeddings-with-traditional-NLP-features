from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Add src to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model_train import JaguarClassifier

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Jaguar WSD API", description="Predicts if 'jaguar' refers to an Animal or a Car.")

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact origin (e.g., http://localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model variable
model = None

@app.on_event("startup")
def load_model():
    global model
    model = JaguarClassifier()
    # In a real scenario, we would load the trained artifacts. 
    # For this demo, we will retrain on the dummy data on startup to ensure it works out of the box.
    print("Initializing and training model on dummy data...")
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
    model.train(train_texts, train_labels)
    print("Model ready.")

class PredictionRequest(BaseModel):
    sentence: str

@app.post("/predict")
def predict(request: PredictionRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    prediction_idx, probabilities = model.predict(request.sentence)
    label = "Car" if prediction_idx == 1 else "Animal"
    
    return {
        "sentence": request.sentence,
        "prediction": label,
        "confidence": float(max(probabilities)),
        "probabilities": {
            "Animal": float(probabilities[0]),
            "Car": float(probabilities[1])
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
