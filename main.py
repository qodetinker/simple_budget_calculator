# 50/30/20
# 50 = Needs
# 30 = wants
# 20 = Savings
needs           = 0.50
wants           = 0.30
saves           = 0.20


print(
    "This is a simple budget calculator based off the 50/30/20 rule" + "\n"
    "50 percent Needs" + "\n"
    "30 percent Wants" + "\n"
    "20 percent savings" + "\n"
    )

totalMonthlyNetPay = float(input("Please enter your total monthly pay:"))

print(
    "\n"
    "Here are your monthly totals" "\n"
    f"50 percent Needs {needs*totalMonthlyNetPay}" + "\n"
    f"30 percent wants {wants*totalMonthlyNetPay}" + "\n"
    f"20 percent savings {saves*totalMonthlyNetPay}"
    )