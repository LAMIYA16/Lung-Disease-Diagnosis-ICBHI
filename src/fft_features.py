import numpy as np
from scipy.fft import fft

def extract_fft(signal, n_features=1000):
    fft_vals = np.abs(fft(signal))
    return fft_vals[:n_features]
