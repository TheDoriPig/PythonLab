chisla = list(map(int, input().split()))
vivod = "Отчислен" if (chisla.count(2) + chisla.count(1)) > 1 else "Учится"
print(vivod)