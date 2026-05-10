tak = set()
while True:
    line = input()
    if not line:
        break
    name = line.split(':')[0]
    tak.add(name.strip())
print(len(tak))