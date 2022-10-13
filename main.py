# 50/30/20
# 50 = Needs
# 30 = wants
# 20 = Savings
# needs           = 0.50
# wants           = 0.25
# saves           = 0.25


class Budget:
    def __init__(self, total_take_home):
        self.needs = total_take_home * .5
        self.wants = total_take_home * .3
        self.save = total_take_home * .2
        needs = self.needs
        wants = self.wants
        save = self.save
        print("\n"
              "Here are your monthly totals"
              "\n"
              f"50 percent Needs {int(needs)}" + "\n"
              f"30 percent wants {int(wants)}" + "\n"
              f"20 percent savings {int(save)}")

        print("\n"
              "Here are your weekly totals"
              "\n"
              f"50 percent Needs {int(needs / 4)}" + "\n"
              f"30 percent wants {int(wants / 4)}" + "\n"
              f"20 percent savings {int(save / 4)}")


# Go
print("This is a simple budget calculator based off the 50/30/20 rule" + "\n"
      "50 percent Needs" + "\n"
      "30 percent Wants" + "\n"
      "20 percent savings" + "\n")

totalMonthlyNetPay = float(input("Please enter your total monthly pay: "))

b = Budget(totalMonthlyNetPay)
