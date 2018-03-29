# 取出 lst 的第二个位置至倒数第二个位置的子串
# 创建为一个新列表 lst2
lst = [1, 2, 3, 5, 8, 13, 22]
lst2 = lst[1:-1]
print(lst2)

lst1 = [1, 2, 3, 5, 8, 13, 22]
# 将lst1中的每一项都乘以2，生成新的列表lst2
lst2 = [i * 2 for i in lst1]
print(lst2)

s = "a b c e d"
ls = s.split()
print(s)
print(ls)

s1 = '||'.join(ls)
print(ls)
print(s1)

print('aaa'.split('a'))

# 把1-100的整数里，能被2,3,5同时整除的数取出，用;分隔的形式输出
# 写法1：
result = []
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        result.append(str(i))
print(';'.join(result))

# 写法2：
result1 = ';'.join([str(i) for i in range(1, 101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])
print(result1)


# 写法3：
def is_mod_by_235(i):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        return True
    else:
        return False


result2 = ';'.join([str(i) for i in range(1, 101) if is_mod_by_235(i)])
print(result2)


# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
# 给定一个整数数列，找出其中和为特定值的那两个数。
#
# 你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


t = Solution()
a = []
a = t.two_sum([2, 7, 11, 15], 9)
print(a)

# 这个算法效率不高??。。。