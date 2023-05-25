#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
#Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
#Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
#Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
#Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке


def check_rhythm(poem):
    lines = poem.split(" ")
    syllables_count = None

    for line in lines:
        words = line.split("-")
        line_syllables_count = sum(count_syllables(word) for word in words)
        if syllables_count is None:
            syllables_count = line_syllables_count
        elif syllables_count != line_syllables_count:
            return "Пам парам"
    
    return "Парам пам-пам"

def count_syllables(word):
    vowels = "аеёиоуыэюя"
    count = 0
    previous_char = None

    for char in word:
        if char.lower() in vowels:
            if previous_char is None or previous_char.lower() not in vowels:
                count += 1
        previous_char = char
    
    return count

poem = input("Введите стихотворение ")
result = check_rhythm(poem)
print(result)
