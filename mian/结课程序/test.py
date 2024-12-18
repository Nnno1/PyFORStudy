import os
file_path = 'your_file_path.csv'
if os.path.exists(file_path):
# 文件存在，可以进行读取操作
df = pd.read_csv(file_path)
else:
print('文件不存在')