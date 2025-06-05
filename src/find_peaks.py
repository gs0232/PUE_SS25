<<<<<<< HEAD
#%% Read CSV file with EKG data
=======
#%%
>>>>>>> main
import pandas as pd
import plotly.express as plx

<<<<<<< HEAD
# %%

def find_peaks(FILE_EKG, row_name):
    indices_peaks = []
    voltage = FILE_EKG[str(row_name)]
    
    threshold = 0.9 * FILE_EKG[str(row_name)].max()  # Weniger streng
    min_peak_distance = 200          # Realer Abstand (z. B. bei 1000 Hz ~ 0.2 s)

    for i in range(1, len(voltage) - 1):
        if voltage.iloc[i] >= voltage.iloc[i - 1] and voltage.iloc[i] >= voltage.iloc[i + 1]:
            if voltage.iloc[i] > threshold:
                if not indices_peaks or i - indices_peaks[-1] > min_peak_distance:
                    indices_peaks.append(i)
    
    return indices_peaks


# %% Plot

# plot the peaks of df_ekg
def plot_peaks(FILE_EKG, row_name, indices_peaks, max_values):
    indices_peaks_small = [i for i in indices_peaks if i < max_values]
    fig = plx.line(FILE_EKG.iloc[0:max_values], x="Time / sec", y=str(row_name), title="EKG Data with Peaks")
    fig.add_scatter(x=FILE_EKG.iloc[indices_peaks_small]["Time / sec"], 
                    y=FILE_EKG.iloc[indices_peaks_small][str(row_name)], 
                    mode='markers', 
                    marker=dict(color='red', size=10), 
                    name='Peaks')
    return fig

# %%
if __name__ == "__main__":
    FILE_EKG = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep="	", names=["Voltage / mV", "Time / sec"])
    df_ekg = FILE_EKG.copy()
    indices_peaks = find_peaks(df_ekg, "Voltage / mV")
    fig_peaks = plot_peaks(df_ekg, "Voltage / mV", indices_peaks, 5000)
    fig_peaks

=======

def find_peaks(df_ekg, threshold, min_peak_distance):

    list_of_index_of_peaks = []

    last_peaks_index = 0

    for index, row in df_ekg.iterrows():
        if index < df_ekg.index.max() - 1:
  #wenn row[voltage in mv] größer als  vorherige und nachfolgende ist
           if row["Voltage in mV"] >= df_ekg.iloc[index - 1]["Voltage in mV"] and row["Voltage in mV"] >= df_ekg.iloc[index + 1]["Voltage in mV"]:
  #dann füge aktuellen index der liste hinzu

              if row["Voltage in mV"] > treshold and index - last_peaks_index > min_peak_distance:
  #wenn treshold überschritten wird und auch der letzte gespeicherte index mindestens den abstand hat
                 list_of_index_of_peaks.append(index)
                 last_peaks_index = index
    return list_of_index_of_peaks

#test 
if "__main__" == __name__:
    
    df_ekg = pd.read_csv("../data/ekg_data/01_Ruhe.txt", sep = "\t", names = ["Voltage in mV", "Time in ms"])
    df_ekg = df_ekg.iloc[0:5000]
    treshold = 0.95 * df_ekg["Voltage in mV"].max()
    min_peak_distance = 10

    list_of_index_of_peaks = find_peaks(df_ekg, treshold, min_peak_distance)    
#%%
import plotly.express as plx

#make the folder wider
fig = plx.line(df_ekg, x = "Time in ms", y = "Voltage in mV", title = "EKG Data")
#mark peaks with red dots
#make the figure wider
plx.defaults.width = 600
#less wider 
plx.defaults.height = 400
fig.add_scatter(x=df_ekg.iloc[list_of_index_of_peaks]["Time in ms"],
                 y=df_ekg.iloc[list_of_index_of_peaks]["Voltage in mV"],
                 mode='markers',
                 marker=dict(color='red', size=10),
                 name='Peaks')
fig
>>>>>>> main
# %%
