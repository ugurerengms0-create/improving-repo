#Week 1 Studies and Week03 (Loops) and Week 4 (Functions) Integration #Week 2 Studies if,elif, else, logical operators, comparison operators
#f-string, variables, operators etc..(week1)

def calculate_budget(daily_money):
        while True:
            money = float(input("Enter your daily money:"))
            if money < 0:
                print("Money cannot be negative. Please enter a valid amount.")
            else:
                break
        weekly_money = money*7
        monthly_money = money*30
        yearly_money = money*365
        return weekly_money, monthly_money, yearly_money
def budget_analysis(yearly_money):
    print("-"*30)
    print("Bütçe Analizi")
    if yearly_money >= 100000:
        print("Durum: Lüks Sınıf 🚀 (Yıllık bütçen gayet yüksek!)")
    elif yearly_money >= 50000 and yearly_money < 100000:
        print("Durum: Orta Sınıf 🚗 (Yıllık bütçen orta seviyede.)")
    else:
        print("Durum: Fakir Sınıf 🐻 (Yıllık bütçen düşük.)")

name = input("Enter your name:").capitalize().strip()
while True:
    age = int(input("Enter your age:"))
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    else:
        break

while True:
    money = float(input("Enter your daily money:"))
    if money < 0:
        print("Money cannot be negative. Please enter a valid amount.")
    else:
        break

weekly_money, monthly_money, yearly_money = calculate_budget(money)
budget_analysis(yearly_money)
print(f"Hello {name}. Your informations are showed in the table.")
print("-*"*30)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"\nWeekly Money: {weekly_money:.2f} TRY")
print(f"Monthly Money: {monthly_money:.2f} TRY")
print(f"Yearly Money: {yearly_money:.2f} TRY")

