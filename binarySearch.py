# Implementing a binary search algorithm

def binary_search(target, nums):
    """
    Function returns true if target is in nums
    Else returns false
    
    """

    floor_index = -1
    ceiling_index = len(nums)
    
    while floor_index + 1 < ceiling_index:

        distance = ceiling_index - floor_index
        half_distance = distance / 2
        guess_index = floor_index + half_distance

        guess_Value = nums[guess_index]

        if target == guess_Value:
            return True
        
        if guess_Value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return False