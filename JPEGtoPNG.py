from PIL import Image
import os
import shutil

# Ask user for input/output directories and prefix
input_dir = "./data_conversion/preprocessed_Filetype"
output_dir = "./data_conversion/preprocessed_size_normalization"
prefix = input("Enter filename prefix (e.g. 'background' or 'positive'): ").strip()
os.makedirs(output_dir, exist_ok=True)

# === Collect and Sort All Relevant Files ===
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
image_files.sort()

# === Convert and Rename ===
for i, filename in enumerate(image_files):
    input_path = os.path.join(input_dir, filename)
    new_name = f"{prefix}{i:03}.png"
    output_path = os.path.join(output_dir, new_name)

    if filename.lower().endswith((".jpg", ".jpeg")):
        # Convert JPEG to PNG
        img = Image.open(input_path).convert("RGB")
        img.save(output_path, "PNG")
        print(f"Converted {filename} → {new_name}")
    else:
        # Copy PNG directly and rename
        shutil.copy(input_path, output_path)
        print(f"Moved {filename} → {new_name}")