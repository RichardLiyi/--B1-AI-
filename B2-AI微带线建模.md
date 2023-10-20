# B2-AI微带线建模-李义

### 问题介绍：

- 输入W、L、H、Er四个参数，自动输出一个s2p文件，包含20行，一行对应一个频段。

- 一个频段要求给出四个参数，S11，S12，S21，S22。但由于对角元素相同，实际只要得到S11，S21即足够
- ![image-20231019160121780](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019160121780.png)

### s2p文件的介绍：

![image-20231019155538894](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155538894.png)

![image-20231019155557707](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155557707.png)

### **用txt方式打开s2p文件，可知：**

![image-20231019155638675](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155638675.png)

### 含义介绍：



**![image-20231019155749750](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155749750.png)**

注意实数和虚数的命名：

- 例如，S11部分，第一列是实数，为S11_realPart，第二列为S11_imagePart

![image-20231019155734397](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155734397.png)

### 基础知识：

#### 区分单频点和多频点数据

假设有一个射频电路，您需要对其进行S参数测量，并得到以下数据：

- 单频点：在频率f=1 GHz上测量的S参数为：

  ```
  [[0.3 + 0.4j, 0.2 - 0.1j],
   [0.2 - 0.1j, 0.3 + 0.2j]]
  ```

  这是一个2x2的矩阵，表示该射频电路在频率为1 GHz时输入和输出端口之间的传输函数。

- 多频点：在频率范围[1 GHz, 2 GHz]内均匀采样n个频率点的S参数数据。例如，当n=3时，您得到以下S参数数据：

  ```
  [
    [[0.3 + 0.4j, 0.2 - 0.1j],  # 在f=1 GHz处的S参数矩阵
     [0.2 - 0.1j, 0.3 + 0.2j]],
  
    [[0.2 + 0.3j, 0.1 - 0.2j],  # 在f=1.5 GHz处的S参数矩阵
     [0.1 - 0.2j, 0.4 + 0.3j]],
  
    [[0.1 + 0.2j, 0.3 - 0.1j],  # 在f=2 GHz处的S参数矩阵
     [0.3 - 0.1j, 0.2 + 0.1j]]
  ]
  ```

  这是一个3维数组，其中每个元素都是一个2x2的矩阵，分别对应于不同频率下的S参数。例如，第一个元素表示在1 GHz下的S参数矩阵，第二个元素表示在1.5 GHz下的S参数矩阵，以此类推。

当您处理单频点S参数时，可以直接使用矩阵操作来分析电路的特性，例如计算反射损耗或传输损耗等。而在处理多频点S参数时，则需要针对每个频率点分别进行分析，例如绘制频率响应曲线、计算带宽等。毕竟多频点S参数提供了更丰富的频率信息，可以更好地描述电路的行为。

#### 幅值和相位：

在信号处理和电路领域中，幅值（Amplitude）和相位（Phase）是描述信号或波形特征的两个重要参数。

1. 幅值（Amplitude）：幅值表示信号的振幅或大小，用于衡量信号的强度或能量。在复数表示中，幅值指的是一个复数的模，即复数在复平面上与原点之间的距离。幅值可以是实数也可以是非负实数，通常用于表示正弦波、震荡信号等的振幅。例如，对于复数z = a + bi，其中a为实部，b为虚部，它的幅值可以表示为|z|或sqrt(a^2 + b^2)。

   举例来说，对于复数4 + 3i，它的幅值可以计算如下：

   |4 + 3i| = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5

   因此，复数4 + 3i的幅值为5。

2. 相位（Phase）：相位表示信号相对于某个基准的偏移量或旋转角度。相位描述了信号的周期性或周期位置。在复数表示中，相位可以由复数的辐角表示，即复数所在向量与实轴之间的夹角。相位通常以弧度或角度表示。例如，对于复数z = a + bi，其中a为实部，b为虚部，它的相位可以表示为theta = atan2(b/a)，其中atan2是一个常用的求反正切函数。

   举例来说，对于复数4 + 3i，它的相位可以计算如下：

   theta = atan2(3/4) ≈ 0.6435 弧度

   因此，复数4 + 3i的相位约为0.6435弧度。

总结起来，幅值描述信号的振幅大小，相位描述信号的偏移或旋转角度。在信号处理和电路中，幅值和相位是描述信号特性的重要参数，用于分析和处理各种信号、波形和频谱等。

### Python读取s2p文件并进行打印输出：

```
import skrf

# 读取S2P文件
# 此处替换为绝对路径
filename = 'D:\\桌面\\先进计算大赛\\专题赛数据\\s2p\\1.s2p'
network = skrf.Network(filename)

# 获取S参数的数据
s_params = network.s

print(s_params)
```

**多频点数据输出展示：**

![image-20231019155437655](C:\Users\Mr.Richard\AppData\Roaming\Typora\typora-user-images\image-20231019155437655.png)

### 读取单个s2p文件并转化为csv文件：

```
import numpy as np
import pandas as pd
import skrf

# 读取S2P文件
# 此处替换为绝对路径
filename = 'D:\\桌面\\先进计算大赛\\B1-AI微带线建模\\专题赛数据\s2p\\1.s2p'
network = skrf.Network(filename)

# 获取S参数的数据
s_params = network.s
# 记录频率点
freqs = network.f

# 定义csv文件中每一列的名字

columns = ["freq (GHz)", "S11_real", "S11_image", "S21_real", "S21_image", "S12_real", "S12_image", "S22_real", "S22_image"]
# 将频率点，S11的实部，虚部，S21的实部，虚部.....拼接在一起
data = np.column_stack((freqs, s_params[:, 0, 0].real, s_params[:, 0, 0].imag,
                        s_params[:, 1, 0].real, s_params[:, 1, 0].imag,
                        s_params[:, 0, 1].real, s_params[:, 0, 1].imag,
                        s_params[:, 1, 1].real, s_params[:, 1, 1].imag))
print(data)
df = pd.DataFrame(data=data, columns=columns)

```

### 批量读取s2p文件并进行转写：

```
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

```

