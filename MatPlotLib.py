import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"D:\PROGRAM\PYTHON COLLEGE\NumPy\plotting_data.xls")

df["Date"] = pd.to_datetime(df["Date"])


plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature (°C)"], marker="o", linestyle="-", color="r", label="Temperature (°C)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Humidity (%)"], marker="s", linestyle="--", color="b", label="Humidity (%)")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.title("Humidity Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()


plt.show()
