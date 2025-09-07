import platform

x = platform.system()
print(x)

x = dir(platform)
# print(x)

for item in x:
    print(item)
