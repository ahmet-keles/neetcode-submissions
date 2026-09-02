class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {num: i for i, num in enumerate(nums)}

        for first_index in range(len(nums)):
            remain = target - nums[first_index]
            if remain in my_dict and my_dict[remain] != first_index:
                second_index = my_dict[remain]
                return [first_index, second_index]
        