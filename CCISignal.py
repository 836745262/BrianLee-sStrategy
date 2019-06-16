import talib as ta
import numpy as np
import pandas as pd

"""
将kdj策略需要用到的信号生成器抽离出来
"""

class CCISignal():

    def __init__(self):
        self.author = 'BrianLee'

    def CCIsignal(self, am, paraDict):
        CCIPeriod = paraDict["CCIPeriod"]
        up = 120
        down = -120
        CCI = ta.CCI(am.high,am.low,am.close,CCIPeriod)

        breakup = CCI[-1]>up and CCI[-2]<=up
        breakdn = CCI[-1]<down and CCI[-2]>=down 
        threshold = paraDict['threshold']
        CrossSignal = 0
        upcount = 0
        downcount = 0
        if breakup :
            CrossSignal = 1
            upcount += 1
            if upcount == threshold:
                CrossSignal = -1
                upcount = 0
        elif breakdn :
            CrossSignal = -1
            downcount += 1
            if downcount == threshold:
                CrossSignal = 1
                downcount = 0
        else:
            CrossSignal = 0
        

        
        return CrossSignal, up,CCI,down
    
        