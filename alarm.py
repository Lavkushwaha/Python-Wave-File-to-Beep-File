import winsound; 
import os

frequency = 1000  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second

for i in range(50):
    if i > 1:
        frequency = 300 * i
        winsound.Beep(frequency, duration)
    # winsound.PlaySound('SystemExit', winsound.SND_ALIAS)

exit()