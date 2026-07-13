class TimeMap:

   def __init__(self):
      self.store = {}
    
        

   def set(self, key: str, value: str, timestamp: int) -> None:
      if key not in self.store:
            self.store[key] = []
      self.store[key].append([value, timestamp])


   def get(self, key: str, timestamp: int) -> str:
      ans = ""
      index = self.store.get(key,[])
      
      l = 0
      r = len(index) - 1

      while l <= r:
         m = l + (r-l) // 2
         
         if index[m][1] < timestamp:
            ans = index[m][0]
            l = m + 1
   
         elif index[m][1] > timestamp:
            r = m - 1
         
         else:
            ans = index[m][0]
            return ans
      
      return ans

