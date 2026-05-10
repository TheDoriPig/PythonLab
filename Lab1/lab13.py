n = int(input())
nat = 1
while True:
    if nat * nat > n:
        print(nat)
        break
    nat += 1