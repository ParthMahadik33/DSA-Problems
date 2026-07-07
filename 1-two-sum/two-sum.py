from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map=defaultdict(list)
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in map.keys():
                return [map.get(x),i]
            else:
                map[nums[i]]=i    

        