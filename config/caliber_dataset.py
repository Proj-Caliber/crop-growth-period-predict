import os
import re
from glob import glob
import pandas as pd

class genus_df:
    def __init__(self, root_path=None, keyword=None):
        self.root_path = root_path
        self.genus = keyword if keyword!=None else input(f'작물의 디렉토리명을 입력하세요. 예) BC')
        if self.root_path:
            self.directories = glob(self.root_path + f'/{self.genus}/*')
            print(self.directories)
        else:
            try:
                self.directories = glob(f'./{self.genus}/*')
                assert self.directories
            except:
                print("경로 설정을 다시 확인하세요.")
            
    def path_by_genus(self):
        image_path = []
        for path in self.directories:
            feats_path = glob(path + '/*.png')
            image_path.extend(feats_path)
        return image_path
    
    def annot_df(self):
        image_path = self.path_by_genus()
        df = pd.DataFrame({'genus':[self.genus for g in range(len(image_path))], 
                           'filename':image_path})
        df['time_delta'] = [os.path.basename(fname) for fname in image_path]
        df['time_delta'] = df['time_delta'].apply(lambda x: re.sub('[^0-9]', '', x))
        print(df['time_delta'].unique())
        return df