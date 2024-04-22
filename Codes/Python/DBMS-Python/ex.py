class Solution:
    def productExceptSelf(self, nums):
        mul = 1
        #c = 0
        d = {0:0,1:0,2:2,3:1}
        for i in nums:
            print(i)
            if i == d[0]:
                print("hi")
                d[1] += d[3]
                if d[1] >= d[2]:
                    return [d[0]]*len(nums)
            else:
                mul *= i
        if d[1] == d[3]:
            return [(mul) if num == 0 else 0 for num in nums ]
        return [(mul // num) if num != 0 else mul for num in nums ]
    
print(Solution.productExceptSelf(0,[2,4,1,3,0,3,1]))