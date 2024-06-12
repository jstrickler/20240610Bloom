import os

start_folder = "."
skip_folder = ".git"

for folder, subs, files in os.walk(start_folder):
    if skip_folder in subs:
        subs.remove(skip_folder)
    print(folder)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            #   os.remove(file_path)  #  nuke it!
            print(f"    {file_size:8d} {file_name}")
