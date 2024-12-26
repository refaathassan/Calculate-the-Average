import numpy as np
ls=[1,2,3,4,5]
def ava(list):
    return np.sum(np.array(list))/len(list)
print(ava(ls))