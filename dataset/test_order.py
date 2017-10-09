import numpy as np

old_data = np.load('data.npy')
new_data = np.load('data_local.npy')

print(np.allclose(old_data, new_data))
