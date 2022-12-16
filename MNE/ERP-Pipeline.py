# This script uses MNE to analyze EEG data. It is a work in progress.
#!/usr/bin/MNE python


import mne 
import numpy as np
import os
import matplotlib as plt


## Loading and plotting raw data

# Set the folder path
folder_path = 'path_to_file'

# create an empty list to store the raw data
raw_data = []

# loop through the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is a BrainVision (.vhdr) file
    if filename.endswith(".vhdr"):
        # construct the full file path
        file_path = os.path.join(folder_path, filename)
        # load the data from the BrainVision file
        raw = mne.io.read_raw_brainvision(file_path)
        # add the raw data to the list
        raw_data.append(raw)

# combine the raw data into a single raw object
raw = mne.concatenate_raws(raw_data)

print(raw.info)
raw.plot_psd(fmax = 50)
raw.plot(duration=5, n_channels=len(raw.ch_names))

