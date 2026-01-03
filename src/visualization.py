import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv("data/historical_snow_data.csv")
forecast = pd.read_csv("data/forecast_ops_next_year.csv")

forecast_events = int(
    forecast[forecast["Priority"] == 1]["Forecast_Operations"].iloc[0]
)

# ----------------------------
# Plot 1: Snow Events Trend
# ----------------------------
years = df["Winter Season"]
events = df["Snow Events"]

plt.figure(figsize=(7, 4))
plt.plot(years, events, marker="o", label="Historical")
plt.plot(
    [years.iloc[-1], years.iloc[-1] + 1],
    [events.iloc[-1], forecast_events],
    linestyle="--",
    marker="o",
    label="Forecast"
)

plt.xlabel("Winter Season")
plt.ylabel("Snow Events")
plt.title("Snow Events – Historical vs Forecast")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/snow_events_trend.png")
plt.close()

# ----------------------------
# Plot 2: Operations by Priority
# ----------------------------
last_year = df.iloc[-1]
last_ops = [
    last_year["P1 Ops"],
    last_year["P2 Ops"],
    last_year["P3 Ops"],
    last_year["P4 Ops"]
]

forecast_ops = forecast["Forecast_Operations"].tolist()
labels = ["P1", "P2", "P3", "P4"]
x = range(len(labels))

plt.figure(figsize=(7, 4))
plt.bar([i - 0.2 for i in x], last_ops, width=0.4, label="Last Season")
plt.bar([i + 0.2 for i in x], forecast_ops, width=0.4, label="Forecast")

plt.xticks(x, labels)
plt.ylabel("Operations")
plt.title("Snow Clearing Operations by Priority")
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("images/forecast_by_priority.png")
plt.close()
