import os
def write_file(working_directory, file_path, content):
    target_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path = os.path.abspath(working_directory)
    if not target_filepath.startswith(abs_path):
        return f'Error: Cannot write to "{target_filepath}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(target_filepath),exist_ok=True)
    except Exception as e:
        return f'Error: {e}'
    try:
        with open(target_filepath, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{target_filepath}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing files: {e}'
