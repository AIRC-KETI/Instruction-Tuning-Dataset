import json
import datasets

from tqdm import tqdm

from KITD_TEMPLATE import KITD_TEMPLATES

def _sample_KITD():
    TOTAL = list()

    # ropes -> test에 답 존재 X, 구축 X
    dataset = datasets.load_dataset('KETI-AIR/kor_ropes', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['ropes']
    total = list()
    for split in dataset.keys():
        if split == 'test':continue
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(background = data['background'], situation = data['situation'], question = data['question'])
            _output = _TEMP_TEMPLATE[0][1].format(answers = data['answers']['text'][0])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'ropes'
            total.append(temp)
    TOTAL.extend(total)

    # web_questions
    dataset = datasets.load_dataset('KETI-AIR/kor_web_questions', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['web_questions']
    total = list()
    for split in dataset.keys():
        if split == 'test':continue
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(url = data['url'], question = data['question'])
            _output = _TEMP_TEMPLATE[0][1].format(answers = data['answers'][0])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'web_questions'
            total.append(temp)
    TOTAL.extend(total)

    # quarel
    dataset = datasets.load_dataset('KETI-AIR/kor_quarel', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['quarel']
    total = list()
    for split in dataset.keys():
        if split == 'test':continue
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(question = data['question'])
            if data['answer_index'] == 0:
                _output = _TEMP_TEMPLATE[0][1].format(answer_index = chr(data['answer_index'] + 65), world = data['world_literals']['world1'][0])
            elif data['answer_index'] == 1:
                _output = _TEMP_TEMPLATE[0][1].format(answer_index = chr(data['answer_index'] + 65), world = data['world_literals']['world2'][0])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'quarel'
            total.append(temp)
    TOTAL.extend(total)

    # qasc => test에 데이터 존재 X -> 제외하고 구축
    dataset = datasets.load_dataset('KETI-AIR/kor_qasc', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['qasc']
    total = list()
    for split in dataset.keys():
        if split == 'test':continue
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(formatted_question = data['formatted_question'], fact1 = data['fact1'], fact2 = data['fact2'])
            _output = _TEMP_TEMPLATE[0][1].format(answerKey = data['answerKey'], text = data['choices']['text'][ord(data['answerKey'][0])-65])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'qasc'
            total.append(temp)
    TOTAL.extend(total)

    # wiki_hop
    dataset = datasets.load_dataset('KETI-AIR/kor_wiki_hop', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['wiki_hop']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(question = data['question'], candidates = data['candidates'], supports = data['supports'])
            _output = _TEMP_TEMPLATE[0][1].format(answer = data['answer'])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'wiki_hop'
            total.append(temp)
    TOTAL.extend(total)

    # quartz
    dataset = datasets.load_dataset('KETI-AIR/kor_quartz', cache_dir= './EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['quartz']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(question = data['question'], para = data['para'], choices_A = data['choices']['text'][0],
                                                 choices_B = data['choices']['text'][1])
            _output = _TEMP_TEMPLATE[0][1].format(answerKey = data['answerKey'], text = data['choices']['text'][ord(data['answerKey']) - 65])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'quartz'
            total.append(temp)
    TOTAL.extend(total)

    # amazon_polarity
    dataset = datasets.load_dataset('KETI-AIR/kor_amazon_polarity', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['amazon_polarity']
    _options = ['부정적이야', '긍정적이야']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(title = data['title'], content = data['content'], options_ = _options)
            _output = _TEMP_TEMPLATE[0][1].format(label = _options[data['label']])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'amazon_polarity'
            total.append(temp)
    TOTAL.extend(total)


    # duorc
    dataset = datasets.load_dataset('KETI-AIR/kor_duorc', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['duorc']
    _duorc_no_answer = '답할 수 없어'
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(title = data['title'], plot = data['plot'], question = data['question'])
            if data['no_answer'] or len(data['answers'])== 0:
                _output = _duorc_no_answer
            else:
                _output = _TEMP_TEMPLATE[0][1].format(answers = data['answers'][0])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data["data_index_by_user"]

            temp['data_name'] = 'duorc'
            total.append(temp)
    TOTAL.extend(total)

    # snli
    dataset = datasets.load_dataset('KETI-AIR/kor_snli', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['snli']
    _snli_answer_list = ['가능하다', '애매하다', '없다']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[4][0].format(premise = data['premise'], hypothesis = data['hypothesis'], options_ = _snli_answer_list)
            _output = _TEMP_TEMPLATE[4][1].format(label = _snli_answer_list[data['label']])

            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'snli'
            total.append(temp)
    TOTAL.extend(total)

    # cosmos_qa
    dataset = datasets.load_dataset('KETI-AIR/kor_cosmos_qa', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['cosmos_qa']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()
            
            _answer_list = [data['answer0'],  data['answer1'],  data['answer2'],  data['answer3']]
            
            _options = ""
            for _answer in _answer_list:
                _options += _answer
                _options += '\n'

            _input = _TEMP_TEMPLATE[3][0].format(context = data['context'], question = data['question'], options_ = _options)
            _output = _TEMP_TEMPLATE[3][1].format(label = _answer_list[data['label']])
            
            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'cosmos_qa'
            total.append(temp)
    TOTAL.extend(total)



    # race
    dataset = datasets.load_dataset('KETI-AIR/kor_race', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['race']
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[3][0].format(article = data['article'], question = data['question'], options_ = data['options'])
            _output = _TEMP_TEMPLATE[3][1].format(answer = data['options'][ord(data['answer']) - 65])
            
            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'race'
            total.append(temp)
    TOTAL.extend(total)



    # squad_v2
    dataset = datasets.load_dataset('KETI-AIR/kor_squad_v2', cache_dir='./EN_DATASET')
    _TEMP_TEMPLATE = KITD_TEMPLATES['squad_v2']
    _squad_v2_no_answer = '답이 없어' # only template[0], no answer
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols = 120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(context = data['context'], question = data['question'])
            if len(data['answers']['text']) == 0:
                _output = _squad_v2_no_answer
            else:
                _output = _TEMP_TEMPLATE[0][1].format(answers = data['answers']['text'][0])
            
            temp['input'] = _input
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'squad_v2'
            total.append(temp)

    TOTAL.extend(total)

    # ag_news
    
    dataset = datasets.load_dataset('KETI-AIR/kor_ag_news')       # hugging face로부터 데이터셋 다운
    _TEMP_TEMPLATE = KITD_TEMPLATES['ag_news']        # 템플릿 선택, 데이터 원본 이름으로 찾기 가능하며 데이터마다 템플릿 확인
    _ag_news_label_list_ko = ['세계', '스포츠', '사업', '과학기술']       # data['label']이 ClassLabel로 구성되어 있음 => 이 구조를 그대로 활용하기 위해 list 사용 
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total = len(dataset[split]), ncols=120):
            # if _idx > 100: break        # sample 제작을 원할경우, 주석해제
            temp = dict()         # 데이터 무결성을 보장하기 위해 딕셔너리로 데이터 객체 생성

            _input = _TEMP_TEMPLATE[0][0].format(text = data['text'], options_ = _ag_news_label_list_ko)        # 데이터셋 템플릿에 맞게 inputdata 입력, 이때 ClassLabel을 선택지로 주고자 options_s에 list 대입
            _output = _TEMP_TEMPLATE[0][1].format(label = _ag_news_label_list_ko[data['label']])        # 마찬가지로 outputdata 입력.
            
            # 각 데이터 객체 구성 5가지
            # input&output data
            # 이 때 원본데이터를 쉽게 찾도록 data_name, data_split_name, data_index를 추가
            # data_index_by_user 값이 없을경우 데이타 마다 고유의 id 이용
            temp['input'] = _input        
            temp['output'] = _output
            temp['data_split_name'] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'ag_news'
            total.append(temp)
    TOTAL.extend(total)


    # anli
    dataset = datasets.load_datasept("KITD.py", "anli", data_dir="KO_DATASET", cache_dir="./EN_DATASET")
    _TEMP_TEMPLATE = KITD_TEMPLATES["anli"]
    _anli_label_list_ko = ["맞다고 할 수 있어", "잘 모르겠어", "아니 틀려"]
    total = list()
    for split in dataset.keys():
        for _idx, data in tqdm(enumerate(dataset[split]), total=len(dataset[split]), ncols=120):
            # if _idx > 100: break
            temp = dict()

            _input = _TEMP_TEMPLATE[0][0].format(
                premise=data["premise"],
                hypothesis=data["hypothesis"],
                options_=data["reason"],
            )
            _output = _TEMP_TEMPLATE[0][1].format(
                label=_anli_label_list_ko[data["label"]]
            )

            temp["input"] = _input
            temp["output"] = _output
            temp["data_split_name"] = split
            temp['data_index_by_user'] = data['data_index_by_user']

            temp['data_name'] = 'anli'
            total.append(temp)
    TOTAL.extend(total)



    json.dump(
        TOTAL,
        open("DATASET_DIRECTORY/KITD_dataset.json", mode="w"),
        ensure_ascii=False,
        indent=4,
    )
