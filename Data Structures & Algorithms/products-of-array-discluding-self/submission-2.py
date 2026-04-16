class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = pre * nums[i]
        
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post = post * nums[i]
        
        return res


        
        
        # pre = [1]
        # post = []
        # mul = 1
        # ans=[]
        # for i in range(len(nums)):
        #     mul = mul * nums[i]
        #     pre.append(mul)
        # print(pre)
        # mul = 1
        # for i in range(len(nums)-1,-1, -1):
        #     mul = mul * nums[i]
        #     post.append(mul)
        # post = post[::-1]
        # post.append(1)
        # print(post)

        # for i in range(len(nums)):
        #     ans.append(pre[i]*post[i+1])
        # return ans



\

        