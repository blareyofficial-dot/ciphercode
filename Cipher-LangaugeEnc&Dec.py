# Mason's Cipher Language (built-in)

mapping = {
    "a": "o", "b": "m", "c": "k", "d": "r", "e": "t", "f": "p",
    "g": "q", "h": "s", "i": "n", "j": "v", "k": "a", "l": "b",
    "m": "c", "n": "d", "o": "e", "p": "f", "q": "g", "r": "h",
    "s": "i", "t": "j", "u": "l", "v": "u", "w": "y", "x": "z",
    "y": "x", "z": "w"
}

# Reverse mapping for decoding
reverse = {v: k for k, v in mapping.items()}


def encode(text):
    output = ""
    for char in text.lower():
        if char in mapping:
            output += mapping[char]
        else:
            output += char
    return output


def decode(text):
    output = ""
    for char in text.lower():
        if char in reverse:
            output += reverse[char]
        else:
            output += char
    return output


def main():
    while True:
        print("\n--- Mason's Cipher Tool ---")
        print("1. Encode English → Cipher")
        print("2. Decode Cipher → English")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Enter English text: ")
            print("Encoded:", encode(text))

        elif choice == "2":
            text = input("Enter cipher text: ")
            print("Decoded:", decode(text))

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
