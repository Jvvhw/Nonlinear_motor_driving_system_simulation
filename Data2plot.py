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

x_Duty = []
x_Duty = [round(Duty_list[i][0],3) for i in range(9,len(Duty_list),10)] # 시간, 0.01초 단위
y_Duty = [round(Duty_list[i][1],3) for i in range(9,len(Duty_list),10)] # duty

tmp_list = fileopen('Vpdata_I=0.csv')
Vp_list = convert_to_floats(tmp_list)

x_Vp = [round(Vp_list[i][0],3) for i in range(9,len(Vp_list),10)] 
y_Vp = [round(Vp_list[i][1],3) for i in range(9,len(Vp_list),10)] #Vp_avg


Ideal_Vp = []
Vp_error = []

for i in range(len(y_Duty)):
    Ideal_Vp.append(Vdc*(y_Duty[i] - 0.5)) # duty에 따른 이상적인 Vp 계산
    Vp_error.append(y_Vp[i]-Ideal_Vp[i])   # 실제 Vp와의 차이를 모두 계산

    
#plt.scatter(x_Duty,y_Duty,label = 'Duty')
plt.scatter(x_Vp,Ideal_Vp,label = 'Vp_Ideal')
plt.scatter(x_Vp,y_Vp,label = 'Vp_avg')
plt.plot(x_Vp,Vp_error,label = 'Vp_error')
plt.xlabel('Time')
plt.legend()
plt.show()











        
