(2) 添加 RecAgent 算法
1.注册 RecAgent 算法： 在 ReChorus 的 model_config.py 中，添加 RecAgent 的引用：from models.recagent import RecAgent
MODEL_REGISTRY["RecAgent"] = RecAgent
2．实现 RecAgent： 在 recagent.py 中实现 RecAgent 的主要逻辑

(3) 配置对比实验
1.	选择对比算法：
o	在框架中选择同类别算法，如：
	Transformer-based 模型：SASRec, BERT4Rec。
	协同过滤模型：ItemCF, UserCF。
2.	修改配置文件： 配置 config.yaml，指定实验参数，如算法名称、数据集路径和评估指标：
3.	运行实验： 使用 ReChorus 提供的运行脚本启动实验：
python run_experiment.py --config config.yaml

（4）结果对比与分析
1.	收集实验结果：
o	ReChorus 会自动生成实验结果文件（通常在 results/ 文件夹下）。
o	提取各算法在不同指标（如 Precision@10、Recall@20）上的表现。
2.	分析与可视化： 使用 Matplotlib 或 Seaborn 绘制对比图：
 

