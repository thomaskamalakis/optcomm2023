import numpy as np
import matplotlib.pyplot as plt

theta_i = np.linspace(0, np.pi / 2, 100)
n1 = 2
n2 = 1

sin_theta_t = n1 / n2 * np.sin(theta_i)
theta_t = np.arcsin( sin_theta_t )

theta_i_deg = theta_i * 180 / np.pi
theta_t_deg = theta_t * 180 / np.pi

plt.close('all')
plt.figure()
plt.plot(theta_i_deg, theta_t_deg)
plt.xlabel('theta_i [deg]')
plt.ylabel('theta_t [deg]')

