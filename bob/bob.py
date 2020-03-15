import re


def is_question(phrase):
    """Returns whether a phrase is a question."""
    return phrase.strip().endswith('?')


def is_yelling(phrase):
    """Returns whether a phrase is a yelling sentence."""
    return phrase.isupper()


def is_saying_nothing(phrase):
    """Returns whether a phrase is not saying anything."""
    return re.match(r'^\s*$', phrase)


def response(hey_bob):
    if is_question(hey_bob) and is_yelling(hey_bob):
        reply = "Calm down, I know what I'm doing!"
    elif is_question(hey_bob):
        reply = "Sure."
    elif is_yelling(hey_bob):
        reply = "Whoa, chill out!"
    elif is_saying_nothing(hey_bob):
        reply = "Fine. Be that way!"
    else:
        reply = "Whatever."

    return reply
