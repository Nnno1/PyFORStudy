#Version1
'''
import jieba as j
txt=open('D:\\PyFORStudy\\mian\\homeworks\\红楼梦.txt','r',encoding='utf-8').read()
words = j.lcut(txt)
counts = {'林黛玉':0,'薛宝钗':0,'贾元春':0,'贾探春':0,'史湘云':0,'妙玉':0,'贾迎春':0,'贾惜春':0,'王熙凤':0,'巧姐':0,'李纨':0,'秦可卿':0}
for word in words:
    if word in counts:
        counts[word] += 1
statistics=sorted(counts.items(), key=lambda x:x[1], reverse=True)
print(statistics)
'''
#Version2

import jieba as j

# 一、称谓扩展（核心优化）
character_map = {
'林黛玉': ['林黛玉', '黛玉', '林妹妹', '颦儿', '潇湘妃子'],
'薛宝钗': ['薛宝钗', '宝钗', '宝姑娘', '蘅芜君', '宝姐姐'],
'王熙凤': ['王熙凤', '凤姐', '凤辣子', '琏二奶奶', '凤哥儿', '凤丫头'],
'贾元春': ['贾元春', '元春', '贵妃娘娘'],
'贾探春': ['贾探春', '探春', '三姑娘', '玫瑰花'],
'史湘云': ['史湘云', '湘云', '云丫头', '史大姑娘'],
'妙玉': ['妙玉', '槛外人', '畸人'],
'贾迎春': ['贾迎春', '迎春', '二姑娘', '二木头'],
'贾惜春': ['贾惜春', '惜春', '四姑娘'],
'巧姐': ['巧姐', '大姐儿'],
'李纨': ['李纨', '珠大嫂子', '宫裁', '稻香老农'],
'秦可卿': ['秦可卿', '可卿', '蓉大奶奶']
}

# 二、自定义词典增强分词精度
j.load_userdict('mian\\homeworks\\1.txt') # 需创建包含所有称谓的词典文件

# 三、建立反向映射（提升检索效率）
reverse_mapping = {}
for main_name, aliases in character_map.items():
    for alias in aliases:
        reverse_mapping[alias] = main_name

# 四、优化文本预处理
txt=open('mian\\homeworks\\红楼梦.txt','r',encoding='utf-8').read()
excludes = {'，','。','？','！','……','‘','’','“','”','（','）','：','；','\n'}
words = j.lcut(txt)
words_clean = [word.strip() for word in words if word not in excludes]

# 五、多重统计逻辑
counts = {name:0 for name in character_map.keys()}
for word in words_clean:
    if word in reverse_mapping:
        main_name = reverse_mapping[word]
        counts[main_name] += 1

statistics = sorted(counts.items(), key=lambda x:x[1], reverse=True)
print(statistics)
'''
[('林黛玉', 1442), ('王熙凤', 1316), ('薛宝钗', 977), 
('贾探春', 436), ('史湘云', 419), ('李纨', 369),
('贾惜春', 226), ('妙玉', 154), ('贾迎春', 145),
('巧姐', 62), ('贾元春', 22), ('秦可卿', 15)]
'''