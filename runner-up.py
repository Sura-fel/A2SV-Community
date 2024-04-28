if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    high = max(arr)
    runner = None
    for i in arr:
        if i != high and runner == None:
            runner = i
        elif runner == None:
            pass
        elif i>runner and i != high:
            runner = i
    print(runner)
