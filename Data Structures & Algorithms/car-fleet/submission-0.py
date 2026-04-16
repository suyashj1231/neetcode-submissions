class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[d,s] for d,s in zip(position,speed)]
        pair.sort(reverse=True)

        stack = []

        for d,s in pair:
            time = (target-d)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)            