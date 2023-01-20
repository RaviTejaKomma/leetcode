__author__ = 'Ravi Teja Komma'


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalpha():
                start += 1
            elif not s[end].isalpha():
                end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True