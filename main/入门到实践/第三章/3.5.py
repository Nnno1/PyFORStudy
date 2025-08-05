name=['张恒溢','杨智文','张艺潇']
for i in range(3):
    print(f'来吃晚餐，{name[i]}！')
print(f'can not arrive {name[2]}')
name[2]='None'
for i in range(3):
    print(f'来吃晚餐，{name[i]}！')