import pandas as pd

# ----------------------------
# Load historical snow data
# ----------------------------
df = pd.read_csv("data/historical_snow_data.csv")

# ----------------------------
# Forecast number of snow events
# ----------------------------
average_events = df["Snow Events"].mean()
forecast_events = round(average_events)

# ----------------------------
# Operations assumptions
# ----------------------------
forecast_p1 = forecast_events
forecast_p2 = forecast_events
forecast_p3 = forecast_events

# Residential roads (P4) cleared less frequently
p4_ratio = df["P4 Ops"].sum() / df["Snow Events"].sum()
forecast_p4 = round(p4_ratio * forecast_events)

# ----------------------------
# Create forecast output
# ----------------------------
forecast_df = pd.DataFrame({
    "Priority": [1, 2, 3, 4],
    "Forecast_Operations": [
        forecast_p1,
        forecast_p2,
        forecast_p3,
        forecast_p4
    ]
})

forecast_df.to_csv("data/forecast_ops_next_year.csv", index=False)

print("Snow & Ice Removal Forecast")
print("---------------------------")
print(f"Forecasted Snow Events: {forecast_events}")
print(f"P1–P3 Operations: {forecast_events}")
print(f"P4 Residential Operations: {forecast_p4}")

# ----------------------------
# Optional spatial integration
# ----------------------------
try:
    import geopandas as gpd

    routes = gpd.read_file("data/city_routes.geojson")
    merged = routes.merge(
        forecast_df,
        left_on="priority",
        right_on="Priority",
        how="left"
    )

    merged.to_file("data/routes_with_forecast.geojson", driver="GeoJSON")
    print("Spatial forecast saved to data/routes_with_forecast.geojson")

except Exception as e:
    print("Spatial integration skipped:", e)
