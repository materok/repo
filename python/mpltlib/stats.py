import numpy as np
import matplotlib.pyplot as plt
from helper.laufen import *

def main():

    t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
    gew,day1= np.genfromtxt('../../stats.txt', unpack=True)

    makeStats(day1,gew,2016,day,show=True)

if __name__=="__main__":
    main()
