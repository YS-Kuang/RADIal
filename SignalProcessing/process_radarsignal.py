import pandas as pd
import os.path as osp 
import numpy as np
import matplotlib.pyplot as plt
import os
import h5py
import json

root_dir = "E:\hiwi\RADIal"
save_file = "E:\hiwi\data_procesing"
data_dir = "E:\\hiwi\\RADIal"
pcl_dir = "E:\\hiwi\\RADIal\\radar_PCL"
print(pcl_dir)
labels = pd.read_csv(os.path.join(root_dir,'labels.csv')).to_numpy()

# Gather each input entries by their sample id
unique_ids = np.unique(labels[:,0])
label_dict = {}
for i,ids in enumerate(unique_ids):
    sample_ids = np.where(labels[:,0]==ids)[0]
    label_dict[ids]=sample_ids
sample_keys = list(label_dict.keys())

index =np.argwhere(labels=='RECORD@2020-11-22_11.24.02')
print(index)

#0,numsample 10,11,12,13 radar_R_m,radar_A_deg,radar_D_mps,radar_P_db 

#label_data = labels[:,[0,10,11,12,13]]
#np.save(osp.join(save_file,'lable.npy'), label_data)
labels = np.load(os.path.join(save_file,'lable.npy'),allow_pickle=True)
print(labels.shape)
"""
eps = np.finfo(float).eps
print(max(labels[:,4]))
print(min(labels[:,4]))
print(np.log10(max(labels[:,4])))
print(np.log10(min(abs(labels[:,4]))))
"""
#RAD power
print(labels[0,:])
RANGE_Resolution = np.around((103/512),2)
Azimuth_Resolution =np.around((180/751),1)
print(Azimuth_Resolution)
Doppler_index =6
Range_index= 3
Azimuth_index =8
a=[1,2,3,4,5,6]
print(a[1:4])

number_sample = labels[:,0]
#radar_name = os.path.join(self.root_dir,'radar_FFT',"fft_{:06d}.npz".format(sample_id))
print(number_sample[0])
radar_fft = os.path.join(root_dir,'radar_FFT',"fft_{:06d}.npy".format(number_sample[0]))
print(radar_fft)
