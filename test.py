import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
e = np.exp(2)
def qiujifen(lower, upper):

    val, err =  quad (lambda x: e*2*np.sin(2*x)*np.cos(x),
                    lower,
                    upper)
    print('积分结果:', val, ',损失值:', err)
    return val, err

if __name__ == '__main__':
    val,err=qiujifen( -1 , 2)
    print(val)
    x=np.linspace(0,3,100)
    picture_1 = np.exp(x)
    plt.plot(x, picture_1)
    plt.show()
