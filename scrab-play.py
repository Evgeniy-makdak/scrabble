import random

#   Создаём переменные:
list_letter = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
               "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
list_numbers = [8, 2, 4, 2, 4, 8, 1, 1, 2, 5, 1, 4, 4, 3, 5, 10, 4, 5, 5, 5, 4, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2]
#----------------------------------------------------------------------------------------------------------------
#   Приветствие:
print("Привет.\nМы начинаем играть в Scrabble.\n\nКак зовут первого игрока?")
player_1 = input()
print("Как зовут второго игрока?")
player_2 = input()
print(f"{player_1} vs {player_2}\n(раздаю случайные буквы)")
#----------------------------------------------------------------------------------------------------------------
#   Реализуем случайную выборку 7 букв из list_letter:

list_1 = "".join(random.sample(list_letter, 7))
list_2 = "".join(random.sample(list_letter, 7))
print(player_1, "- буквы", list_1)
print(player_2, "- буквы", list_2)
#----------------------------------------------------------------------------------------------------------------
#   Выгружаем данные в список из файла russian_nouns.txt


#   эмуляция хода первого игрока:

while True:
    score_1 = 0
    count_letters_in_answer_1 = 0
    print("ходит", player_1)
    answer_1 = input(f"{player_1}, составь слово из предложенных букв : ")
    for letter in str(list_1):
        if (letter in answer_1):
            count_letters_in_answer_1 += 1
    if len(answer_1) == count_letters_in_answer_1:
        with open('russian_nouns.txt', encoding='utf-8') as fail:
            for symb in fail:
                if answer_1 == symb:
                    if len(answer_1) == 3:
                        score_1 += 3
                    elif len(answer_1) == 4:
                        score_1 += 6
                    elif len(answer_1) == 5:
                        score_1 += 7
                    elif len(answer_1) == 6:
                        score_1 += 8
                    print(f"Такое слово есть. {player_1} получает {score_1} баллов.")
                    break
                else:
                    new_letter = "".join(random.sample(list_letter, 1))
                    list_1 = list_1 + new_letter
                    print(f"Такого слова нет.\n{player_1} не получает очков.\nДобавляем букву "
                          f"{list_1}")
                    print(f"ход игрока {player_2}")
                    break

    else:
        new_letter = "".join(random.sample(list_letter, 1))
        list_1 = list_1 + new_letter
        print(f"Такого слова нет.\n{player_1} не получает очков.\nДобавляем букву "
              f"{list_1}")
        print(f"ход игрока {player_2}")
#----------------------------------------------------------------------------------------------------------------
#   эмуляция хода второго игрока:

    count_letters_in_answer_2 = 0
    score_2 = 0
    answer_2 = input(f"{player_2}, составь слово из предложенных букв : ")
    for letter in str(list_2):
        if (letter in answer_2):
            count_letters_in_answer_2 += 1
    if len(answer_2) == count_letters_in_answer_2:
        with open('russian_nouns.txt', encoding='utf-8') as fail:
            for symb in fail:
                if answer_2 == symb:
                    if len(answer_2) == 3:
                        score_2 += 3
                    elif len(answer_2) == 4:
                        score_2 += 6
                    elif len(answer_2) == 5:
                        score_2 += 7
                    elif len(answer_2) == 6:
                        score_2 += 8
                    print(f"Такое слово есть. {player_2} получает {score_2} баллов.")
                    break
                else:
                    new_letter = "".join(random.sample(list_letter, 1))
                    list_2 = list_2 + new_letter
                    print(f"Такого слова нет.\n{player_2} не получает очков.\nДобавляем букву "
                          f"{list_2}")
                    print(f"ход игрока {player_1}")
                    break

    else:
        new_letter = "".join(random.sample(list_letter, 1))
        list_2 = list_2 + new_letter
        print(f"Такого слова нет.\n{player_2} не получает очков.\nДобавляем букву "
              f"{list_2}")
#----------------------------------------------------------------------------------------------------------------        print(f"ход игрока {player_1}")