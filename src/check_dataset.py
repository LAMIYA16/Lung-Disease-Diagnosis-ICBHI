import os
import librosa

DATA_DIR = "../data/raw"

for root, _, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root, file)
            try:
                librosa.load(path, sr=22050)
            except Exception as e:
                print("❌ Bad file:", path)
