class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer, end_pointer = 0, len(numbers) - 1

        while start_pointer <= end_pointer:
            total = numbers[end_pointer] + numbers[start_pointer]

            if total == target:
                return [start_pointer + 1, end_pointer + 1]
            elif total < target:
                start_pointer+=1
            elif total > target:
                end_pointer -= 1
            
        

# increasing order
# index1 < index and can not be equal 
# valid solution always 
# O(1) space
# 1 indexed --> starts at 1

# basically 2 sum but 1-indexed 

# brute:  hashmap ( n / n)
# optimal:converging 2 pointer ( n / 1)

# pointer_1 = 0, pointer_2 = len(numbers) -1 
# if numbers[pointer_2] - numbers[pointer_1] = target
    # return [pointer_1, pointer_2]
# elif numbers[pointer_2] - numbers[pointer_1] < target
    # increment pointer 1
# elif numbers[pointer_2] - numbers[pointer_1] > target
    # decerement pointer 2
