import numpy as np
temperature_str=np.loadtxt('ug_detect.csv',\
                            dtype=bytes,\
                            delimiter=',',\
                            skiprows=1,\
                            usecols=(1),\
                            unpack=False)
print("读取出的数组是temperature_str:\n",temperature_str)



temperature=np.ndarray(len(temperature_str))
for index in range(0,len(temperature_str)):
    item = temperature_str[index]
    if item != b"":
        item =item.decode('gb2312')
        item =float(item)
    else:
        item=None
    temperature[index] =item

#处理异常值
    for index in range(0,len(temperature)):
        item = temperature[index]
    if item >= 500.0:
        item=None
    temperature[index] =item
print("温度是：\n",temperature)


#绘制温度曲线
import matplotlib.pyplot as plt

t=np.arange(len(temperature))
plt.plot(t,temperature)
plt.plt(t,temperature,'pr')
plt.show()


#处理缺失值
def bisec(dataArray):
    for index in range(0,len(dataArray)):
        if np.isnan(dataArray[index]):
            dataArray[index]=0.5*(dataArray[index-1]+dataArray[index+1])

#test1
#引入numpy包和matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

#创建输入数据格式转换函数
def inMixDatafloat(org_array,new_array):
    for index in range (0,len(org_array)):
        item =org_array[index]
        if item != b'':
            item =item.decode('gb2312')
        item =float(item)
    else:
        item=None
    new_array[index] =item

#创建异常值转换函数
def defectsCop(data_array,threshold)
    for index in range(0,len(data_array)):
        item = data_array[index]
        if item >= float(threshold):
            item=None
        data_array[index] =item

#创建插值函数
def bisec(dataArray):
    for index in range(0,len(dataArray)):
        if np.isnan(dataArray[index]):
            if index==0:
                dataArray[index]=dataArray[index+1]
            elif index==len(dataArray):
                dataArray[index]=dataArray[index-1]
            else:
                dataArray[index]=0.5*(dataArray[index-1]+dataArray[index+1])

#读取表格数据
（humidity_str,
  gas_str,
  co_str=np.loadtxt('ug_detect.csv',\
                     dtype=bytes,\
                     delimiter=',',\
                     skiprows=1,\
                     usecols=(2,3,4),\
                     unpack=True)

#创建新数组并将数组元素处理为可处理的值
humidity =np.ndarray(len(humidity_str))
gas =np.ndarray(len(gas_str))
co =np.ndarray(len(co_str))
inMixDatafloat(humidity_str,humidity)
defectsCop(humidity,200)
inMixDatafloat(gas_str,gas)
defectsCop(gas,100)
inMixDatafloat(co_str,co)
defectsCop(co,100)


print("井下的湿度是：\n".humidity)
print("井下的瓦斯气体浓度是：\n".gas)
print("井下的一氧化碳浓度是：\n".co)

#处理数组中的空元素
bisec(humidity)
bisec(gas)
bisec(co)
print("井下的湿度是：\n".humidity)
print("井下的瓦斯气体浓度是：\n".gas)
print("井下的一氧化碳浓度是：\n".co)

#将数据写入数据文件
print("保存处理后的湿度数据文件。")
np。savetex('ug_humidity.csv',humidity,delimiter=',',fmt='%.2f')
print("保存处理后的瓦斯浓度数据文件。")
np。savetex('ug_gas.csv',gas,delimiter=',',fmt='%.2f')
print("保存处理后的一氧化碳浓度数据文件。")
np。savetex('ug_co.csv',co,delimiter=',',fmt='%.2f')


#test2
#引入pandas包
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as itp

#创建异常值转换函数
def defectsCop(data_series,threshold)
    for index in range(0,len(data_series)):
        item = data_series[index]
        if item >= float(threshold):
            item=None

