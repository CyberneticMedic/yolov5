from pathlib import Path

# Output text files
train_out = "dual_train.txt"
val_out = "dual_val.txt"

# Paths to training image directories
train_dirs = [
    Path("my_dataset/images/train"),
    Path("roboflow/train/images")
]

# Paths to validation image directories
val_dirs = [
    Path("my_dataset/images/val"),
    Path("roboflow/valid/images")
]

valid_exts = [".jpg", ".jpeg", ".png"]

def write_paths(directories, output_file):
    all_images = []
    for d in directories:
        if d.exists():
            for img in d.glob("*"):
                if img.suffix.lower() in valid_exts:
                    all_images.append(str(img.resolve()))
    with open(output_file, "w") as f:
        f.write("\n".join(all_images))
    print(f"Wrote {len(all_images)} entries to {output_file}")

write_paths(train_dirs, train_out)
write_paths(val_dirs, val_out)
