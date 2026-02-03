import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_audio
from fft_features import extract_fft_features

DATA_DIR = "../data/raw"
CLASSES = ["normal", "copd", "pneumonia"]  # asthma excluded

X, y = [], []

for label in CLASSES:
    class_dir = os.path.join(DATA_DIR, label)
    for file in os.listdir(class_dir):
        if file.endswith(".wav"):
            path = os.path.join(class_dir, file)
            signal = load_audio(path)
            if signal is None:
                 continue
            features = extract_fft_features(signal)
  
            X.append(features)
            y.append(label)

X = np.array(X)
y = np.array(y)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

os.makedirs("../model", exist_ok=True)
with open("../model/rf_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Random Forest trained (normal / copd / pneumonia)")
