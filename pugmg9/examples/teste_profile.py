def main():
    print(fib(25))


def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    main()
