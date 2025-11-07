from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result:")
    print(result)
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result:")
    print(result)

    

if __name__ == "__main__":
    test()
