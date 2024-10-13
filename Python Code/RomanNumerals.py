class solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        :return:
        """

        # dictionary converting roman characters to numbers
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            #Case for IV, XL, XC, CD, CM, etc.
            #See if nth character is bigger than (n-1)th character, in which case you need to calculate its value specially
            #The reason you need to multiply by two is that, in the prior iteration of the loop, you've already added the (n-1)th number
            #So you need to substract out the nunber twice (i.e., for IX you need +10, -2*(1)
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                result += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                result += roman[s[i]]
        return result

