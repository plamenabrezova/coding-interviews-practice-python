from typing import List


def permute(nums: List[int]):
    def dfs(start_index, path):
        if start_index == len(nums):
            result.append(''.join(str(path)))
            return

        for number in nums:
            if number not in path:
                path.append(number)
                dfs(start_index + 1, path)
                path.pop()

    result = []
    dfs(0, [])

    return result

def permute_second(nums:List[int]):
    def backtracking(nums, path):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            backtracking(nums[:i] + nums[i+1:], path + [nums[i]])
    result = []
    backtracking(nums, [])
    return result


if __name__ == '__main__':
    input_nums = [1, 2, 3]
    #print(permute(input_nums))
    print(permute_second(input_nums))

    word = 'hello'
    print(word[::-1])
    print(word[:1])

    # example = ['obe', 'two', 'three', 'four']
    # print(example[::-1])