# 判断一个数是否是偶数
def is_even(number):
    return number % 2 == 0

# 判断一个数是否是奇数
def is_odd(number):
    return number % 2 == 1  # 判断是否为奇数

if __name__ == "__main__":
    print("is_even(4):", is_even(4))  # 预期输出：True

