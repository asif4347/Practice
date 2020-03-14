arr = ['dog', 'deer', 'deal']
str = 'de'
new_strs = [x for x in arr if x.__contains__(str)]
print(new_strs)

# new_strs = []
# for x in arr:
#     if x.__contains__(str):
#         new_strs.append(x)
#
# print(new_strs)
