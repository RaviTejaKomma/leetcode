__author__ = 'Ravi Teja Komma'


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count1 = dict()
        count2 = dict()
        for i in s:
            count1[i] = count1.get(i, 0) + 1
        for i in t:
            count2[i] = count2.get(i, 0) + 1
        for i in count1:
            if count1[i] == count2.get(i, -1):
                continue
            else:
                return False
        for i in count2:
            if count2[i] == count1.get(i, -1):
                continue
            else:
                return False
        return True
