class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(0,len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]]=i
        return False       
            