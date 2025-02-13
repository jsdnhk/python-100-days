"""
函數遞歸調用 - 函數直接或者間接的調用了自身
1. 收斂條件
2. 遞歸公式

n! = n * (n-1)!
f(n) = f(n-1) + f(n-2)
1 1 2 3 5 8 13 21 34 55 ...
"""
from contextlib import contextmanager
from time import perf_counter


def fac(num):
    """求階乘"""
    assert num >= 0
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


def fib2(num):
    """普通函數"""
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return a


def fib3(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# 動態規劃 - 保存可能進行重複運算的中間結果（空間換時間）
def fib(num, results={}):
    """斐波拉切數"""
    assert num > 0
    if num in (1, 2):
        return 1
    try:
        return results[num]
    except KeyError:
        results[num] = fib(num - 1) + fib(num - 2)
        return results[num]


@contextmanager
def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')


def main():
    """主函數"""
    # for val in fib3(20):
    #     print(val)
    # gen = fib3(20)
    # for _ in range(10):
    #     print(next(gen))
    for num in range(1, 121):
        with timer():
            print(f'{num}: {fib(num)}')
    # print(fac(5))
    # print(fac(-5))


if __name__ == '__main__':
    main()
