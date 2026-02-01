import os
import shutil
import csv

AUDIO_DIR = os.path.join(os.path.dirname(__file__), "../ICBHI_audio/audio")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../data/raw")
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/labels.csv")

NORMAL_DIR = os.path.join(OUTPUT_DIR, "normal")
ABNORMAL_DIR = os.path.join(OUTPUT_DIR, "abnormal")

os.makedirs(NORMAL_DIR, exist_ok=True)
os.makedirs(ABNORMAL_DIR, exist_ok=True)

rows = []

for file in os.listdir(AUDIO_DIR):
    if file.endswith(".wav"):
        wav_path = os.path.join(AUDIO_DIR, file)
        txt_path = wav_path.replace(".wav", ".txt")

        if not os.path.exists(txt_path):
            continue

        is_abnormal = False

        with open(txt_path, "r") as f:
            for line in f:
                _, _, crackle, wheeze = line.strip().split()
                if int(crackle) == 1 or int(wheeze) == 1:
                    is_abnormal = True
                    break

        label = "abnormal" if is_abnormal else "normal"
        label_value = 1 if is_abnormal else 0

        dest_dir = ABNORMAL_DIR if is_abnormal else NORMAL_DIR
        shutil.copy(wav_path, os.path.join(dest_dir, file))

        rows.append([file, label, label_value])

# Write CSV
with open(CSV_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "label", "label_value"])
    writer.writerows(rows)

print("Dataset organized and CSV generated")
