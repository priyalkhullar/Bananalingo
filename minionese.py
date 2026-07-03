#!/usr/bin/env python3
"""
Minionese Translator CLI
-------------------------
Translate English text into Minionese (and back), or browse the word bank.

Usage:
    python3 minionese.py "Hello my friend, I am hungry!"
    python3 minionese.py --reverse "Bello bapple, bello stomacho-grumbo!"
    python3 minionese.py --wordbank
    python3 minionese.py --wordbank love
    python3 minionese.py            (interactive mode)
"""

import argparse
import sys

from dictionary import DICTIONARY
from translator import to_english, to_minionese


def print_wordbank(filter_term: str = None):
    print("\n=== Minionese Word Bank ===\n")
    entries = sorted(DICTIONARY.items())
    if filter_term:
        filter_term = filter_term.lower()
        entries = [
            (k, v) for k, v in entries
            if filter_term in k.lower() or filter_term in v[0].lower()
        ]
        if not entries:
            print(f"No entries found matching '{filter_term}'.")
            return

    width_en = max(len(k) for k, _ in entries)
    width_mn = max(len(v[0]) for _, v in entries)

    for english, (minionese, note) in entries:
        print(f"  {english.ljust(width_en)}  ->  {minionese.ljust(width_mn)}   ({note})")
    print(f"\n{len(entries)} word(s) shown.\n")


def interactive_mode():
    print("=== Minionese Translator (interactive) ===")
    print("Type English text to translate. Commands: :reverse <text>, :wordbank, :quit\n")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPoopaye!")
            break

        if not line:
            continue
        if line in (":quit", ":q", "exit"):
            print("Poopaye!")
            break
        if line == ":wordbank":
            print_wordbank()
            continue
        if line.startswith(":reverse "):
            print(to_english(line[len(":reverse "):]))
            continue

        print(to_minionese(line))


def main():
    parser = argparse.ArgumentParser(description="English <-> Minionese translator")
    parser.add_argument("text", nargs="*", help="Text to translate")
    parser.add_argument("-r", "--reverse", action="store_true", help="Translate Minionese -> English")
    parser.add_argument("-w", "--wordbank", nargs="?", const="", metavar="FILTER",
                         help="Show the word bank, optionally filtered by a search term")
    args = parser.parse_args()

    if args.wordbank is not None:
        print_wordbank(args.wordbank or None)
        return

    if not args.text:
        interactive_mode()
        return

    text = " ".join(args.text)
    if args.reverse:
        print(to_english(text))
    else:
        print(to_minionese(text))


if __name__ == "__main__":
    sys.exit(main())