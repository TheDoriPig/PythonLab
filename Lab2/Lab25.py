things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300}
d = {}
while True:
    line = input()
    if not line:
        break
    pred, ves = line.split('=')
    d[pred] = int(ves)
things.update(d)
print(things)