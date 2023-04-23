

def filetype_validator(file, allowed_files):
    if file.name.lower().endswith(allowed_files):
        return True
    else:
        return False
