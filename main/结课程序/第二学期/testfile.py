import numpy as np

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
        return 100+(A-1)*100   #搅拌速率[100,600]rpm
    
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
        G=(sigma**1.2)*factor3*(1-C/500)**2.1  # 恢复原始计算公式
    return (speed,G)

def predict(sx):
    speed,G=sx
    if speed==0 or G==0:
        return {'状态':'失败','尺寸':'0μm','结果':'无结晶'}
    limit=G/speed
    if limit<=0:
        return {'状态':'失败','尺寸':'0μm','结果':'无结晶'}    #晶体尺寸
    size=np.exp((np.log(limit)/3)+1.8)                     #尺寸计算式
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
        for k, v in res.items():
            print(f"{k}:{v}")

def main():
    for i in range(10):
        single()

main()