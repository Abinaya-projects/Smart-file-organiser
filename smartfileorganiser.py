import os
import shutil

source_folder = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if extension in extensions:

                target_folder = os.path.join(source_folder, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, filename)
                )

                print(f"Moved {filename} -> {folder}")
                break

print("Organization completed!")
