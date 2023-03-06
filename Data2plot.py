import csv
import matplotlib.pyplot as plt
import numpy as np

Vdc = 300
Vdc_half = 0.5*Vdc

'''
-------------------------------------------------------------------------------------------------------------------------
'''

#csv파일을 열어서 리스트로 리턴하는 함수
def fileopen(filename):
    data = list()
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    return data

#2차원 리스트 모든 원소 실수로 변환
def convert_to_floats(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
    return matrix


tmp_list = fileopen('Duty.csv')
Duty_list = convert_to_floats(tmp_list)

x_Duty = [round(i[0],2) for i in Duty_list] #시간, 0.01초 단위
y_Duty = [round(i[1],2) for i in Duty_list]

tmp_list = fileopen('Vpdata_I=0.csv')
Vp_list = convert_to_floats(tmp_list)

x_Vp = [round(i[0],2) for i in Vp_list] #시간, 0.01초 단위
y_Vp = [round(i[1],2) for i in Vp_list] 

for i in range(len(y_Vp)): # period average block 특성상 정확히 Duty가 바뀌는 지점에서는 Tsamp만큼의 딜레이가 발생함으로 0.01초 뒤의 값과 똑같이 맞춰
    if i > 95: break

    elif i % 5 == 0:
        y_Vp[i] = y_Vp[i+1]

Ideal_Vp = []
Vp_error = []

for i in range(len(y_Duty)):
    Ideal_Vp.append(Vdc*(y_Duty[i] - 0.5))
    Vp_error.append(y_Vp[i]-Ideal_Vp[i])


#plt.scatter(x_Duty[5:95],y_Duty[5:95],label = 'Duty')
plt.scatter(x_Vp[5:95],Ideal_Vp[5:95],label = 'Vp_Ideal')
plt.scatter(x_Vp[5:95],y_Vp[5:95],label = 'Vp_avg')
plt.plot(x_Vp[5:95],Vp_error[5:95],label = 'Vp_error')
plt.xlabel('Time')
plt.legend()
plt.show()







        
