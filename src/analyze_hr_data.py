#%% Import necessary libraries
import pandas as pd
from plotly import express as px
import plotly.graph_objects as go

#%% Laod the HR data
def load_activity_data(PATH):
    df1 = pd.read_csv(PATH) # Dataframe is like a table. in argument ../ to geht out of src folder and go somewhere else
    return df1

    #%% Sakai_3 mean and max of power
    #power_max = df1["PowerOriginal"].max()  # Maximum value
    #power_mean = df1["PowerOriginal"].mean()  # Mean value

    #df1["PowerOriginal"].plot()  # Plot the PowerOriginal column

    #print("Maximum Power:", power_max)
    #print("Mean Power:", power_mean)

    #%% Sakai_3 mean and max of heart rate
    #hr_max = df1["HeartRate"].max()  # Maximum value
    #hr_mean = df1["HeartRate"].mean()  # Mean value

    #df1["HeartRate"].plot()  # Plot the HeartRate column

    #print("Maximum Heart Rate:", hr_max)
    #print("Mean Heart Rate:", hr_mean)

    #%% Zone definitions
def set_max_hr(max_hr):
    set_max_hr = max_hr

    hr_zones = {}
    counter = 1
    for percent in range(50, 100, 10):
        hr_zones["Zone " + str(counter)] = set_max_hr * (percent / 100)
        counter += 1

    hr_zones["Zone 1"] = 0
    return hr_zones

    #%% Assign zones based on heart rate
def assign_zones(df1, hr_zones):
    current_zone = []

    for row in df1.iterrows():
        current_hr = row[1]["HeartRate"]
        for zone, threshold in reversed(list(hr_zones.items())):
            if current_hr > threshold:
                current_zone.append(zone)
                break  # Stop after finding the first matching zone

    df1["Zone"] = current_zone  # Add the zones to the dataframe
    df1_zone_mean = df1.groupby("Zone").mean()

    time_in_zones = {}

    for zone in current_zone:
        if zone =="Zone 1":
            time_in_zones["Zone 1"] = time_in_zones.get("Zone 1", 0) + 1
        elif zone == "Zone 2":
            time_in_zones["Zone 2"] = time_in_zones.get("Zone 2", 0) + 1
        elif zone == "Zone 3":
            time_in_zones["Zone 3"] = time_in_zones.get("Zone 3", 0) + 1
        elif zone == "Zone 4":
            time_in_zones["Zone 4"] = time_in_zones.get("Zone 4", 0) + 1
        elif zone == "Zone 5":
            time_in_zones["Zone 5"] = time_in_zones.get("Zone 5", 0) + 1
    
    return df1, time_in_zones
    
    # Create a new DataFrame for time in zones
def zone_time_and_power(df1, time_in_zones):
    df1_zone_time_power = pd.DataFrame.from_dict(time_in_zones, orient='index', columns=["Time in Zone"])
    df1_zone_time_power.index.name = "Zone"
    mean_power_in_zones = df1.groupby("Zone")["PowerOriginal"].mean()
    mean_power_in_zones = mean_power_in_zones.round(2)  # Round the mean power values to 2 decimal places
    df1_zone_time_power["Mean Power"] = mean_power_in_zones
    return df1_zone_time_power
    #%% Plot with plotly
def plot_hr_data(df1, hr_zones):
    df1["Time"] = df1.index / 60
    zone_colors = {
        'Zone 1': 'rgba(198,239,206,0.3)',  # hellgrün
        'Zone 2': 'rgba(255,255,153,0.3)',  # gelb
        'Zone 3': 'rgba(255,204,102,0.3)',  # orange
        'Zone 4': 'rgba(255,153,51,0.3)',   # dunkleres orange
        'Zone 5': 'rgba(255,102,102,0.3)'   # rot
    }
    fig = px.line(df1, x="Time", y="HeartRate", title="Heart Rate in Zones")

    # Sortierte Zonen für sichere Reihenfolge
    zone_items = list(hr_zones.items())
    for i, (zone, lower) in enumerate(zone_items):
        upper = zone_items[i + 1][1] if i + 1 < len(zone_items) else df1["HeartRate"].max()
        fig.add_shape(
            type="rect",
            xref="paper", yref="y",
            x0=0, x1=1,
            y0=lower, y1=upper,
            fillcolor=zone_colors[zone],
            line=dict(width=0),
            layer="below"
        )

    # Layout
    fig.update_traces(line=dict(color="black", width=2))
    fig.add_scatter(
        x=df1["Time"],
        y=df1["PowerOriginal"],
        name="Power",
        yaxis="y2",
        line=dict(color="blue", width=2, dash="dot")
    )
    fig.update_layout(
        xaxis_title="Time / min",
        yaxis_title="Heart Rate / bpm",
        xaxis=dict(showgrid=False),
        yaxis=dict(
            title="Heart Rate / bpm",
            range=[df1["HeartRate"].min() - 5, df1["HeartRate"].max() + 5],
            showgrid=False
        ),
        yaxis2=dict(
            title="Power / Watt",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        showlegend=False
    )
    return fig

#%% Test functions of pandas
TEST_PATH = "data/activity.csv"
df2 = pd.read_csv(TEST_PATH)

#%% Select specific columns from the dataframe
df2["HeartRate"] # Select a single column
df2[["Distance", "HeartRate"]]  # Select multiple columns
df2[["Distance", "HeartRate", "Cadence"]]  # Select multiple columns including Time

#%% Read max, min, mean, and median of the HeartRate column
df2["HeartRate"].max()  # Maximum value
df2["HeartRate"].min()  # Minimum value 
df2["HeartRate"].mean()  # Mean value
df2["HeartRate"].median()  # Median value

#%% Plot Values
df2["HeartRate"].plot()  # Plot the HeartRate column

#%% Zone definition
df2["HeartRate"] > 180
df2["Zone 5"] = df2["HeartRate"] > 180  # Create a new column "Zone 5" with True/False values
df2["Zone 5"].value_counts()  # Count the number of True/False values in the "Zone 5" column

# %% Zugreifen auf einen bestimmten Wert
df2.iloc[0,3] # Heart Rate in der ersten Zeile (0. Zeile, 3. Spalte)

# %% Mean value in Zone 5 table
df2.groupby("Zone 5").mean()  # Group by "Zone 5" and calculate the mean of "HeartRate"

# %%
