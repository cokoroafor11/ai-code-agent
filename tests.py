from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "main.py")
    print("Result:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result:")
    print(result)
    

if __name__ == "__main__":
    test()
