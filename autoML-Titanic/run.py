# autogluon会自动做特征提取，然后用多个分类器来训练数据，整个训练在cpu上花费几分钟
from autogluon.tabular import TabularDataset, TabularPredictor
# 训练
train_data = TabularDataset('train.csv')   # TabularDataset实际上就是pandas Dataframe的一个子类
id, label = 'PassengerId', 'Survived'
predictor = TabularPredictor(label=label).fit(
    train_data.drop(columns=[id]))

# 接下来生成数据，提交结果
import pandas as pd
#预测
test_data = TabularDataset('test.csv')
preds = predictor.predict(test_data.drop(columns=[id]))
submission = pd.DataFrame({id:test_data[id], label:preds})
submission.to_csv('submission.csv', index=False)