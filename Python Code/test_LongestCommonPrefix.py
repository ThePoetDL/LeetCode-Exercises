from LongestCommonPrefix import Solution

s = Solution()

def test_longestCommonPrefix():
    listStrsA = ["flower","flow","flight"]
    listStrsB = ["dog","racecar","car"]
    listStrsC = [""]

    assert s.longestCommonPrefix(listStrsA) == "fl"
    assert s.longestCommonPrefix(listStrsB) == ""
    assert s.longestCommonPrefix(listStrsC) == ""