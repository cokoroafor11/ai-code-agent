import os
def get_files_info(working_directory, directory="."):
    target_dir_path = os.path.abspath(os.path.join(working_directory,directory))
    abs_dir_path = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir_path.startswith(abs_dir_path):
        return f'Error: Cannot list "{target_dir_path}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir_path):
        return f'Error: {target_dir_path} is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir_path):
            file_size = os.path.getsize(os.path.join(target_dir_path,filename))
            path_is_file = os.path.isfile(os.path.join(target_dir_path,filename))
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={path_is_file}"
            )
        return "\n".join(files_info)
    except Exception as e:
        print(f'Error listing files: {e}')


get_files_info("functions","tests.py")