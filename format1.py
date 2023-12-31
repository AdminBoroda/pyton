foo = 1  # Задаем значения переменных
bar = 'bar'  # Задаем значения переменных
baz = 3.14  # Задаем значения переменных
print('{}, {} and {}'.format(foo, bar, baz)) # Пары в скобках заменяются аргументами в порядке их передачи "1, bar and 3.14"
print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz)) # Номера соответствуют индексам аргументов : "1, bar, 3.14, and bar" 
print('{2}, {0}, {2}, and {1}'.format(foo, bar, baz)) # Номера соответствуют индексам аргументов 
#print('{0}, {1}, {2}, and {3}'.format(foo, bar, baz))  выдает ошибку так как индекс 3 не существует
print("X value is: {xx}. Y value is: {yyl}.".format(xx=2, yyl=3)) # Можно использовать именованные аргументы 
# аргументы по умолчанию                                                                                                                                                                                 print("Hello {}, your balance is {}.".format("Adam", 230.2346)) 
 # позиционные аргументы                                                                                                                                                                                      print("Hello {0}, your balance is {1}.".format("Adam", 230.2346)) 
 # аргументы ключевые слова                                                                                                                                                                                print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346)) 
 # смешанные аргументы                                                                                                                                                                                       print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))
print('{:~^20}'.format('centered')) #вы можете также включать в спецификацию формата внутри фигурных скобок.                                                                                           #Это выражение , которое следует , и особые правила должны предшествовать двоеточие ( : ).                                                                      # :~^20 ( ^ означает выравнивание по центру, общая ширина 20, подстановка символа ~ )

# целочисленные аргументы
print("The number is:{:d}".format(123))

 # аргументы с плавающей точкой
print("The float number is:{:f}".format(123.4567898))

 # восьмеричный, двоичный и шестнадцатеричный формат
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

# целые числа с выравниванием по правому краю
print("{:5d}".format(12))

 # числа с плавающей точкой с выравниванием по центру
print("{:^10.3f}".format(12.2346))

 # выравнивание целого числа по левому краю заполнено нулями
print("{:<05d}".format(12))

 # числа с плавающей точкой с выравниванием по центру
print("{:=8.3f}".format(-12.2346))

# показать знак +
print("{:+f} {:+f}".format(12.23, -12.23))

 # показать знак -
print("{:-f} {:-f}".format(12.23, -12.23))
 # показать место для знака +
print("{: f} {: f}".format(12.23, -12.23))
# отступ строки с выравниванием по левому краю
print("{:5}".format("cat"))
 # отступ строки с выравниванием по правому краю
print("{:>5}".format("cat"))
 # заполнение строк с выравниванием по центру
print("{:^5}".format("cat"))
 # заполнение строк с выравниванием по центру # и '*' - символ заполнения
print("{:*^5}".format("cat"))
