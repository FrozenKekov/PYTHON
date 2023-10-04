salary = 6900
sale_veg = 0.7
cucumber= 90
tomato = 150
strawberry = 385
cookies = 140 + 140

buy = sale_veg * (5 * cucumber + tomato * 4) + cookies #сколько потратил
print(salary -buy)
print(f"у Вани было {salary} рублей {buy} рублей")
print(f"Осталось {salary-buy} рублей")

print(10//3)
print(10%3)

money = salary - buy
stock = 134
rate = 36
print(f"Ваня может купить {money // stock} акций")
print(f"Проезд стоит {rate} рублей, а у Вани остается {int(money % stock)} рублей")
