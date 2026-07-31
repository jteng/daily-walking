"""Registry of all 66 Bible books (XML book@number, Chinese name, chapter
count) plus the ordered queue of books remaining for the chapter commentary
pilot after Luke/John/Acts/Romans (42-45, already fully drafted), and each
book's expositor voice per TIER1_SPEC.md's genre table.

Numbers match ChineseSimplifiedBible.xml's book@number and index.html's
Reader.bookMap, in standard 66-book canonical order.
"""

BOOKS = {
    1: ("创世记", 50), 2: ("出埃及记", 40), 3: ("利未记", 27), 4: ("民数记", 36),
    5: ("申命记", 34), 6: ("约书亚记", 24), 7: ("士师记", 21), 8: ("路得记", 4),
    9: ("撒母耳记上", 31), 10: ("撒母耳记下", 24), 11: ("列王纪上", 22), 12: ("列王纪下", 25),
    13: ("历代志上", 29), 14: ("历代志下", 36), 15: ("以斯拉记", 10), 16: ("尼希米记", 13),
    17: ("以斯帖记", 10), 18: ("约伯记", 42), 19: ("诗篇", 150), 20: ("箴言", 31),
    21: ("传道书", 12), 22: ("雅歌", 8), 23: ("以赛亚书", 66), 24: ("耶利米书", 52),
    25: ("耶利米哀歌", 5), 26: ("以西结书", 48), 27: ("但以理书", 12), 28: ("何西阿书", 14),
    29: ("约珥书", 3), 30: ("阿摩司书", 9), 31: ("俄巴底亚书", 1), 32: ("约拿书", 4),
    33: ("弥迦书", 7), 34: ("那鸿书", 3), 35: ("哈巴谷书", 3), 36: ("西番雅书", 3),
    37: ("哈该书", 2), 38: ("撒迦利亚书", 14), 39: ("玛拉基书", 4),
    40: ("马太福音", 28), 41: ("马可福音", 16), 42: ("路加福音", 24), 43: ("约翰福音", 21),
    44: ("使徒行传", 28), 45: ("罗马书", 16), 46: ("哥林多前书", 16), 47: ("哥林多后书", 13),
    48: ("加拉太书", 6), 49: ("以弗所书", 6), 50: ("腓立比书", 4), 51: ("歌罗西书", 4),
    52: ("帖撒罗尼迦前书", 5), 53: ("帖撒罗尼迦后书", 3), 54: ("提摩太前书", 6),
    55: ("提摩太后书", 4), 56: ("提多书", 3), 57: ("腓利门书", 1), 58: ("希伯来书", 13),
    59: ("雅各书", 5), 60: ("彼得前书", 5), 61: ("彼得后书", 3), 62: ("约翰一书", 5),
    63: ("约翰二书", 1), 64: ("约翰三书", 1), 65: ("犹大书", 1), 66: ("启示录", 22),
}

NAME_TO_NUMBER = {name: num for num, (name, _) in BOOKS.items()}

# Already fully drafted before this queue existed (drafted one-book-at-a-time
# via the old PILOT_BOOK_* scope in chapter_status.py, per CHAPTER_SPEC.md's
# history): 路加福音 (Luke, 42), 约翰福音 (John, 43), 使徒行传 (Acts, 44),
# 罗马书 (Romans, 45).
DONE_BOOKS = {42, 43, 44, 45}

# Order for finishing the rest of the Bible (user's explicit choice,
# 2026-07-31): finish the NT first — continue from where Romans left off
# (1 Corinthians through Revelation), then the two Gospels skipped when the
# pilot started with Luke (Matthew, Mark) — then the whole OT in canonical
# order, Genesis through Malachi.
QUEUE = list(range(46, 67)) + [40, 41] + list(range(1, 40))


def voice_for_book(number):
    """Expositor voice per TIER1_SPEC.md's genre table."""
    if number in (40, 41, 42, 43, 44):
        return "Carson + Ferguson"  # Gospels & Acts
    if number == 66:
        # Revelation isn't in TIER1_SPEC's table (apocalyptic, not epistle or
        # narrative) — MacArthur for doctrinal exposition, Motyer for the
        # prophetic/OT-echo dimension that dominates the book's imagery.
        return "MacArthur + Motyer"
    if 45 <= number <= 65:
        return "MacArthur + Sproul + Keller"  # Epistles (grace/doctrine)
    if number in (18, 19, 20, 21, 22):
        return "Kidner + Piper"  # Psalms & wisdom (Job, Psalms, Proverbs, Ecclesiastes, Song of Songs)
    if 23 <= number <= 39:
        return "Motyer"  # Prophets
    if 1 <= number <= 17:
        return "Kidner + Waltke"  # OT narrative
    raise ValueError(f"no voice mapping for book number {number}")
