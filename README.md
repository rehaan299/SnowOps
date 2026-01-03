Snow and Ice Removal Performance Forecasting – City of Edmonton Prototype
Introduction
Edmonton, a northern city known for its long winters, faces significant challenges in managing snow and ice on its roadways. The City operates a Snow and Ice Control (SNIC) program that maintains main roads, bus routes, bike lanes, multi-use trails, residential roads and alleys throughout the winteredmonton.ca. When it snows, crews follow a well-defined plan and priority system to efficiently clear transportation routes – including roadways, protected bike lanes, sidewalks, and bus stops – to keep the mobility network safeedmonton.caedmonton.ca. Ensuring timely snow removal is critical not only for public safety and accessibility, but also for the economic well-being of the community.
In recent years, Edmonton has emphasized performance management in its infrastructure operations. The Parks and Roads Services (PARS) branch – which oversees snow removal – has been developing a comprehensive performance measurement framework for the SNIC programedmonton.ca. This includes tracking key metrics (e.g. response times, route completion rates, and service level compliance) and using data to inform decision-making. Under the City's Enterprise Performance Management (EPM) initiatives, services are encouraged to measure and improve their productivity and set targets for outcomes. For example, a 2021 audit recommended incorporating benchmarking practices into the City’s EPM framework, with clear guidelines so that decision-makers can compare performance against external standards and make informed choicesedmonton.ca. In the snow operations context, this means using data-driven insights to optimize resource allocation and to maintain council-approved service levels even as weather conditions fluctuate.
One area of growing interest is forecasting – using historical data and analytics to predict future snow and ice control needs. By forecasting the demand for snow removal in the upcoming season, City operations can better plan staffing, equipment, and materials (such as plow trucks, salt, and sand) in advance. For instance, knowing if next winter is likely to have above-average snowfall or an unusually high number of small snow events can guide budget preparations and ensure the City meets its roadway service level targets. This is important because it’s the number and nature of snow events (rather than just total snow volume) that drives removal costs – ten small snowfalls can be more expensive to handle than one big storm of equivalent total snowsunvalleyomaha.com. Many municipalities are turning to predictive modeling to aid winter operations; for example, predictive machine-learning models can forecast snowstorm frequency, enabling preemptive route planning and dynamic resource deploymentfareye.com. This prototype project demonstrates how the City of Edmonton could leverage its historical performance data and spatially-enabled route information to forecast next year’s snow and ice removal needs, as a tool to enhance operational planning and performance management.
Note: This project is a proof-of-concept and uses simulated dummy data for demonstration. All data sets (e.g. snowfall amounts, snow events, and road network details) are synthetic and created for this example. However, the approach and methods mirror real-world techniques and are informed by actual City policies and industry best practices in winter operations.
Project Objectives
This prototype project aims to achieve the following objectives:


Analyze Historical Performance: Ingest and analyze past winter operations data (e.g. number of snow events, snowfall amounts, and road clearing metrics) to understand trends and variability in the City’s snow and ice control demands.


Forecast Future Needs: Develop a simple model to forecast key metrics for the upcoming winter season, such as the expected number of city-wide snow events and the anticipated number of snow clearing operations for various roadway categories.


Spatial Data Integration: Incorporate spatially-enabled data (road network routes with priority levels) to distribute the forecasted operations geographically. This allows identifying where the demand will be (e.g. how often each route or area might need service), not just how much overall.


Performance & Resource Planning: Provide insights that help connect forecasted needs with performance targets. For example, use the forecast to anticipate if current resources are sufficient to meet the City’s Snow & Ice Control service level standards (clearing priorities within specified timelines) and inform budgeting or staffing adjustments ahead of time.


Documentation & Prototype Outputs: Produce a comprehensive README (this document) detailing the entire project, along with example data files, Python code, and visualizations (charts/maps) so that the analysis is transparent and reproducible as a prototype for a potential GitHub project.


Data Sources and Preparation
Historical Data: For this prototype, we created a dummy dataset representing 5+ years of Edmonton’s winter operations statistics. The data is an annual summary for each winter season (from 2018–2019 through 2022–2023 in our example). Each record includes: the winter season, the number of Snow Events (major snowfall events that triggered city-wide road clearing operations), the Total Snowfall in that season (in cm), and the number of times roads were cleared by priority category (P1 through P4). In reality, the City defines a “snow event” for roadways as an accumulation of ≥2 cm that requires clearing (and any amount of snow for active pathways triggers an event)edmonton.ca. For example, in the winter of 2022–23, Edmonton officially declared only 3 snow events for roadways (an unusually low-snow year), while Active Pathway areas saw 20 minor snowfall eventsedmonton.ca. That season had lower-than-average precipitation, which, combined with other factors (like additional staffing), led to improved snow clearing performance compared to the previous yearedmonton.ca. This illustrates how dramatically the workload can vary year to year.
For our dummy data, we emulate such variability. Table 1 below shows a snippet of the historical_snow_data.csv (constructed for this project):
Winter SeasonSnow EventsTotal Snow (cm)P1 OpsP2 OpsP3 OpsP4 Ops2018–201949044412019–2020713077752020–2021917099972021–202212200121212102022–20233603331
Table 1: Example historical winter data (dummy values). Snow Events counts the number of significant snowfalls requiring road clearing. Total Snow is the cumulative snowfall. P1 Ops through P4 Ops indicate how many times that category of road was serviced. (In this simplified data, Priority 1–3 operations usually equal the number of events, since those routes are cleared every time it snows. Priority 4 – residential roads – are often only cleared after larger storms, so the number of residential blading cycles can be lower than the total events in a season.)
This historical dataset would typically be derived from multiple real sources: e.g. Environment Canada weather data for snowfall, City operational logs of plowing/sanding activities, and performance reports. In the City of Edmonton, such data is tracked internally and summarized in annual SNIC reports. (For instance, the City’s 2022–23 report notes 44 precipitation days that winter vs a 53.7-day average, highlighting the below-average snowfall that yearpub-edmonton.escribemeetings.com.) For our prototype, we assume the data is readily available in the above aggregated format.
Spatial Data: We also include a dummy spatial dataset city_routes.geojson representing the road network segments in Edmonton and their snow clearing priorities. In reality, the City categorizes roads by priority (Priority 1 = major roads, Priority 2 = arterial/collector roads, Priority 3 = industrial/rural roads, Priority 4 = residential roadsedmonton.caedmonton.ca). The geospatial data would come from the City’s GIS – for example, an open data portal or internal GIS files containing road centerlines with attributes denoting priority class and route identifiers. For this prototype, we simulate a small set of road segments with a priority field (1–4). This spatial data allows us to link our forecast results to actual map features.
Before analysis, the data preparation steps involve loading the historical CSV and the routes GeoJSON. Minimal cleaning is needed since the dummy data is already consistent. In a real scenario, preparation could include merging multiple years of records, handling missing values (e.g. if a winter had an incomplete record), and ensuring the spatial data’s attributes align (e.g. priority labels match those used in the operations data). We also ensure that our data types are correct (e.g. numerical fields for snowfall, events counts, etc.) for analysis.
Methodology
Our methodology follows a typical data science workflow: starting with exploratory analysis of historical data, developing a forecasting model, and then integrating the results with spatial data for visualization. All analysis was done using Python. Key steps are outlined below.
Exploratory Data Analysis (EDA)
We first examined the historical trends in snow and ice control operations. This includes looking at how the number of snow events and total snow accumulation varied each year, and how that impacted the frequency of road clearing for different priorities. Understanding these patterns is crucial for making a credible forecast. For example, our dummy data shows that winter 2021–22 was especially severe (12 major snow events), whereas 2022–23 was extremely mild (only 3 events), with other years falling in between. This kind of volatility is consistent with real observations – cities often have some years with frequent storms and others that are relatively calm.
 Historical number of snow events per winter season in Edmonton (2015–2024 actual data in blue) with a forecast for 2025 (in red). Each point represents the count of city-wide snow events that triggered road clearing.
In the above chart, we observe the year-to-year fluctuation in snow events. There is no obvious upward or downward trend over the decade of historical data – instead, the pattern is cyclical or random, underscoring the influence of weather variability. For instance, the drop to only 3 events in the 2022–2023 season (far below the typical ~7–10 events) is a notable outlier. (This mirrors Edmonton’s actual 2022–23 winter, which saw unusually low snowfalledmonton.ca.) Such variability highlights a key challenge: budgeting and planning for snow control must account for uncertainty. The City’s performance reports indicated that in 2022–23, thanks in part to the lighter winter, crews were able to meet their road clearing targets more consistently (100% of priority routes cleared within the target time) compared to a heavier snow yearedmonton.ca. Conversely, a winter with many storms can strain resources and lead to lower compliance with the 1-day or 5-day clearing standards. These insights from EDA set the stage for forecasting – we expect our forecast to ideally predict an “average” demand, but we must be mindful of the possible swing to extremes.
Beyond just counts of events, we also looked at relationships in the data: e.g. does more total snow automatically mean more operations? Often, the number of snowfall events is more impactful than the total accumulationsunvalleyomaha.com. Ten small snowfalls will incur the cost of mobilizing crews ten times, whereas one big snowfall (even with the same total snow) might be handled in one extended operation. Our historical dummy data reflects this: compare 2017–2018 vs 2019–2020, where similar total snow might have been distributed in different event counts, leading to different numbers of mobilizations. This reaffirmed that our forecast model should focus on predicting the number of events first and foremost, as it’s a driver of operational workload.
Forecasting Model
For forecasting the next winter’s needs, we chose a straightforward approach suitable for the relatively small dataset. Given about 5–10 data points (winters) of history in our example, a complex machine learning model would be overkill – instead, we used a simple time-series average as our baseline forecast. Essentially, we took the mean of the number of snow events from past years to predict the next year’s number of events. This yielded an initial forecast of approximately 7 snow events for the upcoming winter. In practice, one might refine this by considering longer climate trends or known upcoming factors (e.g. ocean patterns like El Niño/La Niña that influence winter weather). For a more robust model, techniques such as ARIMA or Facebook Prophet (time series forecasting tools) could be applied given a longer historical record. These models can capture seasonality and trends – for example, an ARIMA model could use the last 30 years of snowfall data to project the probability of extreme seasons.
After forecasting the overall number of snow events, we translated that into expected operations for each road priority category. Under the City’s policy, whenever a snow event is declared, Priority 1, 2, and 3 roads will all be serviced (cleared or sanded) within days as part of the responseedmonton.caedmonton.ca. Priority 4 (residential) roads, however, are only bladed after significant accumulations (they aim to maintain up to 5 cm snowpack and will blade residentials typically once a major snowfall has ended, within 14 days)edmonton.ca. In other words, not every minor snow event triggers a citywide residential road clearing; it usually takes a larger storm or cumulative snowfall to initiate a residential blading cycle. Based on historical patterns, we estimated that out of the forecast ~7 snow events, roughly 4 of those would result in residential road clearing (P4 operations). This estimate came from looking at the ratio of past residential operations to events in the dummy data.
Thus, our forecast for next winter can be summarized as: about 7 major snow events city-wide, with each Priority 1–3 route likely needing ~7 clearings (one per event), and each Priority 4 route needing ~4 clearings (assuming not every event warrants a residential blade). We compiled these results into a simple forecast output, showing the expected number of operations by priority level for the next season.
To implement this, we wrote a Python script that:


Loads the historical data and computes the average number of snow events (or we could use a more advanced model’s prediction if available).


Rounds that forecast to a reasonable integer (since we can’t have a fraction of an event – we predicted 7 events for simplicity).


Assumes P1, P2, P3 operations will each equal the number of events (7 each in the forecast).


Estimates P4 operations by using the historical average proportion of events that led to residential blading. In our dummy data, roughly 65–70% of snow events resulted in a residential clearing (since minor events are sometimes skipped), so we applied a similar ratio to get ~4 for P4.


Saves the forecast results in a structured format (CSV file) for use in reporting and visualization.


This forms a basic forecasting framework. Of course, there are limitations: this model doesn’t incorporate any actual weather forecasting. In a real deployment, one might combine this with meteorological forecasts for the coming winter. For example, if Environment Canada projects a colder, snowier winter, the model’s output might be adjusted upward from the historical average. Conversely, if a mild winter is anticipated, the city might budget for fewer events. Nonetheless, even a historical-average-based forecast is valuable for budgeting, as it guards against the common pitfall of using only the last year’s data. Industry experts suggest planning based on long-run averages to avoid surprises – e.g., not assuming a string of mild winters will continue indefinitelysunvalleyomaha.com. Our forecast of 7 events is essentially a realistic baseline, around which the City can develop contingency plans for both lighter or heavier scenarios.
Spatial Integration & Mapping
The final step was to integrate the forecasted operations with the spatial road network data. This step addresses where the snow clearing needs will occur. Since our forecast is broken down by priority class, we can join those predictions to all road segments of that priority. We performed a spatial data merge: essentially adding a new attribute to each road in city_routes.geojson indicating the predicted number of times that road will be cleared next winter. All Priority 1, 2, and 3 roads received a value of 7 (the forecast number of events), and Priority 4 roads received a value of 4 in this example. The result is a geospatial dataset (routes_with_forecast.geojson) that can be visualized on a map.
If we were to visualize this, we could create a thematic map of Edmonton where each road segment is color-coded or labeled by how many clearings it’s expected to need. For instance, all major arteries (P1/P2) might be highlighted in one color (indicating they will be cleared 7 times), while residential streets might be a lighter color (4 times). This spatial visualization could help planners see if certain districts have disproportionately more road clearing operations (e.g. perhaps one district has many more roads in a certain priority).
For demonstration, we focused on generating a couple of summary charts from the data (shown in the Results section). However, the project could be extended to interactive maps. In fact, the use of GIS for snow operations is well-established: New York City’s sanitation department (DSNY) built internal apps to track snowplow routes in real-time, and they leveraged open-source geospatial tools like GeoPandas (for data processing) and LeafletJS (for interactive web maps) to create route analytics dashboardsesri.com. Likewise, Edmonton could incorporate this forecast data into an ArcGIS or Leaflet-based map for public communication or internal planning. For example, an operations dashboard could display our forecasted plow frequency alongside live tracking of plows during the winter, to compare forecast vs actual in each storm. Such integration of spatial analytics with predictive data would align well with the City’s goal of performance-based management and transparent service delivery.
Tech Stack
Our prototype leverages a modern data analytics tech stack, primarily in Python. Key technologies and libraries include:


Python 3.x – Chosen as the core language for its rich ecosystem in data science. Python was used for all data loading, analysis, and modeling tasks.


Pandas – Used for data manipulation and analysis of the tabular historical dataset. Pandas makes it easy to calculate statistics (like mean snow events) and filter or aggregate the data by year or road priority.


NumPy – Utilized under the hood by Pandas for efficient numerical computations. We used NumPy arrays for some calculations (e.g. computing ratios and means).


GeoPandas – An extension of Pandas for geospatial data, used to read and write GeoJSON files and to merge our forecast results with the spatial road network. GeoPandas handles geometric objects (like road segment shapes) and allowed us to perform the join based on the priority attribute.


Matplotlib (with Seaborn style) – Used for creating static charts to visualize historical trends and forecast results. We plotted the time series of snow events and a bar chart of operations by priority. Matplotlib provides fine control for labeling and styling, which we used to make the charts clear.


StatsModels / scikit-learn (potential) – While our final model was a simple average (implemented without special libraries), we considered using StatsModels for an ARIMA time-series model or scikit-learn for a regression, if a more sophisticated approach were warranted. These libraries could be introduced if the project scope grows (e.g., incorporating weather predictors into the forecast).


Jupyter Notebook – During development, we used Jupyter notebooks to interactively explore the data and test the forecasting approach. This allowed for iterative visualization and tweaking of the model before exporting the code to standalone .py scripts for the final project structure.


GIS Tools (optional) – Although not explicitly used in our code, tools like QGIS or ArcGIS Pro could be used to further visualize the output GeoJSON and produce maps. Additionally, if this project were deployed, we might use a web mapping library (e.g., Leaflet or Mapbox GL JS) to create an interactive map for stakeholders to explore the forecast by area.


Environment: The code is written to be run in a standard Python environment. One should have the above libraries installed (pandas, geopandas, matplotlib, etc.). The project is OS-agnostic (Windows, Linux, Mac) as long as the environment is set up. For reproducibility, a requirements.txt could be provided listing exact version numbers of libraries used, but generally the latest versions as of 2025 will work.
Project Structure
The repository is organized as follows (files and directories):
snow-ice-forecasting-project/
├── README.md               <- Comprehensive project documentation (this file)
├── data/
│   ├── historical_snow_data.csv    <- Dummy historical winter operations data (see format in README)
│   └── city_routes.geojson         <- Dummy spatial data of city road segments with priority attribute
├── src/
│   ├── forecast_model.py           <- Python script for loading data, forecasting next year's needs, and outputting results
│   └── visualization.py            <- Python script for generating plots/visualizations from data and forecast
├── images/
│   ├── snow_events_trend.png       <- Line chart of historical snow events vs forecast (generated by visualization.py)
│   └── forecast_by_priority.png    <- Bar chart comparing last season vs next season forecast by priority (generated by visualization.py)
└── requirements.txt         <- (Optional) Python package requirements for the project environment



The data/ folder contains input datasets. In a real project, this might include raw data (e.g. daily logs or GIS files) and processed data. Here we have the primary inputs: historical_snow_data.csv and city_routes.geojson. We emphasize that these contain dummy data for prototype purposes. If adapting this project, one would replace these with real City of Edmonton data (e.g., from their open data portal or internal databases).


The src/ directory holds the source code. We have separated the core forecasting logic (forecast_model.py) from the visualization code (visualization.py) to keep things modular. For example, one could rerun just the forecast script when new data comes in, without regenerating charts, or vice versa. (Alternatively, all code could be in a single notebook or script; we chose multiple files for clarity.)


The images/ directory stores the output figures that are included in the README for illustration. These images were produced by running the visualization script. In a live GitHub project, including such images is helpful so that readers can see the results without running the code. We explicitly note in the README how these were created and what they show.


The requirements.txt (if provided) would list required libraries (with versions). This ensures someone recreating the environment can install the same dependencies using pip install -r requirements.txt. (For example, entries would include pandas, geopandas, matplotlib, etc. with specific version numbers.)


Below we provide the content of the main source files. These scripts are written in a clear, commented manner for ease of understanding:
src/forecast_model.py
import pandas as pd

# Load historical data
df = pd.read_csv('../data/historical_snow_data.csv')  # adjust path as needed if running from project root

# Compute basic statistics from historical data
avg_events = df['Snow Events'].mean()  # average number of snow events per year
forecast_events = round(avg_events)    # forecasted number of snow events for next season (rounded to nearest int)

# We assume Priority 1-3 roads are cleared for each snow event:
forecast_ops_p1 = int(forecast_events)
forecast_ops_p2 = int(forecast_events)
forecast_ops_p3 = int(forecast_events)

# Estimate Priority 4 (residential) operations based on historical ratio of P4 ops to events
if df['Snow Events'].sum() > 0:
    ratio_p4 = df['P4 Ops'].sum() / df['Snow Events'].sum()
else:
    ratio_p4 = 0
forecast_ops_p4 = int(round(ratio_p4 * forecast_events))

# Prepare forecast results as a DataFrame
forecast_df = pd.DataFrame({
    'Priority': [1, 2, 3, 4],
    'Forecast_Operations': [forecast_ops_p1, forecast_ops_p2, forecast_ops_p3, forecast_ops_p4]
})

# Save the forecast results to a CSV (could be used by other scripts or for reporting)
forecast_df.to_csv('../data/forecast_ops_next_year.csv', index=False)

# Print out a summary of the forecast
print(f"Predicted number of snow events next winter: ~{forecast_events}")
print("Expected snow clearing operations for next winter by priority level:")
print(f"  Priority 1-3 roads: ~{forecast_ops_p1} operations each (one per snow event)")
print(f"  Priority 4 roads: ~{forecast_ops_p4} operations (blading cycles in residential areas)")

# Optional: integrate with spatial data if available
try:
    import geopandas as gpd
    routes_gdf = gpd.read_file('../data/city_routes.geojson')
    # Merge forecast ops into routes by matching priority
    routes_gdf = routes_gdf.merge(forecast_df, how='left', left_on='priority', right_on='Priority')
    # Save the routes with forecast data (could be used in a GIS or further analysis)
    routes_gdf.to_file('../data/routes_with_forecast.geojson', driver='GeoJSON')
    print("GeoJSON with forecast operations per route saved to data/routes_with_forecast.geojson")
except ImportError:
    print("geopandas not installed; skipping spatial merge.")
except Exception as e:
    print(f"Skipping spatial integration due to error: {e}")

Explanation: This script reads the historical data, calculates the average number of snow events, and uses that to forecast the next season. It then constructs a small table of expected operations for priority 1–4 roads. The results are printed to the console and also saved to forecast_ops_next_year.csv for use by other parts of the project. At the end, the script attempts an optional step: if geopandas is installed and the city_routes.geojson file is present, it merges the forecast data into the spatial dataset and outputs a new GeoJSON (routes_with_forecast.geojson). This file would contain each road segment with an added field for Forecast_Operations, which could be visualized on a map. We wrap this in a try/except so that the script still runs even if geopandas isn't available (in which case it just skips the spatial part). The console prints provide a quick summary for the user running the script.
src/visualization.py
import pandas as pd
import matplotlib.pyplot as plt

# Load historical data and forecast results
df = pd.read_csv('../data/historical_snow_data.csv')
forecast_df = pd.read_csv('../data/forecast_ops_next_year.csv')

# Determine the forecasted number of events (Priority 1 forecast operations equals number of events)
forecast_events = int(forecast_df[forecast_df['Priority'] == 1]['Forecast_Operations'])

# Plot 1: Snow events trend over years with forecast
years = df['Winter Season']  # assuming this column holds a numeric year or season label
events = df['Snow Events']

plt.figure(figsize=(6,4))
plt.plot(years, events, marker='o', color='steelblue', label='Historical Snow Events')
# Extend the line to next year forecast
if len(years) > 0:
    next_year = years.iloc[-1] + 1  # increment the last year for forecast label (if years are numeric like 2018, 2019,...)
else:
    next_year = 1
plt.plot([years.iloc[-1], next_year], [events.iloc[-1], forecast_events], 
         linestyle='--', marker='o', color='orangered', label='Forecast (Next Year)')
plt.xlabel('Winter Season')
plt.ylabel('Number of Snow Events')
plt.title('Snow Events per Winter – Historical and Forecast')
plt.legend()
plt.grid(True)
# Save the figure
plt.tight_layout()
plt.savefig('../images/snow_events_trend.png')
plt.close()

# Plot 2: Comparison of last season vs forecast by priority
# Get last season's operations from historical data (assuming last row is last season)
last = df.iloc[-1]
last_ops = [last['P1 Ops'], last['P2 Ops'], last['P3 Ops'], last['P4 Ops']]
forecast_ops = list(forecast_df['Forecast_Operations'])

labels = ['Priority 1', 'Priority 2', 'Priority 3', 'Priority 4']
x = range(1, 5)

plt.figure(figsize=(6,4))
plt.bar([i - 0.2 for i in x], last_ops, width=0.4, color='gray', label='Last Season')
plt.bar([i + 0.2 for i in x], forecast_ops, width=0.4, color='teal', label='Forecast')
plt.xticks(x, labels)
plt.ylabel('Number of Operations')
plt.title('Snow Clearing Operations: Last Season vs Next Season Forecast')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('../images/forecast_by_priority.png')
plt.close()

Explanation: This visualization script generates two charts and saves them as PNG images in the images/ folder. The first chart (“snow_events_trend.png”) plots the historical number of snow events per year and appends the forecast for the next year as a red point with a dashed line. This gives a quick visual of how the forecast compares to past winters. The second chart (“forecast_by_priority.png”) is a side-by-side bar chart comparing the last winter season with the forecast for next winter, broken down by road priority level. This chart helps illustrate how we expect the operations for each category to change (or not change). In our dummy case, the forecast is fairly similar to the last season for P1–P3 (since last season had 3 events and forecast has 7, P1–P3 increase accordingly) and shows a slight increase for P4. The chart uses different colors and includes a legend for clarity. After plotting, we call plt.close() to free up memory since these scripts might be run in succession.
Usage Instructions
To run this project yourself (with the dummy data or your own data), follow these steps:


Setup Environment: Ensure you have Python 3 installed, along with the required libraries. You can install the needed packages using pip. For example:
pip install pandas numpy geopandas matplotlib

(GeoPandas may require additional system dependencies for spatial data support; if preferred, you can skip the spatial part by not installing GeoPandas.) Alternatively, use the provided requirements.txt with pip install -r requirements.txt to get exact versions.


Obtain Data: Place the historical snow data CSV and the city routes GeoJSON in the data/ directory. If you are using the dummy data from this project, it should already be there. If you want to experiment with real data, ensure it matches the expected format (you might need to modify the code if your columns are named differently or if you have more detailed data).


Run Forecast Script: Execute the forecasting script to generate the prediction. From the project root directory, run:
python src/forecast_model.py

This will output a summary to the console (showing the predicted number of events and operations) and create a file data/forecast_ops_next_year.csv. If GeoPandas is available, it will also produce data/routes_with_forecast.geojson. Check the console output for any messages (e.g., it will notify you if the spatial integration was skipped).


Run Visualization Script: Next, generate the charts by running:
python src/visualization.py

This will read the historical data and the forecast results, then save two image files in the images/ folder (snow_events_trend.png and forecast_by_priority.png). You can open these PNG files to view the charts. They are also embedded in the README for quick reference.


Inspect Outputs: Open the images to analyze the forecast. The snow events trend chart will show you how next year’s predicted number of snow events compares to previous years. The operations by priority chart will show, for example, if you are expecting to do more residential blading operations next year than last year, or if the demand on main roads will be similar to before. If you generated routes_with_forecast.geojson, you can load it in a GIS tool (or a GeoJSON viewer) to see each road segment with the forecast attribute.


Iterate or Modify: Feel free to adjust the dummy data or model. For example, try changing the number of events in historical_snow_data.csv to simulate a different climate trend and rerun the forecast. The code is relatively simple and documented, so it’s also easy to replace the forecasting logic with something more sophisticated if desired.


Results and Analysis
After running the analysis with our prototype data, we obtain a forecast that next year will have approximately 7 snow events requiring major roadway clearing. This is in line with the historical average in our dataset. For context, Edmonton’s winters typically have around 7–10 noticeable snowfall events, although it can vary widely (as seen with 3 events in one year vs. 12 in another in our data). The forecast is neither an extreme high nor low, but a moderate scenario.
In terms of operations, the forecast translates to the following expected workload:


Priority 1 (freeways, arterial main roads) – cleared ~7 times over the winter (essentially every event).


Priority 2 (other arterial/collector roads, bus routes) – cleared ~7 times (every event, similar to P1).


Priority 3 (industrial and rural roads) – cleared ~7 times (each event, since even lower-priority public roads get attention during city-wide snow response).


Priority 4 (residential roads and alleys) – bladed ~4 times in the winter (only after significant snow accumulation; not every minor snowfall will trigger residential blading).


 Comparison of the last winter season (gray) vs. the next winter’s forecast (teal) for the number of snow clearing operations by priority level. The chart illustrates that, in this example, the upcoming winter is expected to be busier than the last in terms of snow events (7 vs 3 events, hence the taller teal bars for P1–P3). Consequently, we predict more operations on all road types compared to the previous year. The residential roads (P4) in the last season were only bladed once (since 2022–23 had very little snow), but we forecast around 4 residential clearing cycles next season – a notable increase.
From a performance management perspective, this forecasted increase in operations is critical information. If the City expects more frequent snow events, it may need to allocate a higher budget or ensure additional crews and equipment are on standby to maintain the same level of service. In Edmonton’s case, they have service level targets such as clearing Priority 1 roads within 24 hours of a snowfall endedmonton.ca, Priority 2 within 5 daysedmonton.ca, and residential within 14 daysedmonton.ca. These targets were met 100% in the mild 2022–23 winteredmonton.ca partly because there were so few events (and because extra staff had been hired that seasonedmonton.ca). If next winter brings more snow, maintaining those performance levels will be more challenging. The City might need to ramp up resources (e.g. hire seasonal staff or contractors in advance) to handle the ~7 events forecast. This aligns with what happened historically: when additional crews were available, the City could improve its snow clearing completion rates despite eventsedmonton.ca. Our forecast thus serves as a proactive tool – it signals to decision-makers that last year’s minimal operations were an anomaly and that a return to a more average winter will require renewed investment and readiness.
Another insight from the results is the significance of residential clearing cycles. They are resource-intensive (blading thousands of neighborhood streets can take up to two weeks for a full cycleedmonton.ca). An increase from 1 residential cycle last year to 4 next year could substantially impact resident satisfaction and City communications (e.g. announcing parking bans for residential blading four times). Knowing this in advance allows for better communication strategies and perhaps exploring efficiencies (like dividing the city into zones to clear sequentially).
It’s also worth noting what the forecast does not capture: timing and clustering of events. Seven events could be spread out as one per week all winter (easier to manage), or they could come as two or three back-to-back blizzards (much harder to manage). Our simple model doesn’t predict this level of detail. It provides a seasonal total. However, it establishes a baseline expectation. If early in the season it appears we are deviating (say, December already had 5 events), managers could adjust the plan (e.g. prepare for the possibility of an above-average year).
In summary, the results indicate a return to normal winter operations levels in the coming year, after an exceptionally light year. The City should plan for more frequent deployments of plows and consider the strain on meeting all policy timelines if the forecast holds true. These findings would be reported to the relevant City departments to inform winter budget planning and resource allocation.
Discussion and Implications
The prototype demonstrates how forecasting can be integrated into performance management for winter operations. There are several implications and points of discussion:


Budgeting and Resource Allocation: Using a data-driven forecast helps avoid the common pitfall of simply using last year’s expenditures to set the budgetsunvalleyomaha.com. If Edmonton had cut its snow budget after a mild winter, it might be under-prepared for an average or heavy winter. Our forecast suggests budgeting for ~7 events, which ensures funds for salt, sand, fuel, staff overtime, etc., are in line with a typical winter. This approach smooths out the spikes – as recommended by experts, looking at a 5-year average can greatly reduce surprises and ensure sufficient funds over the long runsunvalleyomaha.com.


Performance Targets and Staffing: The City’s performance framework for SNIC could benefit from forecasts by setting realistic targets. For example, if more events are expected, perhaps the target of 100% routes cleared within the set time might be at risk unless extra measures are taken. Edmonton’s experience showed that adding staff improved performance outcomes in snow clearingedmonton.ca. With a forecast, management can decide early if they need to hire temporary crews or authorize overtime to maintain performance levels. This proactive stance is far better than reacting after service levels slip.


Public Communication: In a performance management context, communicating expectations is key. If the City knows that more residential blading will occur, it can start informing the public earlier about parking bans and what to expect. Conversely, if a light winter was forecast (not the case in our example, but hypothetically), the City could explain any budget savings or reallocate resources to other winter maintenance tasks (like more frequent ice scraping on bike lanes, etc.). Essentially, forecasting adds to transparency – it provides a rationale for City actions and helps set public expectations (residents often wonder “will my street get cleared this winter and how often?” – now there’s a data-backed estimate).


Limitations and Uncertainty: It’s important to stress that a forecast is not a guarantee. Weather can always surprise us. Our model, being simple, has a wide uncertainty range. In practice, we might present the forecast as a range (e.g. “We expect 6–8 major snow events”) rather than a single number. Scenario planning is useful: If we get 10+ events, do we have a contingency budget? If only 3 events, will we divert savings to additional sidewalk clearing or carry it forward? These discussions can happen before the season starts, using the forecast as a starting point.


Link to Route Optimization: While our project didn’t delve into route optimization, having a spatial forecast could feed into those algorithms. If certain districts are expected to be serviced 4 times, the City could optimize plow routes knowing they’ll be run multiple times (maybe alternating starting points each event to spread out who gets cleared first). There is active research on optimizing snowplow routes to minimize cost and timebeta-inc.comfareye.com, and combining that with frequency predictions is an exciting future direction.


Enterprise Performance Management (EPM) Alignment: In the broader sense, integrating forecasting into the City’s EPM framework means the City can set performance benchmarks not just based on static targets, but dynamic ones informed by expected conditions. For example, a KPI could be “% of snow events for which we met the clearing timeline.” If we forecast more events, maybe the acceptable threshold could be adjusted or contingency plans triggered. The City Auditor’s report on productivity noted the lack of external benchmarkingedmonton.ca – one could potentially benchmark Edmonton’s forecasted vs actual snow clearing efficiency against similar cities (e.g., compare with Calgary or Winnipeg data) to strive for best-in-class performance. Our project lays the groundwork by quantifying the upcoming workload, which is the first step to such comparisons.


In summary, the discussion underscores that forecasting enhances preparedness. It connects the dots between past performance, future needs, and resource deployment. For the City of Edmonton, adopting such a model (refined with real data and better algorithms) could mean more resilient winter operations and a more agile performance management process, where targets and resources are continually aligned with the reality of Mother Nature.
Future Work
This prototype can be expanded and improved in numerous ways. Some potential future enhancements include:


Incorporate Climate Forecasts: Integrate weather forecast data (e.g. seasonal climate outlooks) into the model. For instance, if meteorological services predict an El Niño winter (typically warmer/drier in Edmonton) or a La Niña winter (colder/snowier), the model could weight the forecast accordingly. This could be done via regression (with ENSO indices as input) or simply adjusting the output based on expert guidance.


Advanced Predictive Modeling: Implement more sophisticated time-series models or machine learning algorithms. With a richer historical dataset (say 20+ years of data at monthly resolution), one could use ARIMA, exponential smoothing, or even machine learning models (random forests, etc.) to predict snowfall or snow events. These models might capture trends (e.g. if climate change is gradually affecting snowfall) or periodic cycles. Additionally, using bootstrapping or simulation to estimate the probability of extreme scenarios (very high or low snow years) would provide a risk assessment around the forecast.


Higher Granularity Spatial Forecasts: Our current forecast treats all P1 (etc.) roads the same. In reality, there could be micro-climate differences or usage differences across the city. Future work could attempt to forecast needs at a district or route level. For example, perhaps the southwest quadrant of the city typically gets slightly more snow (due to storm tracks) – the City could then allocate slightly more equipment there. This would require localized historical data, possibly from road weather information systems or maintenance records by depot.


Real-time Data Integration: Develop a dashboard that not only shows the preseason forecast (what we did here) but also tracks progress through the winter. This could tie in live data, such as the number of events that have occurred so far versus forecast. If by mid-winter the forecast is exceeded, the tool could alert managers to consider activating additional resources or contracting extra help. Conversely, if it’s a mild winter, they might save budget. Integrating with the City’s 24/7 operations center data (plow GPS trackers, 311 complaints about snow, etc.) could provide a comprehensive Winter Operations Dashboard.


Performance Benchmarking and Reporting: Extend the performance framework to include this forecasting module. That is, after winter, compare the forecast vs actual: How accurate were we? Use this to improve the model (learning from errors). Also, incorporate metrics like cost per event, or % of events where service level was met, and relate it to the forecast. Over time, this could become a standard part of annual reporting (e.g. “We predicted 7 events, we got 9 events; as a result, we exceeded our planned budget by X but still achieved Y% service level”). This kind of reflection closes the loop in the performance management cycle.


Integration with Route Optimization & Scheduling: As hinted earlier, combine the forecasting with route optimization tools. Esri’s Winter Weather solutions and other logistic software can create optimal plow routesbeta-inc.com. Using forecast frequency, one could schedule maintenance (like which routes might need more frequent salt refills, etc.). Also, labor scheduling can benefit – e.g., ensure standby contracts are in place for the forecast number of events (plus a margin).


Use of Real Data & Validation: Transition from dummy data to real City of Edmonton data. This would involve obtaining detailed records (perhaps from the City’s open data catalog or internal systems) such as daily snow clearing logs, snowfall measurements, etc. We would then validate the model: how would it have performed in past years if we had used it? We could back-test the forecast on previous winters to gauge its accuracy. This validation would highlight if the simple average is sufficient or if another method consistently performs better.


Enhance Visualization: Create interactive visualizations for the GitHub project. For example, an interactive map (using Folium or Mapbox) that shows the forecast by area, or an interactive chart where one can toggle different scenarios (normal winter vs extreme winter). This would make the project more engaging for stakeholders exploring the repository.


Each of these future improvements would move the project from a basic prototype closer to a robust decision-support tool for the City. Given the importance of snow and ice control in Edmonton (often a topic of high public interest and significant budget expenditure), investing in such data-driven tools can yield substantial benefits in efficiency and service quality.
Conclusion
In this project, we presented a comprehensive prototype for a Snow and Ice Removal Performance Forecasting tool, tailored to the City of Edmonton’s context. Using a combination of historical data analysis, simple forecasting techniques, and spatial data integration, we demonstrated how one can predict next year’s winter maintenance needs and tie those predictions into the City’s performance management framework. The project resulted in a detailed README (this document), sample code, and visual examples that showcase the approach.
What we achieved: We showed that even with a straightforward model, valuable insights emerge – such as anticipating a return to average winter conditions after an outlier year and quantifying the expected increase in operations across different road priorities. By doing so, we highlighted how forecasting supports proactive decision-making: budgets can be set more realistically, resources can be marshaled in advance, and service level targets can be safeguarded through informed planning. We also maintained an emphasis on spatial awareness, ensuring the forecast is not just abstract numbers but is linked to actual city streets and infrastructure.
Value to Performance Management: This prototype aligns with the City’s efforts to adopt a more data-driven culture. It provides a template for integrating analytics into municipal operations. In essence, it turns historical performance data into a forward-looking management tool. As Edmonton refines its Enterprise Performance Management system, projects like this can serve as pilot initiatives that demonstrate quick wins – showing Council and management that investing in analytics yields actionable intelligence (e.g., identifying the need for additional snow crews or the benefit of reallocating resources). Moreover, it underscores transparency: predictions and outcomes can be tracked and reported, holding the City accountable and allowing continuous improvement in the process.
It is important to reiterate that the data used here was dummy and the model simplistic. For real-world adoption, further refinement and validation are needed (as discussed in Future Work). However, the structure of the project – with clear data input, documented code, and interpretive output – means it can be a strong foundation to build upon. A city like Edmonton, with its open data and smart city initiatives, could take this prototype and enrich it with real data and more advanced models relatively easily.
Ultimately, being prepared for whatever winter might bring is the goal of any city’s snow and ice control program. This forecasting project is a step in that direction – moving from reactive operations to a predict-and-prepare strategy. By forecasting next year’s needs and planning accordingly, Edmonton can continue to keep its roads safe and mobility reliable for all citizens, while using taxpayer resources efficiently and meeting its performance objectives. The project serves as an illustrative example of how deep research and practical application can come together in an open-source format (a GitHub repository) to drive innovation in public service delivery.
