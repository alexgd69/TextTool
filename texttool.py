#!/usr/bin/env python3

def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    elif cmd == "lowercase":
        return text.lower()
    elif cmd == "count-words":
        return str(len(text.split()))
    elif cmd == "length":
        return str(len(text))
    elif cmd == "prefix":
        return text[:10]

    return "Unknown command " + cmd


def main():
    while True:
        try:
            line = input("commande> ")
        except EOFError:
            break

        print(process_line(line))


if __name__ == "__main__":
    main()
