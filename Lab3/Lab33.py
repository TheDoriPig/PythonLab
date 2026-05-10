def outer(tmp):        # внешняя функция
 
    def inner(fname, sname):      # локальная функция
        return str.format(tmp, fname, sname)   
 
    return inner

print(outer("Уважаемый {}, {}! Вы делаете работу по замыканиям функций.")(input(), input())) #Вывод