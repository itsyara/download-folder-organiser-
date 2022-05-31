import os
import collections
from pprint import pprint

#find download folder
Download_Path = os.path.join(
    os.path.expanduser('~'),
    "Downloads"
)
#file type to folder
file_mappings = collections.defaultdict()
for file_name in os.listdir(Download_Path):
    file_type = file_name.split(".")[-1]
    file_mappings.setdefault(file_type,[]).append(file_name)
#pprint(file_mappings)
#move all file into their folders
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(Download_Path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_items in folder_items:
        source = os.path.join(Download_Path, folder_items)
        destination = os.path.join(folder_path, folder_items)
        print(f"Moving {source} to {destination}")

