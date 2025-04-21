from pathlib import Path

# Output files
train_out = "dual_train.txt"
val_out = "dual_val.txt"

# Define image sources
train_dirs = [
    Path("my_dataset/images/train"),
    Path("roboflow/train/images")
]

val_dirs = [
    Path("my_dataset/images/val"),
    Path("roboflow/valid/images")
]

# Image file types to include
valid_exts = [".jpg", ".jpeg", ".png"]

# Helper to write full paths to file
def write_paths(directories, output_file):
    all_images = []
    for d in directories:
        if d.exists():
            for img in d.glob("*"):
                if img.suffix.lower() in valid_exts:
                    all_images.append(str(img.resolve()))
    with open(output_file, "w") as f:
        f.write("\n".join(all_images))
    print(f"Saved {len(all_images)} paths to {output_file}")

# Write both splits
write_paths(train_dirs, train_out)
write_paths(val_dirs, val_out)
