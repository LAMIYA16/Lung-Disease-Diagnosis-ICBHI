import os
import shutil

SRC_DIR = r"c:\Users\lamiy\Downloads\archive (2)\ICBHI_final_database"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.path.join(BASE_DIR, "../ICBHI_audio/audio")

os.makedirs(DEST_DIR, exist_ok=True)

for file in os.listdir(SRC_DIR):
    if file.endswith(".wav") or file.endswith(".txt"):
        shutil.copy(
            os.path.join(SRC_DIR, file),
            os.path.join(DEST_DIR, file)
        )

print("All WAV and TXT files copied to ICBHI_audio/audio")
