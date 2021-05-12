import random

carts = {
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    2: "В",
    3: "Д",
    4: "К",
    11: "Т"
}

def rndCart (p):
    cartsn = [ cart for cart in carts.keys()]
    cart = random.choice(cartsn)
    p.append(cart)
    p.append(carts[cart])


print("Игра 21")
print("Игра с компьютером")
is_answer = random.choice([True, False])


def log_bot(b, p):
    score_b = b
    score_p = p
    if score_b > score_p:
        return
    elif score_b <= score_p:
        return rndCart(bot)



def player_cart(p):
    sum_pl = sum([i for i in p if isinstance(i, int)])
    pl = [i for i in p if isinstance(i, str)]
    return [pl, sum_pl]

while 1:
    print("Готовы играть? (y/n)")
    key = input().upper()
    if key == "Y":
        bot = []
        player = []
        rndCart(player)
        rndCart(player)

        rndCart(bot)
        rndCart(bot)

        while True:
            print("Ваши карты")
            print(player_cart(player)[0], player_cart(player)[1])
            print("Карты бота")
            print(player_cart(bot)[0], player_cart(bot)[1])
            if player_cart(bot)[1] == 21 and player_cart(player)[1] == 21:
                print("Ничья")
                break
            if player_cart(bot)[1] == 21 or player_cart(player)[1] > 21:
                print("Win Bot")
                break
            elif player_cart(player)[1] == 21 or player_cart(bot)[1] > 21:
                print("Win You")
                break
            else:
               n = player_cart(player)[1]
               b = player_cart(bot)[1]
               print('Карту берешь? (y/n)')
               answer = input().upper()
               if answer == "Y":
                   rndCart(player)
                   log_bot(b, n)
               elif answer == "N":
                   log_bot(b, n)

    else:
        print("Пока")
        break