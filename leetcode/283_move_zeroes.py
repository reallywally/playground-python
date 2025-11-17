from typing import List


def moveZeroes(nums: List[int]) -> None:
    left = 0  # 0이 아닌 원소를 배치할 위치

    # 배열을 순회하면서
    for right in range(len(nums)):
        if nums[right] != 0:
            # 0이 아닌 원소를 찾으면 left 위치와 swap
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


test_case_list = [
    [0, 1, 0, 3, 12],
    [0]
]

for test_case in test_case_list:
    moveZeroes(test_case)
