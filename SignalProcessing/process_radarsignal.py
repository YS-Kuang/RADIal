import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import timeit
from rpl import RadarSignalProcessing
import sys
from DBReader.DBReader import SyncReader

root_folder ='RADIal/RECORD@2020-11-22_12.54.38'
db = SyncReader(root_folder,tolerance=40000,offset_radar = -180000,offset_scala = -40000)

RSP = RadarSignalProcessing('CalibrationTable.npy',method='RD')

rd=RSP.run(sample['radar_ch0']['data'],sample['radar_ch1']['data'],sample['radar_ch2']['data'],sample['radar_ch3']['data'])

