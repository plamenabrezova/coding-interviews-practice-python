def is_valid_anagram(str1: str, str2: str) -> bool:
    return True if sorted(str1) == sorted(str2) else False

string1 = 'hello'
happyPath = 'oellh'
sadPath = 'world'
print(is_valid_anagram(string1, happyPath))
print(is_valid_anagram(string1, sadPath))