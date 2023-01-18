__author__ = 'Ravi Teja Komma'


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        frequency = dict()
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
            if frequency[num] > 1:
                return True
        return False
