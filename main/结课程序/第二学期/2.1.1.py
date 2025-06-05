import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

plt.rcParams["font.sans-serif"]=["SimHei"]   #设置字体
plt.rcParams["axes.unicode_minus"]=False     #该语句解决图像中的“-”负号的乱码问题

def roll_poinnt(mode):
    '''六面骰子产生[1,6]'''
    A=np.random.randint(1,7)
    if mode=='sigma':
        return 1.05+(A-1)*0.05   #过饱和度取值[1.05,1.30]
    elif mode=='T':
        return 40+(A-1)*10       #温度[40,90]摄氏度
    elif mode=='C':
        return (A-1)*100         #杂质浓度[0,500]ppm
    elif mode=='R':
        return 100 + (A-1)*100   #搅拌速率[100,600]rpm
    else:
        return False
    
def f1(sigma, T, C, R):
    '''
    计算成核速率speed
    10**24:前因子，与分子碰撞频率和界面张力相关
    factor1:描述过饱和度sigma对成核能垒的影响。
    factor2:描述温度T对动力学的影响。
    '''
    factor1=np.exp(-16/(np.log(sigma)**2))
    factor2=np.exp(-5800/(8.314*(T+273.15)))
    speed=(10**24)*factor1*factor2 
    #搅拌影响&杂质抑制
    factor3=0.8+0.2*np.tanh(0.01*(R-300))
    if C>300:
        G=0
    else:
        G=(2.3**-8)*(sigma**1.2)*factor3*(1-C/500)**2.1
    return speed,G

def predict(sx):
    speed,G=sx
    if speed==0 or G==0:
        return {"状态":"无结晶","尺寸":"0 μm","结果":"无结晶"}    #晶体尺寸
    size=(G/speed)**(1/3)*(10**6)  # 从速率比推导特征尺寸（单位：μm）
    # 尺寸分布宽度（经验公式）
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
    endresult={"状态":"成功","尺寸":f"{size:.1f}±{std:.1f} μm","结果":result}
    return endresult

def visial():
    # 1. 生成 σ 和 T 的网格
    sigma_range = np.linspace(1.05, 1.30, 20)   # 20 个过饱和度点
    T_range = np.linspace(40, 90, 20)           # 20 个温度点（摄氏度）
    Sigma, T = np.meshgrid(sigma_range, T_range)

    # 2. 准备存储“晶体尺寸”的数组
    Size = np.zeros_like(Sigma)

    # 3. 对网格中每一个 (σ, T) 点，使用 roll_poinnt 随机取 C、R，算出尺寸
    for i in range(Sigma.shape[0]):
        for j in range(Sigma.shape[1]):
            σ_val = Sigma[i, j]
            T_val = T[i, j]

            # 随机生成当前点的“杂质浓度 C” 和 “搅拌速率 R”
            C_val = roll_poinnt('C')    # 返回 {0, 100, 200, 300, 400, 500} 中的某个值
            R_val = roll_poinnt('R')    # 返回 {100, 200, 300, 400, 500, 600} 中的某个值

            # 计算成核速率 speed 和生长速率 G
            speed, G = f1(σ_val, T_val, C_val, R_val)

            # 调用 predict 得到晶体尺寸（如果无结晶，size=0）
            result_dict = predict((speed, G))
            if result_dict["状态"] == "成功":
                # 从类似 "120.5±36.2 μm" 中提取主尺寸数值
                size_str = result_dict["尺寸"]     # e.g. "120.5±36.2 μm"
                size_num = float(size_str.split("±")[0])
                Size[i, j] = size_num
            else:
                Size[i, j] = 0.0

    # 4. 下面开始画 3D 曲面：sigma (x) - T (y) - Size (z)
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制曲面
    surf = ax.plot_surface(Sigma, T, Size, cmap='viridis', edgecolor='none')

    # 坐标轴标签
    ax.set_xlabel('过饱和度 σ', fontsize=12)
    ax.set_ylabel('温度 T (℃)', fontsize=12)
    ax.set_zlabel('晶体尺寸 (μm)', fontsize=12)
    ax.set_title('含随机 C、R 的晶体尺寸三维分布', fontsize=14)

    # 添加颜色条（表示尺寸大小）
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='尺寸 (μm)')

    plt.tight_layout()
    plt.show()

def main():
    try:
        print("结晶过程概率模拟系统")
        print("1. 单次模拟") 
        print("2. 参数空间可视化")
        print("程序已启动，等待用户输入...")
        
        while True:
            choice = input("请选择操作 (1/2): ").strip()
            print(f"用户选择了: {choice}")
            
            if choice in ("1", "2"):
                break
            print("输入无效，请重新输入1或2")
        
        if choice == "1":
            # 单次模拟
            σ = roll_poinnt("sigma")
            T = roll_poinnt("T")
            C = roll_poinnt("C")
            R = roll_poinnt("R")
            
            print(f"\n骰子结果: σ={σ:.2f}, T={T}°C, C={C} ppm, R={R} rpm")
            speed, G = f1(σ, T, C, R)
            res = predict((speed, G))
            print("\n结晶预测结果:")
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == "2":
            visial()
            
    except Exception as e:
        print(f"程序运行出错: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
