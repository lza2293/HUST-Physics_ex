import numpy as np

def calc_sigma(l):
    l_mean = np.mean(l)
    return np.sqrt(np.sum([(item - l_mean) ** 2 for item in l]) / (len(l) - 1))

def remove_data_out3sigma(l):
    l_std = calc_sigma(l)
    l_mean = np.mean(l)
    l = l[l <= l_mean + 3 * l_std]
    l = l[l >= l_mean - 3 * l_std]
    return l

tp          = {3:4.3, 4:3.18, 5:2.78, 6:2.57,
                7:2.45, 8:2.37, 9:2.31, 10:1.96}

T = 5
len_string  = np.array([74.05, 73.70, 73.75, 73.35, 73.90])
time_5T     = np.array([8.82, 8.85, 8.66, 8.78, 8.78])
len_string  = len_string / 100

len_string  = remove_data_out3sigma(len_string)
time_5T     = remove_data_out3sigma(time_5T)

avg_string  = np.mean(len_string)
avg_time_5T = np.mean(time_5T)

ua_string   = tp[len(len_string)] * calc_sigma(len_string) / np.sqrt(len(len_string))
ua_time_5T  = tp[len(time_5T)] * calc_sigma(time_5T / T) / np.sqrt(len(time_5T))

ub_string   = 0.001
ub_time_5T  = 0.01

u_string    = np.sqrt(ua_string ** 2    + ub_string ** 2)
u_time_5T   = np.sqrt(ua_time_5T ** 2   + ub_time_5T ** 2)

ur_g        = np.sqrt(np.square(u_string / avg_string) + 
                        np.square(2 * u_time_5T / avg_time_5T))

avg_g = 4 * T * T * np.pi * np.pi * avg_string / (avg_time_5T ** 2)

print('Calculated ur_g = {}'.format(ur_g))
print('Calculated g={}'.format(avg_g))
print('Estimated g falls in range({}, {})'.format(avg_g*(1-ur_g), avg_g*(1+ur_g)))
print('Phyphox g : {}'.format(9.63))


