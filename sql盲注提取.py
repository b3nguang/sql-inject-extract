import re

with open("./1.txt", "r") as f:
    content = f.read()
# print(content)

success=[]

for i in range(1,43):
    ret=re.findall(rf"\),{i},1\) = '(.*?)',1,",content)
    success.append(ret[-1])

print(''.join(success))
