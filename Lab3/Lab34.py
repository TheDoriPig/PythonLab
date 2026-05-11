def decorator_factory(start):   #Декортатор функции
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            # Логика до вызова
            result = func(*args, **kwargs) + start
            # Логика после вызова
            return result
        return wrapper
    return real_decorator

@decorator_factory(5)   #Применение декоратора
def fun(chisla: str):
    ik = chisla
    sum = 0
    for i in ik:
        sum += int(i)
    return sum
op = input().split()
print(fun(op))