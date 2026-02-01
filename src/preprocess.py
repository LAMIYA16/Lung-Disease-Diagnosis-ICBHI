import librosa
import numpy as np

def load_audio(path, sr=22050):
    signal, _ = librosa.load(path, sr=sr)
    return signal

def normalize(signal):
    return signal / (np.max(np.abs(signal)) + 1e-6)
