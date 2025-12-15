import sys
from cowsay_demo import cowsay

def main():
    print("Hello from gitsample-project!")
    message = sys.argv[1] if len(sys.argv) > 1 else "Hello from main!"
    cowsay(message)


if __name__ == "__main__":
    main()
