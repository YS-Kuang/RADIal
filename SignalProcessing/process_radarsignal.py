from DBReader import SyncReader
from DBReader.SensorsReaders import CANDecoder
import matplotlib.pyplot as plt

db = SyncReader('RADIal/RECORD@2020-11-22_12.28.47')
# if you leave the default parameters, the master sensor is the radar as it is the slowest one
# if you are interested by only the camera and laser scanner, you can call:
# db = SyncReader('dataset_path',master='camera',tolerance=200000)

# use print_info function to get all the details of the database content
db.print_info()
print('')

# Create an iterator on the dataset
ite = iter(db)

# ALl data are return in a dictionay
data=next(ite)
print(data.keys())

# and then each sensor returns a dictionary
print(data['camera'].keys())
print('')

plt.plot(data['scala']['data'][:,1],data['scala']['data'][:,0],'r.')
plt.xlim(-40,40)
plt.ylim(0,100)
plt.grid()
