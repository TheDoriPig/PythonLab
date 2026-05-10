info = input("Введите данные в формате \"Имя, возраст, группа, список оценок\": ").split()
name = info[0]
age = info[1]
group = info[2]
num = info[3:8]
res = [name, age, group, num]
print(res)