import random

print("Вітаю у грі 'Вгадай число'!")
nickname = input("Введіть ваш нікнейм: ")
print(f"Привіт, {nickname}! Я загадав число від 1 до 50. Спробуй вгадати!")

secret_number = random.randint(1, 50)

while True:
    guess = input("Ваш варіант: ")

    if not guess.isdigit():
        print("Помилка: потрібно вводити лише число! Спробуйте ще раз.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Більше!")
    elif guess > secret_number:
        print("Менше!")
    else:
        print(f"Вітаю, {nickname}! Ви вгадали число {secret_number}!")
        break
print("дякую за гру!")
#print(f"К-сть зіграних раундів: {len(game_history)}")