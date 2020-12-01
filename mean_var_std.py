import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
  # convert list to numpy array ✓
    list = np.array(list)
  # convert to 3x3 matrix ✓
    list = list.reshape((3, 3)) 
  # define and assign each value here ✓
  # flattened 
    flattened_mean = np.mean(list).tolist()
    flattened_var = np.var(list).tolist()
    flattened_std = np.std(list).tolist()
    flattened_max = np.max(list).tolist()
    flattened_min = np.min(list).tolist()
    flattened_sum = np.sum(list).tolist()
  # for axis 1
    axis1_mean = np.mean(list, axis=0).tolist()
    axis1_var = np.var(list, axis=0).tolist()
    axis1_std = np.std(list, axis=0).tolist()
    axis1_max = np.max(list, axis=0).tolist()
    axis1_min = np.min(list, axis=0).tolist()
    axis1_sum = np.sum(list, axis=0).tolist()
  # for axis 2
    axis2_mean = np.mean(list, axis=1).tolist()
    axis2_var = np.var(list, axis=1).tolist()
    axis2_std = np.std(list, axis=1).tolist()
    axis2_max = np.max(list, axis=1).tolist()
    axis2_min = np.min(list, axis=1).tolist()
    axis2_sum = np.sum(list, axis=1).tolist()
  # final result
    result = {
      'mean': [axis1_mean, axis2_mean, flattened_mean],
      'variance': [axis1_var, axis2_var, flattened_var],
      'standard deviation': [axis1_std, axis2_std, flattened_std],
      'max': [axis1_max, axis2_max, flattened_max],
      'min': [axis1_min, axis2_min, flattened_min],
      'sum': [axis1_sum, axis2_sum, flattened_sum]
      }

    return result
    
