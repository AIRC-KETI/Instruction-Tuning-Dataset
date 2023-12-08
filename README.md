# 한국어 지시학습 데이터셋

거대 언어 모델의 제로 샷(Zero shot) 성능을 향상시키는 방법으로 제시된 Instruction Tuning 데이터셋을 한국어로 번역한 데이터셋입니다.
[LongKE-T5](https://github.com/AIRC-KETI/long-ke-t5) 모델을 이용해 영어 데이터셋과 템플릿을 한국어로 번역했습니다.
한국어 데이터셋과 템플릿, 그리고 템플릿화하는 예제 코드를 제공합니다.
자세한 내용은 아래 Citation에 제공된 논문을 참고하시길 바랍니다.


## 한국어 데이터셋
아래 데이터셋들은 [KETI-AIR 허깅페이스](https://huggingface.co/KETI-AIR)에서 다운로드 할 수 있습니다.

  | Dataset  | HF name |
  | --------------------- | --------------------- |
  | aeslc | **KETI-AIR/kor_aeslc** |
  | ag_news | **KETI-AIR/kor_ag_news** |
  | ai2_arc | **KETI-AIR/kor_ai2_arc** |
  | amazon_polarity | **KETI-AIR/kor_amazon_polarity** |
  | anli | **KETI-AIR/kor_anli** |
  | boolq | **KETI-AIR/kor_boolq** |
  | commonsense_qa | **KETI-AIR/kor_commonsense_qa** |
  | cosmos_qa | **KETI-AIR/kor_cosmos_qa** |
  | dbpedia_14 | **KETI-AIR/kor_dbpedia_14** |
  | duorc | **KETI-AIR/kor_duorc** |
  | glue | **KETI-AIR/kor_glue** |
  | hellaswag | **KETI-AIR/kor_hellaswag** |
  | nq_open | **KETI-AIR/kor_nq_open** |
  | piqa | **KETI-AIR/kor_piqa** |
  | qasc | **KETI-AIR/kor_qasc** |
  | quail | **KETI-AIR/kor_quail** |
  | quarel | **KETI-AIR/kor_quarel** |
  | quartz | **KETI-AIR/kor_quartz** |
  | race | **KETI-AIR/kor_race** |
  | ropes | **KETI-AIR/kor_ropes** |
  | snli | **KETI-AIR/kor_snli** |
  | squad_v2 | **KETI-AIR/kor_squad_v2** |
  | web_questions | **KETI-AIR/kor_web_questions** |
  | wiki_hop | **KETI-AIR/kor_wiki_hop** |


## 한국어 데이터를 원본(영어데이터)과 비교하고싶은 경우
```python
    import json
    import datasets

    ko_ dataset = json.load(open("DATASET_DIRECTORY/KITD_dataset.json", mode="r"))
    ko_data = ko_dataset[0]

    # 각 데이터 객체마다 data_name, data_split_name, data_index_by_user가 존재하므로 이를 이용

    data_name = ko_data['data_name'] 
    data_split_name = ko_data['data_split_name'] 
    data_index_by_user = ko_data['data_index_by_user']

    en_dataset = datasets.load_dataset(data_name, data_split_name, cache_dir = './EN_DATASET') # 캐쉬파일이 저장될 디렉토리 지정
    en_data = en_dataset[data_index_by_user]

    print(f"\n[ 한국어 데이터 ]\n{ko_data}\n\n")
    print(f"\n[ 영어 데이터]\n{en_data}\n")
```

## 파이썬 템플릿으로 프롬프트 만들기

파이썬 템플릿 이용을 위한 환경설정
```bash
    conda activate your_environment
    pip install datasets tqdm
```
한국어 지시학습 데이터셋 제작
```bash
    python make_sample.py
```
데이터셋 마다 task와 데이터 구성이 다르기 때문에, 아래와 같은 데이터셋 구성 코드를 참조하여 직접 구현  
( 우선 데이터에 해당하는 템플릿이 존재 하는지 확인 -> 데이터셋 구성요소(dataset.features) 이용하여 구조 확인)
```python
    # make_sample.py
    import json
    import datasets

    from tqdm import tqdm

    from KITD_TEMPLATE import KITD_TEMPLATES
    
    TOTAL = list() # DataLoader에 적재하기위한 Total Dataset
    
    # ag_news
    
    dataset = datasets.load_dataset('KETI-AIR/kor_ag_news', cache_dir = './KO_DATASET')       # hugging face로부터 데이터셋 다운, 캐쉬파일이 저장될 디렉토리를 KO_DATASET으로 지정
    _TEMP_TEMPLATE = KITD_TEMPLATES['ag_news']        # 템플릿 선택, 데이터 원본 이름으로 찾기 가능하며 데이터마다 템플릿 확인
    _ag_news_label_list_ko = ['세계', '스포츠', '사업', '과학기술']       # data['label']이 ClassLabel로 구성되어 있음 => 이 구조를 그대로 활용하기 위해 list 사용 
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols=120):
            # if _idx > 100: break        # sample 제작을 원할경우, 주석해제
            temp = dict()         # 데이터 무결성을 보장하기 위해 딕셔너리로 데이터 객체 생성

            _input = _TEMP_TEMPLATE[0][0].format(text = data['text'], options_ = _ag_news_label_list_ko)        # 데이터셋 템플릿에 맞게 inputdata 입력, 이때 ClassLabel을 선택지로 주고자 options_s에 list 대입
            _output = _TEMP_TEMPLATE[0][1].format(label = _ag_news_label_list_ko[data['label']])        # 마찬가지로 outputdata 입력.
            # _TEMP_TEMPLATE[0] == ["\n\n{text}\n\n이거 주제는 뭐야?{options_}", "{label}"]
            # Data Example
            # _input == "\n\n월스트 베어스 클로우 백 인 더 블랙 (로이터) 로이터=연합뉴스) 월스트리트의 초중고 유통업체 공매도자들이 다시 녹색을 보이고 있다.\n\n이거 주제는 뭐야? ['세계', '스포츠', '사업', '과학기술']"
            # _output == "사업"
            
            # 각 데이터 객체 구성 5가지
            # input & output data
            # 이 때 원본데이터를 쉽게 찾도록 data_name, data_split_name, data_index_by_user를 추가
            # data_index_by_user 키 값을 이용해 번역된 데이터와 원본 데이터 비교 가능

            temp['input'] = _input        
            temp['output'] = _output
            temp['data_name'] = 'ag_news'
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            total.append(temp)
    TOTAL.extend(total)
    ```
    데이터셋 2
    ```
    데이터셋 3
    ```
    json.dump(
        TOTAL,
        open("DATASET_DIRECTORY/KITD_dataset.json", mode="w"),
        ensure_ascii=False,
        indent=4,
    )
```
데이터셋 snli는  multi-input-text-classification task  
하지만 템플릿을 다음과 같이 수정하면 데이터의 task를 수정할 수 있음. (multi-input-text-classification -> text-generation)  
자신만의 템플릿을 추가하여 데이터 구성 가능  
또는 다른 task의 템플릿을 이용하여 적절히 사용 가능
```python
    # snli
    
    dataset = datasets.load_dataset('KETI-AIR/kor_snli', cache_dir = './KO_DATASET')       # hugging face로부터 데이터셋 다운, 캐쉬파일이 저장될 디렉토리를 KO_DATASET으로 지정
    _TEMP_TEMPLATE = KITD_TEMPLATES['snli']
    _snli_label_list_ko = ['가능하다', '애매하다', '없다']       # data['label']이 ClassLabel로 구성되어 있음 => 이 구조를 그대로 활용하기 위해 list 사용 
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols=120):
            # if _idx > 100: break        # sample 제작을 원할경우, 주석해제
            temp = dict()         # 데이터 무결성을 보장하기 위해 딕셔너리로 데이터 객체 생성
            _NEW_TEMPLATE = [
              "\"전제 : {premise} 가설 : (정답) \n 위 전제가 참이면 가설도 참이라고 할 수 있어? {label}\"\n 위 문장에서 (정답)에 들어갈 수 있는 문장을 써줘",
              "{hypothesis}라고 할 수 있습니다."
            ]
            _input = _NEW_TEMPLATE[0].format(premise = data['premise'], label = _snli_label_list_ko[data['label']])        # 데이터셋 템플릿에 맞게 inputdata 입력
            _output = _NEW_TEMPLATE[1].format(hypothesis = data['hypothesis'])        # 마찬가지로 outputdata 입력.
            
            # 각 데이터 객체 구성 5가지
            # input&output data
            # 이 때 원본데이터를 쉽게 찾도록 data_name, data_split_name, id를 추가
            # data_index_by_user 값을 이용해 번역된 데이터와 원본 데이터 비교 가능

            temp['input'] = _input        
            temp['output'] = _output
            temp['data_name'] = 'ag_news'
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            total.append(temp)
    TOTAL.extend(total)
```


## Jinja 템플릿으로 프롬프트 만들기

자세한 내용은 [promptsource](https://github.com/bigscience-workshop/promptsource) 깃허브를 참고하세요.

### 환경 만들기
깃허브에서 한글 template clone 해오기
```bash
git clone https://github.com/AIRC-KETI/Instruction-Tuning-Dataset.git
```

promptsource 설치
```bash
cd ./promptsource
pip install -e .
```

### 템플릿으로 원본 데이터와 같은 task의 데이터셋 만들기

#### 데이터셋 예시(ag_news, classification)
```python
{
    "text": "유가가 사상 최고치를 경신하며 미국 경제에 새로운 위협이 되고 있다.",
    "label": 2
}
```

#### 템플릿 예시(ag_news 템플릿, classification task)
```jinja2
이 뉴스 기사를 가장 잘 설명하는 분류는 무엇입니까?

{{ text }}
|||
{{ answer_choices[label] }}
```

#### 프롬프트 만들기
```python
# 한국어로 번역한 데이터셋 불러오기
from datasets import load_dataset
dataset = load_dataset("KETI-AIR/kor_ag_news", split="train")
example = dataset[4]

# 한국어로 번역한 템플릿 불러오기
from promptsource.templates import DatasetTemplates
ag_news_template = DatasetTemplates("ag_news")

# 예시 템플릿 하나 선정
prompt = ag_news_template["classify_question_first"]

# 데이터에 프롬프트 적용
result = prompt.apply(example)
print("input: ", result[0])
print()
print("output: ", result[1])
```
```text
input:  이 뉴스 기사를 가장 잘 설명하는 분류는 무엇입니까?
유가가 사상 최고치를 경신하며 미국 경제에 새로운 위협이 되고 있다.

output:  비즈니스
```

### 템플릿으로 원본 데이터와 다른 task의 데이터셋 만들기

#### 데이터셋 예시(squad_v2, QA)
```python
{
    "id": "56be85543aeaaa14008c9063",
    "title": "비욘세.",
    "context": "비욘세 지젤 노울스-카터(/bijnse/bee-YON-say)(1981년 9월 4일생)는 미국의 싱어, 작곡가, 음반 제작자, 여배우이다.텍사스 휴스턴에서 태어나 자란 그녀는 어렸을 때 다양한 노래와 춤 경연대회에서 공연했으며 1990년대 후반 R&B 걸그룹 'Destiny's Child'의 리드싱어로 명성을 날렸다.(생략)",
    "question": "비욘세는 언제부터 인기를 끌기 시작했나요?",
    "answers": {
        "text": [
            "1990년대 후반"
        ],
        "answer_start": [
            269
        ]
    },
    "data_index_by_user": 0
}
```

#### 템플릿 예시(squad_v2 템플릿, generation task)
```jinja2
이 글이 뭐에 관한 거야?

{{ context }} |||

{{ title | replace("_", " ") }}
```

#### 프롬프트 만들기
```python
# 한국어로 번역한 데이터셋 불러오기
from datasets import load_dataset
dataset = load_dataset("KETI-AIR/kor_squad_v2", split="train")
example = dataset[0]

# 한국어로 번역한 템플릿 불러오기
from promptsource.templates import DatasetTemplates
samsum_template = DatasetTemplates("squad_v2")

# 예시 템플릿 하나 선정
prompt = samsum_template["Topic Prediction - Context"]

# 데이터에 프롬프트 적용
result = prompt.apply(example)
print("input: ", result[0])
print()
print("output: ", result[1])
```
```text
input:  이 글이 뭐에 관한 거야?
비욘세 지젤 노울스-카터(/bijnse/bee-YON-say)(1981년 9월 4일생)는 미국의 싱어, 작곡가, 음반 제작자, 여배우이다.텍사스 휴스턴에서 태어나 자란 그녀는 어렸을 때 다양한 노래와 춤 경연대회에서 공연했으며 1990년대 후반 R&B 걸그룹 'Destiny's Child'의 리드싱어로 명성을 날렸다.(생략)

output: 비욘세.
```

## Citation Information

```
@inproceedings{KITD,
  title={언어 번역 모델을 통한 한국어 지시 학습 데이터 세트 구축},
  author={임영서, 추현창, 김산, 장진예, 정민영, 신사임},
  booktitle={제 35회 한글 및 한국어 정보처리 학술대회},
  pages={591--595},
  year={2023}
}
@inproceedings{KITD,
  title={Korean Instruction Tuning Dataset},
  author={Yeongseo Lim, HyeonChang Chu, San Kim, Jin Yea Jang, Minyoung Jung, Saim Shin},
  booktitle={Proceedings of the 35th Annual Conference on Human and Cognitive Language Technology},
  pages={591--595},
  year={2023}
}
```