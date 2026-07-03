"""
Phonetic fallback engine for Minionese.

Any English word NOT found in the dictionary gets run through this
deterministic transform so it still sounds consistently "Minionese":
same word in -> same word out, every time.
"""

import hashlib

# Ordered letter/sound substitutions (applied left to right)
SOUND_SWAPS = [
    ("th", "t"),
    ("ph", "f"),
    ("ck", "k"),
    ("qu", "kw"),
    ("x", "ks"),
    ("v", "b"),
    ("r", "l"),
]

# Suffix bank -- picked deterministically per word, not randomly,
# so the same input always maps to the same output.
SUFFIXES = ["oo", "ito", "oto", "eeno", "zo", "poo", "ino", "atto"]


def _pick_suffix(word: str) -> str:
    """Deterministically pick a suffix based on the word itself."""
    digest = hashlib.md5(word.encode("utf-8")).hexdigest()
    index = int(digest, 16) % len(SUFFIXES)
    return SUFFIXES[index]


def phonetic_transform(word: str) -> str:
    """
    Transform a single lowercase English word into a Minionese-sounding
    word using consistent sound swaps + a deterministic suffix.
    """
    if not word:
        return word

    base = word.lower()

    for old, new in SOUND_SWAPS:
        base = base.replace(old, new)

    # Duplicate a vowel somewhere in short words for extra silliness
    vowels = "aeiou"
    if len(base) <= 4:
        for i, ch in enumerate(base):
            if ch in vowels:
                base = base[: i + 1] + ch + base[i + 1 :]
                break

    suffix = _pick_suffix(word.lower())
    # Avoid double suffix if the word already ends similarly
    if not base.endswith(suffix):
        base += suffix

    return base