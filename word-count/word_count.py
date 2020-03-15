from collections import Counter
import re


def count_words(sentence):
    cleaned = re.sub(r"\t|\n|:|!|@|#|\$|%|\^|&|,|\.| '|' |'$| \"|\" |_", ' ', sentence.lower())
    return Counter(cleaned.split())
