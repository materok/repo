import numpy as np
import matplotlib.pyplot as plt
from helper.laufen import MakeStats,MakeStats17

def main():

    t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
    gew,day1= np.genfromtxt('../../stats.txt', unpack=True)
    gew17,day17,month17= np.genfromtxt('../../stats_test.txt', unpack=True)

    #MxakeStats(day1,gew,2016,day,show=True)
    MakeStats17(day17,month17,gew17,2016,show=True)

if __name__=="__main__":
    main()
