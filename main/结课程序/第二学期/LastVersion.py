import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["font.sans-serif"]=["SimHei"]   #设置字体
plt.rcParams["axes.unicode_minus"]=False     #该语句解决图像中的“-”负号的乱码问题

def roll_point(mode):
    '''六面骰子产生[1,6]'''
    A=np.random.randint(1,7)
    if mode=='sigma':
        return 1.05+(A-1)*0.05   #过饱和度取值[1.05,1.30]
    elif mode=='T':
        return 40+(A-1)*10       #温度[40,90]摄氏度
    elif mode=='C':
        return (A-1)*100         #杂质浓度[0,500]ppm
    elif mode=='R':
        return 100+(A-1)*100     #搅拌速率[100,600]rpm
    
def f1(sigma,T,C,R):
    '''
    计算成核速率speed
    10**24:前因子，与分子碰撞频率和界面张力相关
    factor1:描述过饱和度sigma对成核能垒的影响。
    factor2:描述温度T对动力学的影响。
    '''
    factor1=(sigma-1.0)**2.5
    factor2=np.exp(-5800/(8.314*(T+273.15)))
    speed=factor1*factor2
    #搅拌影响&杂质抑制
    factor3=0.8+0.2*np.tanh(0.01*(R-300))
    if C>300:
        G=0
    else:
        G=(sigma**1.2)*factor3*(1-C/500)**2.1
    return (speed,G)

def predict(sx):
    speed,G=sx
    if speed==0 or G==0:
        return {'状态':'失败','尺寸':'0μm','结果':'无结晶'}
    limit=G/speed
    if limit<=0:
        return {'状态':'失败','尺寸':'0μm','结果':'无结晶'}    #晶体尺寸
    size=np.exp((np.log(limit)/3)+1.6)                     #尺寸计算式
    if size<50:
        std=0.3*size
    else:
        std=0.2*size
    # 结晶形态判断
    if size>100:
        result='粗大棱柱状'
    elif 50<size<=100:
        result='片状聚集'
    else:
        result='微晶粉末'
    return {'状态':'成功','尺寸':f'{size:.1f}±{std:.1f} μm','结果':result}

def single():
        '''单次模拟情况输出'''
        sigma=roll_point("sigma")
        T=roll_point("T")
        C=roll_point("C")
        R=roll_point("R")
        print(f"\n骰子结果:Sigma={sigma:.2f},T={T}°C,C={C}ppm,R={R}rpm")
        res=predict(f1(sigma,T,C,R))
        print("\n结晶预测结果:")
        for k, v in res.items():
            print(f"{k}:{v}")

def visial():
    sigma_range=np.linspace(1.05, 1.30, 50)
    T_range=np.linspace(40, 90, 50)
    Sigma,T=np.meshgrid(sigma_range,T_range)
    # 存储"晶体尺寸"的数组
    Size = np.zeros_like(Sigma)
    for i in range(Sigma.shape[0]):
        for j in range(Sigma.shape[1]):
            sigmavalue=Sigma[i,j]
            Tvalue=T[i,j]
            Cvalue=roll_point("C")
            Rvalue=roll_point("R")
            result_dict=predict(f1(sigmavalue,Tvalue,Cvalue,Rvalue))
            if result_dict['状态']=='成功':
                size_str=result_dict['尺寸']
                size_num=float(size_str.split("±")[0])
                Size[i,j]=size_num
            else:
                Size[i, j] = 0.0
    # 创建3D图形
    fig=plt.figure(figsize=(12, 8))
    ax=fig.add_subplot(111,projection='3d')
    surf=ax.plot_surface(Sigma,T,Size,cmap='viridis',edgecolor='none',alpha=0.8)
    fig.colorbar(surf,ax=ax,shrink=0.5,aspect=5,label='晶体尺寸 (μm)')
    ax.contourf(Sigma,T,Size,zdir='z',offset=Size.min()-10,cmap='coolwarm',alpha=0.3)
    # 坐标轴标签
    ax.set_xlabel('过饱和度')
    ax.set_ylabel('温度T')
    ax.set_zlabel('晶体尺寸')
    ax.set_title('晶体尺寸参数响应面 (C, R随机)')
    plt.tight_layout()
    plt.show()

print("结晶过程概率模拟(键入0以退出该程序)")
print("1.单次模拟") 
print("2.参数空间可视化")
while True:
    choice=input('请选择(1/2):')
    if choice=='1':
        single()
        break
    elif choice=='2':
        visial()
        break
    elif choice=='0':
        break
    else:
        print('输入错误，请重新输入')