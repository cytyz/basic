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

# 第二种解法：摩尔投票法
# 摩尔投票法分为两个阶段：
# 对抗阶段：分属两个候选人的票数进行两两对抗抵消
# 计数阶段：计算对抗结果中最后留下的候选人票数是否有效
nums = [2, 2, 4, 2, 3, 6, 2]

# 对抗阶段
major = nums[0]
count = 0
for each in nums:
    if count == 0:
        major = each
    if each == major:
        count += 1
    else:
        count -= 1

# 统计阶段
if nums.count(major) > len(nums) / 2:
    print("主要元素是：", major)
else:
    print("不存在主要元素。")