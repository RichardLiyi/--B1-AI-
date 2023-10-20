import os
import numpy as np
import pandas as pd
import skrf

# 输入文件夹路径和输出文件夹路径
input_folder = 'D:\\桌面\\先进计算大赛\\B1-AI微带线建模\\专题赛数据\\s2p'
output_folder = 'D:\\桌面\\先进计算大赛\\B1-AI微带线建模\\专题赛数据\\s2p_To_csv'

# 设置pandas显示选项
pd.set_option('display.float_format', '{:.20f}'.format)

# 获取所有s2p文件的路径
file_list = os.listdir(input_folder)
s2p_files = [os.path.join(input_folder, file) for file in file_list if file.endswith('.s2p')]

# 逐个处理s2p文件
for i, s2p_file in enumerate(s2p_files):
    # 读取S参数数据
    network = skrf.Network(s2p_file)
    s_params = network.s
    freqs = network.f

    # 将S参数数据转换为DataFrame格式
    columns = ["freq (GHz)", "S11_real", "S11_imag", "S21_real", "S21_imag", "S12_real", "S12_imag", "S22_real",
               "S22_imag"]
    data = np.column_stack((freqs, s_params[:, 0, 0].real, s_params[:, 0, 0].imag,
                            s_params[:, 1, 0].real, s_params[:, 1, 0].imag,
                            s_params[:, 0, 1].real, s_params[:, 0, 1].imag,
                            s_params[:, 1, 1].real, s_params[:, 1, 1].imag))
    df = pd.DataFrame(data=data, columns=columns)

    # 构造输出文件路径，保持与输入文件相同的文件名
    base_name = os.path.basename(s2p_file)
    output_file = os.path.join(output_folder, base_name.replace('.s2p', '.csv'))

    # 保存为CSV文件
    df.to_csv(output_file, index=False)

    # 打印结果
    print(f"转换成功：{s2p_file} -> {output_file}")
