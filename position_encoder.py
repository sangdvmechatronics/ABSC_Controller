#!/usr/bin/python3
import numpy as np

# khoang thoi gian lay mau
def get_position(x0, y0, theta0, w1, w2):
    dt = 0.1
    # ban kinh banh xe
    r = 0.03
    # khoang cach 
    l = 0.4
    w1 = w1 * 2*np.pi / 60
    w2 = w2 * 2*np.pi / 60
    thetaf = theta0 + (r*(w2-w1)*dt/(2*l))
    c = np.cos(thetaf)
    s = np.sin(thetaf)
    xf = x0 + r/2 * ((w1 + w2) *c *dt)
    yf = y0 + r/2 * ((w1 + w2 ) *s *dt)
    return xf, yf, thetaf
