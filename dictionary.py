"""
Minionese Dictionary
---------------------
A curated English <-> Minionese word bank.

A handful of classic, instantly-recognizable Minion interjections are kept
intact (bello, poopaye, tank yu, para tu) since they're the "flavor" everyone
expects. The rest of the 150+ entries are original silly coinages built to
sound consistent with that vibe (double vowels, "-oo"/"-oto"/"-ito" endings,
soft consonant swaps).
"""

# word: (minionese, note/meaning-flavor-text)
DICTIONARY = {
    # --- Classic / iconic (kept intact) ---
    "hello": ("bello", "the OG Minion greeting"),
    "hi": ("bello", "casual greeting"),
    "bye": ("poopaye", "the legendary farewell"),
    "goodbye": ("poopaye", "formal farewell"),
    "thanks": ("tank yu", "gratitude, Minion style"),
    "thank you": ("tank yu", "gratitude, formal"),
    "please": ("para tu", "polite request"),
    "friend": ("bapple", "your ride-or-die pal"),
    "underwear": ("chichi pu", "iconic Minion obsession"),

    # --- Greetings & social ---
    "good morning": ("bonjourno-bello", "sunrise greeting"),
    "good night": ("nootee-bello", "bedtime farewell"),
    "welcome": ("bienvenoo", "invitation vibes"),
    "yes": ("poopayo", "affirmative"),
    "no": ("nooto", "negative"),
    "maybe": ("mizzabo", "uncertain"),
    "sorry": ("perlo-doo", "apology"),
    "excuse me": ("escuzimo", "polite interruption"),
    "how are you": ("como estoo", "checking in"),
    "i am fine": ("bello okey-doo", "doing well"),
    "nice to meet you": ("gusto-meecho", "pleased intro"),
    "see you later": ("looko-taro", "casual goodbye"),

    # --- Food (Minions love bananas & food) ---
    "banana": ("banana", "the sacred fruit, unchanged"),
    "food": ("nomoo", "sustenance"),
    "hungry": ("stomacho-grumbo", "need food now"),
    "delicious": ("yummoto", "tastes great"),
    "eat": ("chompo", "consume food"),
    "drink": ("gulpo", "consume liquid"),
    "cake": ("cakoo", "sweet celebration food"),
    "candy": ("dulcito", "sweet treat"),
    "breakfast": ("morno-nomoo", "first meal"),
    "lunch": ("meedo-nomoo", "midday meal"),
    "dinner": ("noshto", "evening meal"),
    "snack": ("snacko-bit", "small bite"),
    "water": ("aguapoo", "hydration"),

    # --- Emotions ---
    "happy": ("bappy", "joyful state"),
    "sad": ("sappo", "down state"),
    "angry": ("grrmpo", "mad state"),
    "excited": ("zippadoo", "hyped state"),
    "scared": ("yikeso", "fearful state"),
    "love": ("luvoo", "deep affection"),
    "like": ("likito", "mild affection"),
    "hate": ("no-luvoo", "strong dislike"),
    "tired": ("droopo", "sleepy state"),
    "bored": ("blahzo", "nothing to do"),
    "surprised": ("whatoo", "shocked state"),
    "confused": ("huhzo", "puzzled state"),
    "proud": ("chesto-poof", "accomplished feeling"),
    "silly": ("gooba", "playful nonsense"),
    "funny": ("hahato", "amusing"),
    "crazy": ("bonko", "wild energy"),

    # --- People & family ---
    "boss": ("gru-meesta", "the one in charge"),
    "family": ("famoolee", "your people"),
    "brother": ("bro-bap", "sibling, male"),
    "sister": ("sis-bap", "sibling, female"),
    "baby": ("babloo", "tiny human"),
    "kid": ("smolbap", "young human"),
    "girl": ("chiquita", "young female"),
    "boy": ("chiquito", "young male"),
    "king": ("rey-boss", "royal leader"),
    "queen": ("reina-boss", "royal leader, female"),
    "hero": ("gadgeto-champ", "the brave one"),
    "villain": ("baddoo", "the mischief-maker"),

    # --- Actions ---
    "run": ("zoomo", "move fast"),
    "walk": ("strollo", "move casually"),
    "jump": ("boingo", "leap up"),
    "dance": ("shakito", "move to music"),
    "sing": ("la-la-doo", "make music with voice"),
    "laugh": ("hehepoo", "express amusement"),
    "cry": ("bawlo", "express sadness"),
    "sleep": ("nootnoot", "rest"),
    "work": ("labooro", "do a job"),
    "play": ("playbo", "have fun"),
    "help": ("helpo-doo", "assist"),
    "stop": ("stoppo", "cease"),
    "go": ("goobo", "proceed"),
    "come": ("comito", "approach"),
    "look": ("lookoo", "observe"),
    "listen": ("earoo", "hear attentively"),
    "talk": ("talkito", "speak"),
    "think": ("brainzo", "ponder"),
    "build": ("makito", "construct"),
    "break": ("smasho", "destroy"),
    "fix": ("patchoo", "repair"),
    "explode": ("kaboomzo", "the Minion favorite pastime"),

    # --- Objects / tech (Minions + Gru's lab) ---
    "gadget": ("gizmoo", "cool device"),
    "weapon": ("zappo-stick", "tool of chaos"),
    "goggles": ("eye-poppers", "protective eyewear"),
    "overalls": ("blue-jumpo", "the classic uniform"),
    "car": ("vroomcar", "vehicle"),
    "rocket": ("blasto-ship", "space vehicle"),
    "money": ("goldito", "currency"),
    "book": ("readoo", "reading material"),
    "phone": ("talkobox", "communication device"),
    "computer": ("thinkobox", "processing device"),
    "door": ("openzo", "entryway"),
    "window": ("seetru", "glass opening"),

    # --- Descriptors ---
    "big": ("hugotron", "large size"),
    "small": ("teeny-boo", "tiny size"),
    "fast": ("speedito", "quick"),
    "slow": ("draggo", "unhurried"),
    "good": ("bueno-doo", "positive quality"),
    "bad": ("no-bueno", "negative quality"),
    "cold": ("brrzo", "low temperature"),
    "hot": ("scorchoo", "high temperature"),
    "beautiful": ("prettoolee", "attractive"),
    "ugly": ("yuckoo", "unattractive"),
    "smart": ("brainiotto", "intelligent"),
    "dumb": ("dopito", "unintelligent"),
    "strong": ("muscoolo", "powerful"),
    "weak": ("floppo", "lacking strength"),
    "new": ("freshito", "recent"),
    "old": ("dustoo", "aged"),
    "clean": ("shinyoo", "tidy"),
    "dirty": ("mucko", "unclean"),
    "loud": ("boomzo", "noisy"),
    "quiet": ("hushoo", "silent"),

    # --- Places ---
    "home": ("nesto", "dwelling"),
    "school": ("learnhouse", "place of learning"),
    "city": ("bigtowno", "urban area"),
    "beach": ("sandobay", "sandy shore"),
    "mountain": ("bigrocko", "tall landform"),
    "party": ("fiestoo", "celebration"),
    "lab": ("mixomatic", "science space"),
    "kitchen": ("nomzone", "cooking space"),
    "bathroom": ("splashroom", "washing space"),
    "office": ("deskito-zone", "work space"),

    # --- Time / misc ---
    "today": ("nowzo", "this day"),
    "tomorrow": ("nextday-oo", "the day after"),
    "yesterday": ("pastday-oo", "the day before"),
    "now": ("nowoo", "this moment"),
    "later": ("laterzo", "future moment"),
    "always": ("foreveroo", "all the time"),
    "never": ("nopezo-time", "not ever"),

    # --- Fun exclamations ---
    "wow": ("wazzoo", "amazement"),
    "awesome": ("awesomoo", "very good"),
    "oh no": ("ai-yai-yai", "distress"),
    "yay": ("yippadoo", "celebration"),
    "oops": ("oopsi-doo", "mistake"),
    "watch out": ("cuidado-zo", "warning"),
    "come on": ("vamoosh", "encouragement"),
    "let's go": ("vamoonow", "call to action"),
    "cheers": ("saludoo", "toast"),
    "congratulations": ("congratoolee", "celebrating achievement"),

    # --- Adjective extras ---
    "cute": ("cutoolee", "endearing"),
    "cool": ("coolzo", "impressive"),
    "weird": ("weirdoo", "strange"),
    "amazing": ("amazoolee", "impressive"),
    "boring": ("blahtoo", "dull"),
    "fun": ("funzo", "enjoyable"),
    "important": ("bigdealoo", "significant"),
    "difficult": ("hardzo", "tough"),
    "easy": ("easypoo", "simple"),
    "perfect": ("perfectoolee", "flawless"),
}

# Multi-word phrases checked BEFORE per-word translation
PHRASE_PRIORITY = [k for k in DICTIONARY if " " in k]
PHRASE_PRIORITY.sort(key=len, reverse=True)  # longest phrases matched first

# Reverse dictionary: minionese -> (english, note)
REVERSE_DICTIONARY = {v[0].lower(): (k, v[1]) for k, v in DICTIONARY.items()}