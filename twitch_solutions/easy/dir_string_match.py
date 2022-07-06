class Solution(object):

    def transform(self, ans, plus):
        add = 0
        for i in range(len(plus) - 1):
            ans[i] = ans[i] + add
            add += plus[i] 
        return ans



    def diStringMatch(self, s):
        used = set()
        used.add(0)
        ans = list()
        plus = list()
        ans.append(0)
        plus.append(0)
        prev = 0
        for c in s:
            if c == "D":
                next_num = ans[-1] + 1
                ans.append(next_num)
                if next_num in used:
                    plus.append(1)
                else:
                    plus.append(0)
            else:   # if c == "I"     
                next_num =  ans[-1] - 1
                ans.append(next_num)
                if next_num in used:
                    if len(plus) > 1:
                        plus[-2] += 1
                    plus.append(0)
            prev = next_num
        return self.transform(ans, plus)
                        