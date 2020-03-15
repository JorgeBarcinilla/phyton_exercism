import re

def abbreviate(words):
    acronym = ''
    for word in re.split('\s|-', words):
        match = re.search('[a-zA-Z]', word)
        if match:
            acronym += match.group(0).upper()
    return acronym
