import os

directory = input("What path do you want to search for .mp3 files? >> ")


def rename(direc: str, file_name: str):
    if file_name.endswith(".mp3"):
        split_name = file_name.split(" - ")
        full_path = os.path.join(direc, file_name)
        # print(full_path)
        os.rename(src=full_path, dst=split_name[2])


for file in os.listdir(directory):
    rename(directory, file)
