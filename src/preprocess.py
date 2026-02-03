import librosa
import numpy as np

TARGET_SR = 22050
DURATION = 5


def load_audio(file_path):
    try:
        y, sr = librosa.load(file_path, sr=TARGET_SR)
    except Exception:
        return None

    max_len = TARGET_SR * DURATION

    if len(y) == 0:
        return None

    if len(y) > max_len:
        y = y[:max_len]
    else:
        y = np.pad(y, (0, max_len - len(y)))

    return y
