import os
import numpy as np
import joblib
from preprocess import load_audio, normalize
from fft_features import extract_fft
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

DATA_DIR = "../data/raw"

X, y = [], []

for label, value in [("normal", 0), ("abnormal", 1)]:
    folder = os.path.join(DATA_DIR, label)
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            signal = load_audio(os.path.join(folder, file))
            signal = normalize(signal)
            features = extract_fft(signal)
            X.append(features)
            y.append(value)

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(model, "../model/rf_model.pkl")
print("Model saved")
