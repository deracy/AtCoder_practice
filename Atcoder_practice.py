while True:

    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break

    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                if j % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
            
        else:
            for t in range(W):
                if t % 2 == 0:
                    print(".", end="")
                else:
                    print("#", end="")
            print()
            
    print()
    

    