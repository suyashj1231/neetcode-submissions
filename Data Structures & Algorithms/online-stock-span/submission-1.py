class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        # consecutive days stock <= price always 1
        self.stocks.append(price)
        streak = 1
        curr = 0
        for i in reversed(self.stocks):
            if i <= price:
                curr +=1
            else:
                break
            streak = max(streak, curr)
        return streak


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)