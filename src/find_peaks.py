#%%
import pandas as pd


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
# %%
