import os
def get_file_content(working_directory, file_path):
    target_filepath = os.path.abspath(os.path.join(working_directory,file_path))
    abs_dir_path = os.path.abspath(working_directory)
    if not target_filepath.startswith(abs_dir_path):
        return f'Error: Cannot list "{target_filepath}" as it is outside the permitted working directory'
    if not os.path.isfile(target_filepath):
        return f'Error: File not found or is not a regular file: "{target_filepath}"'
    
    MAX_CHARS = 10000
    try:
        with open(target_filepath, "r") as f:
            file_content = f.read(MAX_CHARS)
            next_char = f.read(1)
            if next_char:
                return file_content + f'[...File "{file_path}" truncated at 10000 characters]'
            else:
                return file_content

    except Exception as e:
        print(f'Error reading files: {e}')