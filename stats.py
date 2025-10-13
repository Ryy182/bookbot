def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_to_sorted_list(chars):
    sorted_chars = []
    for c in chars:
        sorted_chars.append({"char" : c, "num": chars[c]})
        sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars

        