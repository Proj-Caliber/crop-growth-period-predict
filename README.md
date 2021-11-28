# crop-growth-period-predict

```
.
├── README.md
├── __test__
├── brainnodes.txt
├── config
├── data
│   ├── checkpoiont_128.pt
│   ├── open
│   │   ├── sample_submission.csv
│   │   ├── test_dataset
│   │   │   ├── BC
│   │   │   ├── LT
│   │   │   └── test_data.csv
│   │   └── train_dataset
│   │       ├── BC
│   │       └── LT
│   └── traininfos.json
├── docs
│   ├── Long-term\ Recurrernt\ Convolutional\ Networks\ for\ Visual\ Recognition\ and\ Description.pdf
│   └── Convolutional\ Neural\ Network\ with\ an\ Elastic\ Matching\ Mechanism\ for\ Time\ Series\ Classification.pdf
├── models
├── pyproject.toml
└── script
```

* models : 작물 특성별 예측 모델을 달리 사용할 계획

  * ./models/BC
  * ./models/LT
* config : 데이터 load ~ augmentation까지 기획 중
* docs : references


💡 주석 처리한 내용 참고

<!--
* config : 데이터 load ~ augmentation까지 기획 중, 대회 데이터의 경우엔 폴더별 저장되어있기 때문에 상관이 없지만, 스마트팜 지점 혹은 부서별로 작물의 코드가 자동 저장되는 시스템이 아니라면, 입력할 수 있도록 작성하는 것도 고려해야하나???(이건 서버인데? <-- 우선 대회 데이터까지만 처리하도록 하고 나머지는 향후 과제로 남겨놓거나, DB 연습할 때 사용하기)
	* ./config/caliber-dataset 
	* ./config/caliber-transformer

* data : Augmentation한 데이터도 대외비인지 확인한 뒤, ./data/aug | ./data/open/aug를 정해야 함.
	* ./data/open 대회 제공 데이터, 규정 상 공개 금지(대외비)
	* ./data/~.pt(checkpoint)

* script : 
	* ./script/gdrive 대회에서 제공한 파일이 연결된 구글 드라이브 링크로 이동해서, 다운받은 뒤, ./data에 저장할 수 있도록 하는 코드
	* ./script/predict models run한 뒤, 생장까지 걸리는 기간 예측 결과 반환
-->

## ./data/open

아래의 이미지 경로를 보면, 작물의 종(2)과 각 이미지 특성을 확인할 수 있다. 따라서, ./data/open/train_dataset/{AA}/{AA_99}는 각 종별로 대표적인 특성을 가진 생육 사진 폴더로 가정하고, ./data/open/test_dataset/{AA}/{9999}는 스마트팜 재배 기계의 일련번호로 가정한다.

### train_dataset

```
.
├── BC
│   ├── BC_01
│   ├── BC_02
│   ├── BC_03
│   ├── BC_04
│   ├── BC_05
│   ├── BC_06
│   ├── BC_07
│   ├── BC_08
│   └── BC_09
└── LT
    ├── LT_01
    ├── LT_02
    ├── LT_03
    ├── LT_04
    ├── LT_05
    ├── LT_06
    ├── LT_07
    ├── LT_08
    ├── LT_09
    └── LT_10
```

* image file format :

  ```
  ~/DAT{99}.png
  ```

### test_dataset

```
.
├── BC
│   ├── 1088
│   ├── 1100
│   └── 1112
└── LT
    ├── 1003
    ├── 1088
    └── 1089
```

* image file format :

  ```
  ~/idx_{AA}_{9999}_{00999}.png
  ```

### sample_submission

| idx  | time_delta |
| ---- | ---------- |
| 0    | -1         |
| ...  | ...        |
| 3959 | -1         |

* extension : .csv

## metrics : RMSE

$$
RMSE = \sqrt{\frac{1}{n}\Sigma_{i=1}^{n}{\Big(\frac{d_i -f_i}{\sigma_i}\Big)^2}}
$$

<!--
* 미정
import torch
from pytorch_lightning.utilities import metrics
import torchmetrics
class RMSE(torchmetrics.Metric):
    def __init__(self):
        self.add_state("sum_squared_errors", torch.tensor(0), dist_reduce_fx = "sum")
        self.add_state("n_observations", torch.tensor(0), dist_reduce_fx="sum")

    def update(self, preds, target):
        self.sum_squared_errors += torch.sum((preds - target) ** 2)
        self.n_observations += preds.numel()
        # torch.numel(input) -> int ; the total number of elements in the input tensor.

    def compute(self):
        return torch.sqrt(self.sum_squared_errors / self.n_observations)
-->

## papers

* [Long-term Recurrent Convolutional Networks for Visual Recognition and Description](https://arxiv.org/abs/1411.4389)`<!---->`
* [Convolutional Neural Network with an Elastic Matching Mechanism for Time Series Classification]([https://www.mdpi.com/1999-4893/14/7/192](https://www.mdpi.com/1999-4893/14/7/192))`<!---->`
