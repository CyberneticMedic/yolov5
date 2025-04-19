from PIL import Image
import os

input_dir = "./data_conversion/preprocessed_size_normalization"
output_dir = "./data_conversion/preprocessed_YOLO_convert"
os.makedirs(output_dir, exist_ok=True)

target_size = 416  # YOLOv5 input size

# Loop through all valid image files
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert("RGB")

        # Resize while maintaining aspect ratio using LANCZOS
        img.thumbnail((target_size, target_size), Image.Resampling.LANCZOS)

        # Create a new 416x416 black canvas
        new_img = Image.new("RGB", (target_size, target_size), (0, 0, 0))
        offset_x = (target_size - img.width) // 2
        offset_y = (target_size - img.height) // 2
        new_img.paste(img, (offset_x, offset_y))

        # Save with same filename but as .png
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name + ".png")
        new_img.save(output_path, "PNG")

        print(f"Resized and saved: {output_path}")
