class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or "" in strs:
            return ""

        # use min amd max to find the strings to compare
        # min/max when applied to a list of strings
        # returns the lexographically largest or smallest valued strings
        # the minimum is the one that would be listed first in a dictionary order,
        # and the max is hte one that would be last

        # the insight here is that, amongst the min/max strings:
        # all common characters amongst the full list, must also be common characters amongst the min and max strings
        # any characters that differ between the smallest & largest will not be part of the common prefix

        s1 = min(strs)
        s2 = max(strs)

        #i is the index in the string, c is the character int he string
        for i, c in enumerate(s1):
            if c!= s2[i]:
                return s1[:i]
        return s1