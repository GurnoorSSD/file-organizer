import os
import shutil

def organize_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Folder does not exist.")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower() if ext else "NO_EXTENSION"

            # Create folder for this extension
            ext_folder = os.path.join(folder_path, ext.strip(".") or ext)
            os.makedirs(ext_folder, exist_ok=True)

            # Move file
            new_path = os.path.join(ext_folder, filename)
            shutil.move(file_path, new_path)
            print(f"✅ Moved: {filename} → {ext_folder}")
            files_moved += 1

    if files_moved:
        print(f"\n🎉 Organized {files_moved} files by extension!")
    else:
        print("⚠️ No files found to organize.")

# === Ask user for folder path ===
folder = input("Enter full path of the folder to organize:\n")
organize_by_extension(folder)

input("\nPress Enter to exit...")
