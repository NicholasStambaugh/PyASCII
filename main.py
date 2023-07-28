import pyfiglet

def generate_ascii_art(word):
    ascii_art = pyfiglet.figlet_format(word)
    return ascii_art

def main():
    word = input("Enter a word: ")
    ascii_art = generate_ascii_art(word)
    print(ascii_art)

if __name__ == "__main__":
    main()
