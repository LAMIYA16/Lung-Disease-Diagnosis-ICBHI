import numpy as np


def extract_fft_features(signal):
    fft = np.abs(np.fft.rfft(signal))
    fft = fft / np.max(fft)

    features = [
        np.mean(fft),
        np.std(fft),
        np.max(fft),
        np.sum(fft[20:200]),    # low freq (breathing)
        np.sum(fft[200:800]),   # wheeze range
        np.sum(fft[800:2000])   # crackles
    ]

    return np.array(features)


def asthma_rule_based(fft):
    wheeze_energy = np.sum(fft[200:800])
    total_energy = np.sum(fft)

    ratio = wheeze_energy / total_energy

    return ratio > 0.45  # threshold (can tune)
