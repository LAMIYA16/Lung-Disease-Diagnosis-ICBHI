import os
import shutil



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICBHI_AUDIO = r"C:\Users\lamiy\Downloads\archive (2)\ICBHI_final_database"
OUTPUT_DIR = os.path.join(BASE_DIR, "../data/raw")

os.makedirs(os.path.join(OUTPUT_DIR, "normal"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "abnormal"), exist_ok=True)

if not os.path.exists(ICBHI_AUDIO):
    print(f"Error: Directory not found: {ICBHI_AUDIO}")
    exit(1)

for file in os.listdir(ICBHI_AUDIO):
    if file.endswith(".wav"):
        txt_file = file.replace(".wav", ".txt")
        txt_path = os.path.join(ICBHI_AUDIO, txt_file)

        is_abnormal = False

        with open(txt_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                crackle = int(parts[2])
                wheeze = int(parts[3])

                if crackle == 1 or wheeze == 1:
                    is_abnormal = True
                    break

        label = "abnormal" if is_abnormal else "normal"

        shutil.copy(
            os.path.join(ICBHI_AUDIO, file),
            os.path.join(OUTPUT_DIR, label, file)
        )

print("Dataset organized into Normal and Abnormal")
