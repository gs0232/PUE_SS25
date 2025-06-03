#%% Read CSV file with EKG data
import pandas as pd
import plotly.express as plx

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

# %%
