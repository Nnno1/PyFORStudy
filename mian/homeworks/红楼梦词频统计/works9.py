from jieba import lcut
txt=open("红楼梦.txt",'r',encoding='utf-8').read()
words=lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    if word in ["林黛玉", "黛玉", "颦儿", "林妹妹", "潇湘妃子","绛珠仙子","林姑娘"]:
        name="林黛玉"
    elif word in ["薛宝钗", "宝钗", "宝姐姐", "蘅芜君"]:
        name="薛宝钗"
    elif word in ["贾元春", "元春", "贵妃"]:
        name="贾元春"
    elif word in ["贾探春", "探春", "三姑娘",]:
        name="贾探春"
    elif word in ["史湘云", "湘云", "云妹妹"]:
        name="史湘云"
    elif word in ["妙玉", "槛外人"]:
        name="妙玉"
    elif word in ["贾迎春", "迎春", "二姑娘"]:
        name="贾迎春"
    elif word in ["贾惜春", "惜春", "四姑娘"]:
        name="贾惜春"
    elif word in ["王熙凤", "凤姐", "琏二奶奶","凤辣子"]:
        name="王熙凤"
    elif word in ["巧姐", "大姐儿"]:
        name="巧姐"
    elif word in ["李纨", "大嫂子"]:
        name="李纨"
    elif word in ["秦可卿", "可卿"]:
        name="秦可卿"
    else:
        continue
    counts[name]=counts.get(name,0)+1
items=sorted(counts.items(),key=lambda x:x[1],reverse=True)
for name,count in items:
    print(f"{name:<10}{count:>5}")