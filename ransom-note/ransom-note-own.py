from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransom = Counter(ransomNote)
        counter_magazine = Counter(magazine)
        for i in counter_ransom:
            if counter_ransom[i] > counter_magazine[i]:
                return False
        return True
