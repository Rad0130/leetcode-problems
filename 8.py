class Solution(object):
    def twoSum(self, nums, target):

        lst=[]

        if len(nums)>2:
            for i in range(len(nums)):
                for j in range(1, len(nums)):
                    if i!=j:
                        if nums[i]+nums[j]==target:
                            lst=[i,j]
                            break
                if lst!=[]:
                    break
                else:
                    continue
                
        else:
            lst=[0,1]

        return lst


nums=[2,5,5,11]
target=10
obj=Solution()
output=obj.twoSum(nums, target)
print(output)
