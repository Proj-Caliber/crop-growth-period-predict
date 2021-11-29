import os
from config.caliber_dataset import genus_df

base_dir = os.getcwd() + '/data'
train_dir = os.path.join(base_dir, 'open/train_dataset')
test_dir = os.path.join(base_dir, 'open/test_dataset')

trial = genus_df(root_path = test_dir, keyword = "LT")
print(trial.annot_df())
df = trial.annot_df()
print(df['time_delta'].apply(lambda x: int(x[-5:])).min())
print(df['time_delta'].apply(lambda x: int(x[-5:])).max())

# test BC -> min 10, max 993
# test LT -> min 1, max 989
print(993/24)
print(989/24)
# gdrive url : https://drive.google.com/file/d/1I-u-NKUyd8M-NFm0DJnERVhQ0B8wu76p/view?usp=sharing?export=download
# 