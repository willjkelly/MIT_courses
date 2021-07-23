import os
import sys

def get_name():

    name = input("Please enter student name, or [n/N/no/No] if done.: ")
    return name

def main():
    
    name = get_name()
    while name.lower() not in ['n', 'no']:

        os.mkdir(name)
        with open(f"{name}/README.md", 'w+') as f:
            f.write(f"Hi, my name is {name}!")
    
        name = get_name()

    return 0

if __name__ == "__main__":
    result = main()
    sys.exit(result)
