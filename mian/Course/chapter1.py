
'''
zb1,zb2=input(),input()
x1,y1=float(zb1[0:1]),float(zb1[2:3])
x2,y2=float(zb2[0:1]),float(zb2[2:3])
distance=pow((x1-x2)**2+(y1-y2)**2,0.5)
print(f'两点间的距离为{distance:.2f}')
'''

plaintext = input("请输入明文：")

# 加密过程，每个字符ASCII码转换为数字，加3后取模，再转回字符
ciphertext = ''.join([chr(((ord(c) - ord('0') + 3) % 10) + ord('0')) for c in plaintext])
print(f"密文：{ciphertext}")

# 解密过程，每个字符减3后取模，恢复原文
decrypted = ''.join([chr(((ord(c) - ord('0') - 3) % 10) + ord('0')) for c in ciphertext])
print(f"原文：{decrypted}")



def encrypt(plaintext):
    # 加密过程，每个字符ASCII码转换为数字，加3后取模，再转回字符
    ciphertext = ''
    for c in plaintext:
        encrypted_char = chr((ord(c) - ord('0') + 3) % 10 + ord('0'))
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext):
    # 解密过程，每个字符减3后取模，恢复原文
    decrypted = ''
    for c in ciphertext:
        decrypted_char = chr((ord(c) - ord('0') - 3) % 10 + ord('0'))
        decrypted += decrypted_char
    return decrypted

plaintext = input("请输入明文：")
ciphertext = encrypt(plaintext)
print(f"密文：{ciphertext}")

decrypted = decrypt(ciphertext)
print(f"原文：{decrypted}")

