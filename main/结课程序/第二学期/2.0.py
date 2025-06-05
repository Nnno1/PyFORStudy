import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 添加3D绘图支持

def roll_dice(dice_type):
    face = np.random.randint(1,7)
    if dice_type == "σ":
        return 1.05 + (face-1)*0.05  # 线性映射
    elif dice_type == "T":
        return 40 + (face-1)*10
    elif dice_type == "C":
        return (face-1)*100  # 0-500 ppm
    elif dice_type == "R":
        return 100 + (face-1)*100  # 100-600 rpm
    else:
        raise ValueError("Unknown dice type")

def calculate_crystallization(σ, T, C, R):
    # 计算成核速率
    J = 1e24 * np.exp(-16/(np.log(σ)**2)) * np.exp(-5800/(8.314*(T+273.15)))

    # 计算生长速率修正因子（搅拌影响）
    stir_factor = 0.8 + 0.2*np.tanh(0.01*(R-300))

    # 杂质抑制效应
    if C > 300:  # ppm
        G = 0
    else:
        G = 2.3e-8 * σ**1.2 * stir_factor * (1 - C/500)**2.1

    return J, G

def predict_crystal(J, G):
    # 晶体平均尺寸（μm）
    if J == 0 or G == 0:
        return {"status": "无结晶", "avg_size": "0 μm", "morphology": "无结晶"}

    avg_size = (G/J)**(1/3) * 1e6  # 从速率比推导特征尺寸

    # 尺寸分布宽度
    std_dev = 0.3 * avg_size if avg_size < 50 else 0.2*avg_size

    # 结晶形态判断
    if avg_size > 100:
        morphology = "粗大棱柱状"
    elif 50 < avg_size <=100:
        morphology = "片状聚集"
    else:
        morphology = "微晶粉末"

    return {"status": "成功",
            "avg_size": f"{avg_size:.1f}±{std_dev:.1f} μm",
            "morphology": morphology}

def visualize_parameter_space():
    # 生成参数网格
    σ_range = np.linspace(1.05, 1.30,20)
    T_range = np.linspace(40, 90, 20)

    # 计算响应面
    sizes = []
    for σ in σ_range:
        for T in T_range:
            J, G = calculate_crystallization(σ, T, C=0, R=300)
            res = predict_crystal(J, G)
            sizes.append(float(res['avg_size'].split('±')[0]) if res['status']=='成功' else 0)

    # 3D可视化
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(σ_range, T_range)
    Z = np.array(sizes).reshape(20,20)
    
    # 显式创建3D表面图
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('过饱和度 σ')
    ax.set_ylabel('温度 (°C)')
    ax.set_zlabel('晶体尺寸 (μm)')
    plt.title('结晶尺寸参数响应面 (无杂质, 300 rpm)')
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
            σ = roll_dice("σ")
            T = roll_dice("T")
            C = roll_dice("C")
            R = roll_dice("R")
            
            print(f"\n骰子结果: σ={σ:.2f}, T={T}°C, C={C} ppm, R={R} rpm")
            J, G = calculate_crystallization(σ, T, C, R)
            res = predict_crystal(J, G)
            print("\n结晶预测结果:")
            for k, v in res.items():
                print(f"{k}: {v}")

        elif choice == "2":
            visualize_parameter_space()
            
    except Exception as e:
        print(f"程序运行出错: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
