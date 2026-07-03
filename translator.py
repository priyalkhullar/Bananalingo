"""
Core English <-> Minionese translation logic.

Handles:
- Dictionary lookups (multi-word phrases checked first)
- Phonetic fallback for unknown words
- Capitalization preservation
- Punctuation preservation
"""

import re

from dictionary import DICTIONARY, PHRASE_PRIORITY, REVERSE_DICTIONARY
from phonetics import phonetic_transform

# Splits into words vs. non-word chunks (punctuation/whitespace), keeping both
TOKEN_RE = re.compile(r"[A-Za-z']+|[^A-Za-z']+")


def _match_case(source: str, target: str) -> str:
    """Apply the capitalization pattern of `source` onto `target`."""
    if source.isupper() and len(source) > 1:
        return target.upper()
    if source[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


def _translate_word(word: str) -> str:
    lower = word.lower()
    if lower in DICTIONARY:
        translated = DICTIONARY[lower][0]
    else:
        translated = phonetic_transform(lower)
    return _match_case(word, translated)


def to_minionese(text: str) -> str:
    """Translate English text into Minionese, preserving case & punctuation."""
    lower_text = text.lower()

    # Step 1: find non-overlapping multi-word phrase matches and stash their
    # already-translated replacement behind a placeholder, so the later
    # word-by-word pass doesn't re-translate them.
    placeholders = {}
    i = 0
    buffer = ""
    while i < len(text):
        matched = False
        for phrase in PHRASE_PRIORITY:
            plen = len(phrase)
            if lower_text[i : i + plen] == phrase:
                original_chunk = text[i : i + plen]
                translated = DICTIONARY[phrase][0]
                key = f"\x00{len(placeholders)}\x00"
                placeholders[key] = _match_case(original_chunk, translated)
                buffer += key
                i += plen
                matched = True
                break
        if not matched:
            buffer += text[i]
            i += 1
    remaining = buffer

    # Step 2: split on placeholder markers first, so whitespace around them
    # never gets fused into the same token as the marker itself.
    placeholder_re = re.compile(r"\x00\d+\x00")
    output_parts = []
    last_end = 0
    for m in placeholder_re.finditer(remaining):
        chunk = remaining[last_end : m.start()]
        output_parts.append(_translate_chunk(chunk))
        output_parts.append(placeholders[m.group()])
        last_end = m.end()
    output_parts.append(_translate_chunk(remaining[last_end:]))

    return "".join(output_parts)


def _translate_chunk(chunk: str) -> str:
    """Translate word-by-word for a chunk with no placeholders inside."""
    tokens = TOKEN_RE.findall(chunk)
    parts = []
    for tok in tokens:
        if tok.replace("'", "").isalpha():
            parts.append(_translate_word(tok))
        else:
            parts.append(tok)
    return "".join(parts)


def to_english(text: str) -> str:
    """
    Best-effort Minionese -> English translation.
    Only works for words present in the reverse dictionary;
    unknown words are left as-is (phonetic fallback isn't reversible).
    """
    tokens = TOKEN_RE.findall(text)
    output_parts = []
    for tok in tokens:
        lower = tok.lower()
        if lower in REVERSE_DICTIONARY:
            translated = REVERSE_DICTIONARY[lower][0]
            output_parts.append(_match_case(tok, translated))
        else:
            output_parts.append(tok)
    return "".join(output_parts)