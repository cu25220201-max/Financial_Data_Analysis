import pandas as pd

df = pd.read_csv("financial_data.csv")

print(df)
print("Total Revenue =", df["Revenue"].sum())
print("Total Profit =", df["Profit"].sum())
highest = df.loc[df["Revenue"].idxmax()]

print(highest)
import matplotlib.pyplot as plt

plt.plot(
    df["Year"],
    df["Revenue"],
    marker="o"
)

plt.title("Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Revenue")

plt.show()
plt.bar(
    df["Year"],
    df["Profit"]
)

plt.title("Profit Analysis")
plt.xlabel("Year")
plt.ylabel("Profit")

plt.show()
growth = (
    df["Revenue"].iloc[-1] -
    df["Revenue"].iloc[-2]
)

forecast = (
    df["Revenue"].iloc[-1] +
    growth
)

print("Forecast Revenue 2026 =", forecast)
