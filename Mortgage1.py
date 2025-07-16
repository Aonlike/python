principal = int(input("Enter principal amount: "))

rate = float(input("Enter rate: "))


duration = float(input("Enter duration of the loan: "))

duration1 = duration * 12

monthly_rate = rate / 12 /100

monthly_payment = monthly_rate * (1 + monthly_rate)**duration1


denominator = (1 + monthly_rate)**duration1
denominator1 = denominator - 1

monthly_payment2 = (monthly_payment) / denominator1


monthly_mortgage = monthly_payment2 * principal

print(monthly_mortgage)
