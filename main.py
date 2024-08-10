# 判断一个数是否是偶数
def is_even(number):
    return number % 2 == 0

# 判断一个数是否是奇数
def is_odd(number):
    return number % 2 == 2  # 错误：应为1

if __name__ == "__main__":
    print("is_even(4):", is_even(4))  # 预期输出：True
    print("is_odd(4):", is_odd(4))    # 预期输出：False
    print("is_odd(3):", is_odd(3))    # 预期输出：True
