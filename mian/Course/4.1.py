try:
    # Safely evaluate input and convert to number
    user_input = input("请输入一个数字: ")
    number = float(user_input)  # Convert to float to handle both integers and decimals
    hex_value = hex(int(number))  # Convert to integer first, then to hex
    print(f'{number} 对应的十六进制数为 {hex_value}')
except ValueError:
    print("输入无效，请输入一个有效的数字")
