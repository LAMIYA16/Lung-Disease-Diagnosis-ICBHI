import pickle
import sys
import numpy as np
from preprocess import load_audio
from fft_features import extract_fft_features, asthma_rule_based

MODEL_PATH = "../model/rf_model.pkl"

LABELS = ["normal", "copd", "pneumonia"]

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_audio(file_path):
    signal = load_audio(file_path)

    if signal is None:
        print("❌ Error: Audio file is corrupted or unreadable")
        return "invalid_audio", 0.0

    fft = np.abs(np.fft.rfft(signal))
    features = extract_fft_features(signal)

    # 1️⃣ Asthma rule FIRST
    if asthma_rule_based(fft):
        return "asthma", 0.95

    # 2️⃣ Random Forest for normal / COPD / pneumonia
    probs = model.predict_proba([features])[0]
    pred = LABELS[np.argmax(probs)]
    confidence = np.max(probs)

    return pred, confidence


if __name__ == "__main__":
    audio_path = sys.argv[1]
    prediction, confidence = predict_audio(audio_path)

    print("\nPrediction:", prediction)
    print("Confidence:", round(confidence * 100, 2), "%")
