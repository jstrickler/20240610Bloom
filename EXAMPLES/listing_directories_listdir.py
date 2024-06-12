import os
from datetime import datetime

DIRECTORY = '../DATA'

for entry_name in os.listdir(DIRECTORY):
    file_path = os.path.join(DIRECTORY, entry_name)
    file_size = os.path.getsize(file_path)
    file_raw_timestamp = os.path.getmtime(file_path)
    file_timestamp = datetime.fromtimestamp(file_raw_timestamp)
    print(f"{entry_name:30s} {file_size:10d} {file_timestamp}")
print('-' * 60)
print(os.listdir(DIRECTORY))
