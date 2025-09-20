import argparse
morse_code_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"   # use "/" to represent a space between words
}

morse_code_reverse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
   # slash or 3 spaces means "space" between words
}


def decodeMessage(string):
    string = string.strip()
    string = string.split("   ")
    result = []
    for i in string:
        j = i.split(" ")
        word = ""
        for b in j:
            word += morse_code_reverse[b]
        result.append(word)
    return " ".join(result)


def encodeMessage(string):
    string = string.strip()
    result = []
    for i in string.upper():
        print()
        result.append(morse_code_alphabet[i])
    return " ".join(result)


def handle(command, string):
    # Join list into a single string for encoding/decoding
    string = " ".join(string)

    if command == "encode":
        print("encode:", encodeMessage(string))
    elif command == "decode":
        print("decode:", decodeMessage(string))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    encodeParser = sub.add_parser("encode")
    encodeParser.add_argument("string", type=str, nargs=argparse.REMAINDER)

    decodeParser = sub.add_parser("decode")
    decodeParser.add_argument("string", type=str, nargs=argparse.REMAINDER)

    args = parser.parse_args()
    handle(args.command, args.string)
