# 来源：【10行代码战胜90%数据科学家？-哔哩哔哩】https://b23.tv/86CdgP
# 创建并激活 Python 3.8 的环境
conda create -y --force -n ag python=3.8 pip
conda activate ag

# 安装 autogluon
pip install "mxnet<2.0.0"  # 基于mxnet的后端
pip install autogluon