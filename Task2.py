#На вход программы поступает строка в формате:
#ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
#Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
#tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
#Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.

def create_tuple(kv_string):
    key_value_pairs = kv_string.split()
    tp = tuple(map(lambda kv: tuple(kv.split('=')), key_value_pairs))
    return tp

input_string = input("Введите строку в формате 'ключ=значение': ")
result_tuple = create_tuple(input_string)
print(result_tuple)
