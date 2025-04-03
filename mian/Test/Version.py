import sys
print(sys.version)



a=input()
if a.isalpha():
    print("letter")
elif a.isdigit():
    print("digit")
elif a.isspace():
    print("space")
else:
    print("other")