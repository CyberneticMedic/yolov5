import os
import shutil
import random
from pathlib import Path

# CONFIG
SOURCE_DIR = r"C:\Users\School\Desktop\yolov5\data_conversion\preprocessed_YOLO_convert"
DEST_DIR   = r"C:\Users\School\Desktop\yolov5\yolov5\my_dataset"
TRAIN_RATIO = 0.9

# FOLDER STRUCTURE
images_train = os.path.join(DEST_DIR, "images", "train")
images_val   = os.path.join(DEST_DIR, "images", "val")
labels_train = os.path.join(DEST_DIR, "labels", "train")
labels_val   = os.path.join(DEST_DIR, "labels", "val")

# CREATE OUTPUT DIRECTORIES
for folder in [images_train, images_val, labels_train, labels_val]:
    os.makedirs(folder, exist_ok=True)

# GET .png FILES ONLY
image_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".png")]
image_files.sort()
random.shuffle(image_files)

# SPLIT
split_index = int(len(image_files) * TRAIN_RATIO)
train_files = image_files[:split_index]
val_files   = image_files[split_index:]

def copy_pair(image_list, img_dest, lbl_dest):
    for img in image_list:
        base = Path(img).stem
        img_path = os.path.join(SOURCE_DIR, base + ".png")
        txt_path = os.path.join(SOURCE_DIR, base + ".txt")
        dest_img_path = os.path.join(img_dest, base + ".png")
        dest_txt_path = os.path.join(lbl_dest, base + ".txt")

        # Copy image only if not already present
        if not os.path.exists(dest_img_path):
            shutil.copy(img_path, dest_img_path)
        else:
            print(f"[SKIP] Image {dest_img_path} already exists.")

        # Copy label if it exists and isn't already copied
        if os.path.exists(txt_path):
            if not os.path.exists(dest_txt_path):
                shutil.copy(txt_path, dest_txt_path)
            else:
                print(f"[SKIP] Label {dest_txt_path} already exists.")
        else:
            print(f"[INFO] No label for {img} — treated as negative sample.")


copy_pair(train_files, images_train, labels_train)
copy_pair(val_files, images_val, labels_val)

print("Dataset is ready in 'yolov5/yolov5/my_dataset/'")
