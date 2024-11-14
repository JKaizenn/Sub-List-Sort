# 1. Name:
#      -Jessen Forbush-
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


def subListSort(nums):
    # Initialize the destination list with zeros
    destinationList = [0] * len(nums)
    destIndex = 0
    index = 0
    
    while index < len(nums):
        start = index
        end = findEndOfSorted(nums, start)
        
        # Sort the sublist from start to end
        sublist = nums[start:end + 1]
        sublist.sort()
        
        # Copy the sorted sublist to the destination list
        for i in range(len(sublist)):
            destinationList[destIndex] = sublist[i]
            destIndex += 1
        
        # Move to the next sublist
        index = end + 1
    
    return destinationList


def findEndOfSorted(nums, start):
    end = start
    while end < len(nums) - 1 and nums[end] >= nums[end + 1]:
        end += 1
    return end


def main():
    nums = [34, 12, 45, 23, 8, 47, 50, 15, 29, 41, 33, 18, 77, 62, 3, 67, 90, 55, 22, 39]
    sorted_list = subListSort(nums)
    print("Sorted list:", sorted_list)
    
if __name__ == "__main__":
    main()
