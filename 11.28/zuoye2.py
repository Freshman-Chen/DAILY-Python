# 原始列表
original_list = [8, 10, 2, 16, 14, 4, 6, 18, 12]

# 对列表进行排序
sorted_list = sorted(original_list)
print(f"排序后的列表: {sorted_list}")

# 插入数值15，保持列表有序
import bisect
bisect.insort(sorted_list, 15)
print(f"插入15后的列表: {sorted_list}")

# 删除列表中的10
sorted_list.remove(10)
print(f"删除10后的列表: {sorted_list}")
