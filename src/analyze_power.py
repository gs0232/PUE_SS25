<<<<<<< HEAD
#%% import
=======
# %% Import
>>>>>>> main
import pandas as pd
import plotly.express as plx
import numpy as np

<<<<<<< HEAD
#%% Function to analyze power data

=======
# %% Funktion zur Analyse der Leistungsdaten
>>>>>>> main
def analyze_power(FILE_POWER, row_name):
    df_power = pd.read_csv(FILE_POWER)
    df_power_curve = pd.DataFrame(columns=["Power / W", "Time / min"])

<<<<<<< HEAD
=======
    # Erzeuge eine absteigende Liste von Power-Werten
>>>>>>> main
    column_1 = np.arange(df_power[row_name].max(), df_power[row_name].min(), -1)
    df_power_curve["Power / W"] = column_1
    df_power_curve["Time / min"] = 0

    sum = []
    counting_sum = 0
<<<<<<< HEAD
=======

>>>>>>> main
    for i in df_power_curve["Power / W"]:
        counting_sum += (df_power[row_name] == i).sum()
        sum.append(counting_sum)

    sum = np.array(sum)
<<<<<<< HEAD
    df_power_curve["Time / min"] = sum / 60
    
    return df_power_curve       

# %% Plot
def plot_power_curve(df_power_curve):
    fig = plx.line(df_power_curve, x="Time / min", y="Power / W", title="Power Curve")
    fig.update_layout(xaxis_title="Time / min", yaxis_title="Power / W")
    return fig


# %%
if __name__ == "__main__":
    FILE_POWER = "../data/activity.csv"
    row_name = "PowerOriginal"
    analyze_power(FILE_POWER, row_name)
    fig = plot_power_curve(analyze_power(FILE_POWER, row_name))
    fig.show()
    
=======
    df_power_curve["Time / min"] = sum / 60  # Umwandlung in Minuten

    return df_power_curve

# %% Funktion zum Plotten der Power Curve
def plot_power_curve(df_power_curve):
    fig = plx.line(df_power_curve, x="Time / min", y="Power / W", title="Power Curve")
    fig.update_layout(xaxis_title="Time / min", yaxis_title="Power / W",  xaxis=dict(tickmode="linear", dtick=5 ))
    return fig

# %% Main-Ausführung
if __name__ == "__main__":
    FILE_POWER = "../data/activity.csv"
    row_name = "PowerOriginal"

    df_power_curve = analyze_power(FILE_POWER, row_name)
    fig = plot_power_curve(df_power_curve)
    fig.show()
>>>>>>> main


# %%
