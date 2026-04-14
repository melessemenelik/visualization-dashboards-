import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
sales = [120, 150, 170, 200]

plt.plot(quarters, sales, marker="o")
plt.title("Business Unit Sales Report")
plt.xlabel("Quarter")
plt.ylabel("Sales (in $K)")
plt.show()
