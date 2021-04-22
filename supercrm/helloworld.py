
# 字典按值比较, 按键打印
a = {1: 1, 2: 2}
sort_dict = sorted(a, key=lambda x: a[x], reverse=True)
print(sort_dict)