# 🍌 Minionese 🍌

### *Bello! Poopaye! Tank Yu!*

Ever wondered what your texts would sound like if a Minion wrote them?
Wonder no more. **Minionese** is a fun little translation engine that turns
your English into gloriously silly Minion-speak — complete with a
goggles-and-overalls themed web app and a CLI for the terminal purists.

> 🚨 Disclaimer: this is a fan-made side project for fun.

---

## 🎉 What it does

Type this:
```
Hello my friend, I am hungry! Let's go eat cake.
```

Get this:
```
Bello myzo bapple, Iiito aameeno stomacho-grumbo! Vamoonow chompo cakoo.
```

Every word gets the Minionese treatment — either pulled straight from a
150+ word dictionary (with a few iconic classics kept intact, like
**bello**, **poopaye**, and **tank yu**), or run through a phonetic
fallback engine for anything not on the list. Same word in, same silly
word out, every single time. Capitalization and punctuation survive the
chaos too.

---

## 🍌 Try the Web App

A full goggles-and-overalls themed Streamlit app, because plain text boxes
are for people who don't love bananas.

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔵 Or Live in the Terminal

```bash
# Straight-up translate
python3 minionese.py "Hello my friend, I am hungry!"

# Decode Minionese back to English
python3 minionese.py --reverse "Bello bapple, tank yu!"

# Browse the word bank
python3 minionese.py --wordbank
python3 minionese.py --wordbank love

# No arguments = interactive mode
python3 minionese.py
```

Interactive mode commands: `:reverse <text>`, `:wordbank`, `:quit`.

---



## 📁 What's in here

| File | What it does |
|---|---|
| `app.py` | The Minion-themed Streamlit app |
| `minionese.py` | CLI entry point |
| `dictionary.py` | The word bank |
| `phonetics.py` | Fallback engine for unlisted words |
| `translator.py` | The brains — tokenizing, case-matching, translating |

---

## ✨ Add your own words

Everything reads from one dictionary, so adding a word updates both the
CLI and the web app instantly:

```python
"example": ("examplo-doo", "your note here"),
```

Multi-word phrases work the same way — just put a space in the key.

---

🍌 *Poopaye!* 🍌
