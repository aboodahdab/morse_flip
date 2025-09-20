import morse_talk as mtalk
import argparse


def decodeMessage(string):
    return mtalk.decode(string)


def encodeMessage(string):
    return mtalk.encode(string)


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
