class FreqStack:

    def __init__(self):
        self.stacks = {} # 1 -> [], 2-> []... # are the groups
        self.cnt = {} # count of each variable
        self.maxcnt = 0 # max cnt in that stack

    def push(self, val: int) -> None:
        valuecount = 1 + self.cnt.get(val,0)
        self.cnt[val] = valuecount
        if valuecount > self.maxcnt:
            self.maxcnt = valuecount
            self.stacks[valuecount] = []
        self.stacks[valuecount].append(val)

    def pop(self) -> int:
        ans = self.stacks[self.maxcnt].pop()
        self.cnt[ans] -= 1
        if len(self.stacks[self.maxcnt]) == 0:
            self.maxcnt -=1
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()