import neurokit2 as nk

# Generate 15 seconds of ECG signal (recorded at 250 samples/second)
ecg = nk.ecg_simulate(duration=15, sampling_rate=250, heart_rate=70)

# Process it
signals, info = nk.ecg_process(ecg, sampling_rate=250)

# Visualise the processing
nk.ecg_plot(signals, info)
# Print the info dictionary to see extracted features
print(info) 
# print signals head to see the processed signals
print(signals.head())
