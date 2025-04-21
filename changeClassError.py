import os

# Set this to your project root (adjust if you're not running from root)
LABELS_DIR = "yolov5/my_dataset/labels"

# Walk through subdirectories (train, val, etc.)
for root, dirs, files in os.walk(LABELS_DIR):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            with open(full_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            updated = []
            changed = False
            for line in lines:
                if line.strip().startswith("15 "):
                    updated.append("0" + line[2:])
                    changed = True
                else:
                    updated.append(line)

            if changed:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.writelines(updated)
                print(f"✔ Updated class ID in: {full_path}")
