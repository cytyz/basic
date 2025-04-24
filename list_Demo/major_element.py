# 主要元素
# 如果有一个列表，其中占比超过一半的元素称之为主要元素，那么如何获取一个列表的主要元素呢？
nums = [2, 2, 4, 2, 3, 6, 2]
nums.sort()
major = nums[len(nums) // 2]
major_num = 0
for i in nums:
    if i == major:
        major_num += 1
if major_num >= (len(nums) // 2):
    print(major, "为主要元素")
else:
    print("不存在主要元素")
