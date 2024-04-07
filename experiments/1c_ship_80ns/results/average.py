import pandas as pd

# 请求用户输入Excel文件的路径
file_path = './statistics.xlsx'

# 使用pandas读取Excel文件
df = pd.read_excel(file_path)

# 定义要计算平均值的列名
columns_to_calculate = [
    'Core_0_IPC', 
    'Core_0_LLC_total_access', 
    'Core_0_LLC_total_hit', 
    'Core_0_LLC_average_miss_latency'
]

# 检查所需列是否存在于DataFrame中
missing_columns = [col for col in columns_to_calculate if col not in df.columns]
if missing_columns:
    print(f"错误：找不到列 {', '.join(missing_columns)}")
else:
    # 对每个指定的列计算平均值，并打印结果
    for col in columns_to_calculate:
        average = df[col].mean()
        print(f"{col} 列的平均值为：{average}")
