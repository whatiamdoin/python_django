from pathlib import Path


def read_file(filename):
    with open(filename) as file:
        return file.read()


def save_file(time, file, destination, stud_class, lab_group, email):
    path_tree = f"{destination}{stud_class}\\{lab_group}\\{email}\\"
    Path(path_tree).mkdir(parents=True, exist_ok=True)
    with open(f"{path_tree}{time}_{file.name}", "wb+") as file_to_save:
        for chunk in file.chunks():
            file_to_save.write(chunk)
