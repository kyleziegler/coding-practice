# create virtual env
# virtualenv -p /usr/bin/python3 py3
# Activate
# source py3/bin/activate   


class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:

        runningList = []
        maxseqlength = 0
        charList = [c for c in s]
        if(len(charList) == 0):
            return 0
#         iterate through each char and try to create a long string
        for c in charList:
            print("on list charactuer:",c)
            if (len(runningList) == 0):
                runningList.append(c)
            else:
                temp = []
                for a in runningList:
                    # print("Is %s in the runningList?" %c)
                    # print("List:", runningList)
                    # print("Working chars:",a,c)
                    # We've reached a duplicate
                    if (a == c):
                        if (len(runningList) > maxseqlength):
                            maxseqlength = len(runningList)
                        runningList.clear()
                        break;
                    # This is a new character, but dont add it to the list we are working on
                    else:
                        print("Add char %c to the list" %c)
                        runningList.append(c)
                runningList+=temp
                temp.clear()
                print(runningList)
                print(maxseqlength)
        return maxseqlength

print("Result 1: ", Solution().lengthOfLongestSubstring(s='pwwkew'))
# print("Result 2: ", Solution().lengthOfLongestSubstring(s='aaabaabcabc'))
# print("Result 3: ", Solution().lengthOfLongestSubstring(s=''))
                    
                    