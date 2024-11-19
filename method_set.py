photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '480x240'}

photo_sizes.add('1024x768')
print(photo_sizes)

all_sizes = photo_sizes.union(other_sizes)
print(all_sizes)

common_s = photo_sizes.intersection(other_sizes)
print(common_s)

nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}
res = nums.issubset(other_nums)
print(res)