#!/usr/bin/python3
import numpy as np
import time
class ABSC_controller:
    def __init__(self, ld, k3, chi):
        # Các tham số cố định có thể khởi tạo tại đây
        self.ld = ld
        self.k3 = k3
        self.chi = chi

    def run_bdk(self, t, x_d, y_d, theta_d, x_actual, y_actual, theta_actual, V_d, V_d_dot, oz_d):
        e_x_erorr = x_d - x_actual
        e_y_erorr = y_d - y_actual
        e_theta_erorr = theta_d - theta_actual

        # Tính toán e_r tại đây
        e = np.array([[e_x_erorr], [e_y_erorr], [e_theta_erorr]])
        o = theta_actual
        matrix_R = np.array([[np.cos(o), -np.sin(o), 0],
                             [np.sin(o), np.cos(o), 0],
                             [0, 0, 1]])
        matrix_R_T = np.transpose(matrix_R)
        e_r = np.dot(matrix_R_T, e)

        # Tính toán V và omega
        e_rx = e_r[0][0]
        e_ry = e_r[1][0]
        e_rtheta = e_r[2][0]

        c = np.cos(e_rtheta)
        s = np.sin(e_rtheta)

        dental = 0.5 - V_d

        if np.abs(e_rx) <= self.ld:
            k1 = ((-dental / (2 * self.ld ** 3)) * (np.abs(e_rx) ** 2)) + (3 * dental / (2 * self.ld))
        else:
            k1 = dental / (np.abs(e_rx))

        # Tính toán vận tốc V
        V = V_d * c + k1 * e_rx

        # Tính toán vận tốc góc omega
        z1 = e_ry + self.chi * s
        omega = (self.k3 * z1 + 2 * V_d * s - (self.chi * V_d_dot * s) / V_d + self.chi * c * oz_d) / (e_rx + self.chi * c)

        # Điều chỉnh omega trong giới hạn
        if omega >= 2.5:
            omega = 2.5
        if omega <= -2.5:
            omega = -2.5
        return V, omega
