class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, jleft, kright = L, 0, 0 

            while jleft < len(left) and kright < len(right):
                if left[jleft] <= right[kright]:
                    arr[i] = left[jleft]
                    jleft+=1
                else:
                    arr[i] = right[kright]
                    kright+=1
                i += 1
            
            while jleft < len(left):
                arr[i] = left[jleft]
                jleft+=1
                i+=1
            while kright < len(right):
                arr[i] = right[kright]
                kright+=1
                i+=1

        
        def mergeSort(arr, L, R): # recurisve 
            if L >= R:
                return
            M = (L + R) // 2
            mergeSort(arr, L, M) # left 
            mergeSort(arr, M + 1, R) # right
            merge(arr, L, M, R)

        mergeSort(nums, 0, len(nums) - 1)
        return nums


# merge sort

# time: O(nlogn)
# space: O(n)


