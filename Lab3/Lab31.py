def stroka(string):
    return len(string) >= 3
icity = input().split()
fcity = [city for city in icity if stroka(city)]
print(fcity)