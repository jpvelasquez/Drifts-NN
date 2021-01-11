import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta



def GetAveragedExBVertical(directory, filename, str_month):
    #filename ='jul20200101_150km.001.hdf5' 
    file_hf5 = directory + '/' + filename #'../Data-JULIA/January-2020/150-km-Echoes/' + filename
    hf = h5py.File(file_hf5, 'r')
    if str_month == 'Agosto':
        num_month=8
    with h5py.File(file_hf5, 'r') as f:
        g = f.visit(print)
        #print(g)

    snl = hf['Data/Table Layout/']['snl']
    vipe1 = hf['Data/Table Layout/']['vipe1']
    vipn1 = hf['Data/Table Layout/']['vipn1']
    #Te = hf['Data/Table Layout/']['te']
    days = np.array(hf['Data/Table Layout/']['day'],dtype=int)
    year = np.array(hf['Data/Table Layout/']['year'],dtype=int)
    month = np.array(hf['Data/Table Layout/']['month'],dtype=int)
    hour = np.array(hf['Data/Table Layout/']['hour'],dtype=int)
    minutes = np.array( hf['Data/Table Layout/']['min'],dtype=int)
    seconds = np.array(hf['Data/Table Layout/']['sec'],dtype=int)
    rango = hf['Data/Table Layout/']['gdalt']
    #NeFlat = np.array(Ne)
    print(snl.shape)
    print(rango.shape)

#########################################################

#converted_value = getattr(value, "tolist", lambda: value)()
    days = getattr(days, "tolist", lambda: days)()
    year = getattr(year, "tolist", lambda: year)()
    month = getattr(month, "tolist", lambda: month)()
    hour = getattr(hour, "tolist", lambda: hour)()
    minutes = getattr(minutes, "tolist", lambda: minutes)()
    seconds = getattr(seconds, "tolist", lambda: seconds)()
    rango = getattr(rango, "tolist", lambda: rango)()
    time_vector = []
    date_list = [] # list for datetime objects
    datetimeFormat = '%Y-%m-%d %H:%M:%S'
    for y, m, d,h, mmins, sec in zip(year,month,days,hour,minutes,seconds):
        date_string = '%d-%02d-%02d %02d:%02d' % (y,m,d,h,mmins)
        #print(type(sec), type(mmins), type(d), type(h), type(y))
        date = datetime.datetime(y,m,d,h,mmins, sec)#, datetimeFormat)
        time_vector.append(date_string)
        date_list.append(date)
    #print date
    index = pd.DatetimeIndex(date_list) - pd.Timedelta(hours=5)

#########################################################

    list_of_tuples = list(zip(rango,vipe1, vipn1, index))  
    df = pd.DataFrame(list_of_tuples, columns = ['rango', 'vipe1', 'vipn1', 'time'], index=index)
    #df.set_index(index)
    #drifts = pd.DataFrame()
    r_min = 135 # (km)
    r_max = 167 # (km)
    #df['time'] = df.index
    condition1 = df['rango']< r_max
    condition2 = df['rango'] > r_min
    df_speed_range = df.loc[condition1 & condition2]

#########################################################

    #df_speed_range.index = df_speed_range.time
    #df_speed_range.index = df_speed_range.index - pd.Timedelta(hours=5)
#########################################################

    #df_5min_mean = df_speed_range.rolling('5T')[['vipe1','vipn1']].mean()
    df_5min_mean = df_speed_range[['vipe1','vipn1']].resample('5T').mean()
    #df_5min_mean = df_speed_range[['vipn1']].resample('5T').mean()
    
    #time1 = datetime.datetime(2020, num_month, df_speed_range.index.day[0], 10, 0,0) #- pd.Timedelta(hours=5)
    #time2 = datetime.datetime(2020, num_month, df_speed_range.index.day[0], 16, 0, 0) #- pd.Timedelta(hours=5)
    #print(time1)
    #print(time2)
    #df_5min_mean.head(3)
    #df_ExB_vertical = df_5min_mean.loc[time1:time2].fillna(method='ffill')
    df_ExB_vertical = df_5min_mean.fillna(method='ffill')
    #df_ExB_vertical.index = df_ExB_vertical.index #- pd.Timedelta(hours=5)
##########################################################
    return df_ExB_vertical

