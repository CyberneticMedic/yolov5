import subprocess
import os

# === Step 1: Clear old cache files ===
cache_files = ["dual_train.cache", "dual_val.cache"]
for cache_file in cache_files:
    if os.path.exists(cache_file):
        os.remove(cache_file)
        print(f"🧹 Removed: {cache_file}")
    else:
        print(f"✅ Already clean: {cache_file}")

# === Step 2: Regenerate TXT split files ===
print("🔄 Regenerating dual_train.txt and dual_val.txt...")
subprocess.run(["python", "generate_combined_txt.py"])

# === Step 3: Launch training ===
train_script = "train.py"
yaml_path = "dual_dataset.yaml"
weights_path = ""  # Empty for training from scratch
cfg_path = "models/yolov5s.yaml"
hyp_path = "data/hyps/hyp.custom.yaml"
run_name = "WN_trainhypOBJ0.5_IouT_0.4"#######################################################

command = [
    "python", train_script,
    "--cfg", cfg_path,
    "--hyp", hyp_path,
    "--img", "416",
    "--batch", "8",
    "--epochs", "100",
    "--data", yaml_path,
    "--weights", weights_path,
    "--name", run_name,
    "--exist-ok"
]

print(f"\n🚀 Launching YOLOv5 training with config: {yaml_path}")
subprocess.run(command)
