#!/usr/bin/python3
import numpy as np
import time
import pandas as pd
from bdk_PID import *
#from read_data_encoder import *
from position_encoder import *

# Đọc dữ liệu từ tệp Excell
file_path = 'trajectory.xlsx'
data = pd.read_excel(file_path)
t_d = data.iloc[1:, 0].values  # Lấy từ cột thứ 0,  bắt đầu từ 0
#print(t_d)
x_excel_d = data.iloc[1:, 1].values  
y_excel_d = data.iloc[1:, 2].values 
theta_excel_d = data.iloc[1:, 3].values
V_excel_d = data.iloc[1:, 4].values 
oz_excel_d = data.iloc[1:, 5].values  
V_excel_d_dot = data.iloc[1:, 6].values

ABSC = ABSC_controller(ld=0.4, k3=13.1, chi=0.413)

def main_program():
    t_i = t_count = 0
    x0 = y0 = theta0 = 0
    for t, x_d, y_d, theta_d, V_d, oz_d, V_d_dot  in zip (t_d, x_excel_d, y_excel_d, theta_excel_d, V_excel_d, oz_excel_d, V_excel_d_dot):        
        start_time = time.time()
        t_i = t_i + t_count
        w1, w2 = encoder_callback() ###
        x_actual, y_actual, theta_actual = get_position(x0, y0, theta0, w1, w2)
        V, omega = ABSC.run_bdk(t, x_d, y_d, theta_d, x_actual, y_actual, theta_actual, V_d, V_d_dot, oz_d) 

        print(V, omega)
        time.sleep(0.0925)
        end_time = time.time()
        t_count = end_time - start_time
        x0 = x_actual
        y0 = y_actual
        theta0 = theta_actual
if __name__ == "__main__":
    main_program()
