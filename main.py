import sys
from cowsay_demo import cowsay

def main():
    print("Hello from gitsample-project!")
    # Accept user input interactively
    try:
        message = input("Please enter the message for the cow: ")
        if not message:
            message = "Hello from main!"
    except EOFError:
        message = "Hello from main!"
    
    cowsay(message)


if __name__ == "__main__":
    main()
