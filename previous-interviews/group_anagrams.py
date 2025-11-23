from typing import List

def group_anagrams(strs: List[str]):
   anagram_map = dict()

   for word in strs:
       sorted_word = ''.join(sorted(word))
       anagram_map.setdefault(sorted_word, []).append(word)

   return anagram_map.values()

if __name__ == '__main__':
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
