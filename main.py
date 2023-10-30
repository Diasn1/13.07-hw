import os

current_directory = os.getcwd()

watch_me_directory = os.path.join(current_directory, 'watch_me')
os.mkdir(watch_me_directory)

video_directory = os.path.join(current_directory, 'video')
sub_directory = os.path.join(current_directory, 'sub')

for folder in [video_directory, sub_directory]:
    for filename in os.listdir(folder):
        source_path = os.path.join(folder, filename)
        dest_path = os.path.join(watch_me_directory, filename)
        os.rename(source_path, dest_path)

print("Содержимое папок 'video' и 'sub' перемещено в 'watch_me'.")
####################################################################
import os

current_directory = os.getcwd()
file_list = os.listdir(current_directory)

for filename in file_list:
    parts = filename.split("_")

    if len(parts) >= 2:
        new_filename = parts[1] + "_" + parts[0] + "_".join(parts[2:])
        old_filepath = os.path.join(current_directory, filename)
        new_filepath = os.path.join(current_directory, new_filename)
        os.rename(old_filepath, new_filepath)

print("Файлы успешно переименованы.")
#############################################
import os
import shutil

current_directory = os.getcwd()

list_file_path = os.path.join(current_directory, 'list.csv')

list_directory = os.path.join(current_directory, 'list')

if not os.path.exists(list_directory):
    os.mkdir(list_directory)

if os.path.exists(list_file_path):
    with open(list_file_path, 'r') as file:
        file_list = file.read().splitlines()

    for filename in file_list:
        source_path = os.path.join(current_directory, filename)
        dest_path = os.path.join(list_directory, filename)

        if os.path.exists(source_path):
            shutil.move(source_path, dest_path)
            print(f"Файл '{filename}' перемещен в папку 'list'.")

    print("Файлы успешно перемещены в папку 'list'.")
else:
    print("Файл 'list.csv' не найден в текущей папке.")
