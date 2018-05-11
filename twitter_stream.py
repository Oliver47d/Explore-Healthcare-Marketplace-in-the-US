# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:15:56 2018

@author: Albert
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Start_year=2014
End_year=2018

bencostsharing_2014 = pd.read_csv('2014/Benefits_Cost_Sharing_PUF.csv', dtype='unicode')
crosswalk_2016 = pd.read_csv('2016/plan-id-crosswalk-puf.csv', dtype='unicode')
print (BCS_PUF2014.head())