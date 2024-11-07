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


nums = [34, 12, 45, 23, 8, 47, 50, 15, 29, 41, 33, 18, 77, 62, 3, 67, 90, 55, 22, 39]


def create_subList(nums):
    sublist = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
    return sublist

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    return sorted_list

def subList_sort(nums, sublist):
    sorted_sublists = [merge_sort(sub) for sub in sublist]
    return sorted_sublists

def main(nums):
    sublist = create_subList(nums)
    sorted_sublists = subList_sort(nums, sublist)
    print(sorted_sublists)

main(nums)