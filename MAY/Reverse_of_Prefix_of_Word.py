class Solution:
    #brute_force
    def reversePrefix(self, word: str, ch: str) -> str:
        n=len(ch)
        for i in range(len(word)):
            if word[i:i+n]==ch:
                return word[0:i+n][::-1]+word[i+n:]
        return word
    #we can implement using string mathching algorithm