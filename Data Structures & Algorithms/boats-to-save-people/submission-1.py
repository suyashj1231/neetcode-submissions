class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1

        people.sort()
        lightest = 0
        heavy = len(people) - 1
        boat = 0
        while lightest<=heavy:
            if people[lightest] + people[heavy] <= limit:
                lightest += 1
                heavy -= 1
            
            else:
                heavy -=1
            
            boat += 1

        return boat
            


