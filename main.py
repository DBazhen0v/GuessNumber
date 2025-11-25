import random

def play_game():
    secret_number = random.randint(1, 50)
    attempts = 0
    guesses = []

    print("Я загадав число від 1 до 50. Спробуй його відгадати!")

    while True:
        user_i = input("Введи свій варіант: ")


        if not user_i.isdigit():
            print("Помилка! Потрібно вводити тільки числа.")
            continue

        g = int(user_i)
        attempts += 1
        guesses.append(g)

        if g < secret_number:
            print("Моє число більше!")
        elif g > secret_number:
            print("Моє число менше!")
        else:
            print(f"Вітаю! Ти вгадав число {secret_number} за {attempts} спроб(и)!")
            print(f"Твої спроби: {guesses}")
            return attempts

print("Вітаю у грі 'Вгадай число'!")
nickname = input("Введи свій нікнейм: ")
print(f"Привіт, {nickname}! Почнемо гру!")

all_attempts = []

while True:
    at = play_game()
    all_attempts.append(at)

    print(f"Статистика спроб по раундах: {all_attempts}")
    print(f"Найкращий результат: {min(all_attempts)} спроб(и)")

    play_again = input("Хочеш зіграти ще раз? (так/ні): ")
    if play_again not in ("так", "taк", "yes", "y"):
        print(f"Дякую за гру, {nickname}! Побачимось!")
        break