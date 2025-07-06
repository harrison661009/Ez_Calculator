def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("簡易計算機")
    print("選擇運算：")
    print("1. 加法")
    print("2. 減法")
    print("3. 乘法")
    print("4. 除法")

    choice = input("請輸入選項 (1/2/3/4): ")

    num1 = float(input("輸入第一個數字: "))
    num2 = float(input("輸入第二個數字: "))

    if choice == '1':
        print("結果：", add(num1, num2))
    elif choice == '2':
        print("結果：", subtract(num1, num2))
    elif choice == '3':
        print("結果：", multiply(num1, num2))
    elif choice == '4':
        print("結果：", divide(num1, num2))
    else:
        print("無效的輸入")

if __name__ == "__main__":
    main()