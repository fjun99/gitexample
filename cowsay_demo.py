import sys

def cowsay(message):
    border = "-" * (len(message) + 2)
    print(f" {border}")
    print(f"< {message} >")
    print(f" {border}")
    print("        \\   ^__^")
    print("         \\  (oo)\\_______")
    print("            (__)\\       )\\/\\")
    print("                ||----w |")
    print("                ||     ||")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        try:
            message = input("What does the cow say? ")
        except EOFError:
            message = "Moo"
    if not message:
        message = "Moo"
    cowsay(message)
