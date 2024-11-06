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




nums = [12, 4, 5, 6, 7, 43, 3, 9, 1, 11, 34, 76, 98, 4, 23, 45, 67, 89, 10, 72]



"""Create SubLists from the list of 20 numbers"""
def create_subList(nums):
    sublist = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
    print(sublist)



def main(nums):
    create_subList(nums)

main(nums)
