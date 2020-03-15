def is_isogram(string):
    letters = [ch for ch in string.lower() if "a" <= ch <= "z"]
    
    return len(letters) == len(set(letters))
