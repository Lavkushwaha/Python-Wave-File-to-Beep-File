from scipy.io import wavfile
import numpy as np
import winsound; 

duration = 300 


fs, data = wavfile.read('./song.wav')


for mydata in data:
    print(np.array(mydata)[0])
    if(mydata[0]>500):
        winsound.Beep(mydata[0], duration)