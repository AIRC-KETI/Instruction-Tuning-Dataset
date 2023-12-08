KITD_TEMPLATES_SAMPLE = {
    "ag_news": [
        ["\n\n{text}\n\n이거 주제는 뭐야?{options_}", "{label}"],
        ["\n\n{text}\n\n주제가?{options_}", "{label}"],
        ["{text}\n요약해.\n{options_}", "{label}"],
        ["{text}\n그래서 뭐에 관한 거야?\n{options_}", "{label}"],
    ],
    "amazon_polarity": [
        [
            "제목 : {title}\n\n 내용 : {content}\n 이 글의 내용은 어떤 것 같아? ( 보기 : {options_} )\n",
            "{label}",
        ]
    ],
    "anli": [
        [
            '{premise}\n\n위 글에서 아래문장이 맞다고 할 수 있어?\n"{hypothesis}"\n\n{options_}',
            "{label}",
        ],
        ["{premise}\n\n글을 읽어봤을 때 아래 문장이 참이야?\n{hypothesis}\n\n{options_}", "{label}"],
        ["{premise}\n\n결론을 아래 문장처럼 지을 수 있나?\n{hypothesis}\n\n{options_}", "{label}"],
        [
            "{premise}\n\n위 글을 읽었을 때 다음 문장으로 뒤 따라오는 게 맞지않아?\n{hypothesis}\n\n{options_}",
            "{label}",
        ]
    ],
    "cosmos_qa": [
        ["{context}\n\n질문: {question}\n{options_}", "{label}"],
        ["{context}\n\n{question}\n{options_}", "{label}"],
        ["{context}\n\n다음 질문에 답하라: {question}\n{options_}", "{label}"],
        ["{context}\n\n앞의 지문을 바탕으로 다음과 같은 질문에 답하라. {question}\n{options_}", "{label}"],
    ],
    "duorc": [
        [
            "제목 : {title}\n\n {plot}\n\n 다음 질문에 답해줘\n{question}\n",
            '"{answers}" 라고 답할 수 있어.',
        ],
        ["{question}\n[ {title} ]\n\n{plot}", "{answers}"],
        [
            '{plot}\n"{title}"라는 제목의 위 내용을 바탕으로 {question}에 대한 답변을 작성해줘',
            "답변 : {answers}",
        ],
        ['아래 글을 읽고,\n"{question}" 라는 질문에 대답하시오.\n{title}\n {plot}', "정답 : {answers}"],
    ],
    "qasc": [
        [
            "다음 질문에 답해, {formatted_question}\n [참조]\n{fact1},\n{fact2}",
            "({answerKey}) {text}",
        ]
    ],
    "quarel": [
        ["다음 질문 형식에서 알맞은 답을 골라줘, 알파벳까지 포함해서.\n{question}", "({answer_index}) {world}"]
    ],
    "quartz": [
        [
            "[질문]\n{question}\n추가정보:{para}\n\n(A) {choices_A}\n(B) {choices_B}\n",
            "({answerKey}) {text}",
        ]
    ],
    "race": [
        ["[전제] : {article}, {question}은 무엇인가?\n\n{options_}", "{answer}"],
        ["여기서 전제가 되는 것은 {article}이다.\n\n{question}은 무엇인가?\n\n{options_}", "{answer}"],
        ['{article}\n\n위의 글을 읽고, "{question}"에 답하시오.\n\n{options_}', "{answer}"],
        ["{article}\n\n합리적인 {question}은 무엇인가?\n\n{options_}", "{answer}"],
    ],
    "ropes": [
        [
            "{background}\n위 글을 읽고 아래 상황에 대한 질문에 답해줘\n( 상황 : {situation} )\n{question}",
            "{answers}",
        ],
        [
            "질문 : {question}\n배경지식 : {background}\n상황 : {situation}\n\n위 질문에 대한 답은?",
            '답변은 "{answers}" 이다.',
        ],
    ],
    "snli": [
        ['만약 "{premise}"라면, 이것은 "{hypothesis}"을 의미하는가?\n\n{options_}', "{label}"],
        ['만약 "{premise}"라면, 우리는 "{hypothesis}"을 결론지을 수 있을까?\n\n{options_}', "{label}"],
        ['만약 "{premise}"라면 그 "{hypothesis}"을 논리적으로 따를 것인가?\n\n{options_}', "{label}"],
        [
            '"{premise}"라는 문장에 근거하여, "{hypothesis}"이라는 문장은 참 문장인가?\n\n{options_}',
            "{label}",
        ]
    ],
    "squad_v2": [
        [
            '\n\n{context}\n\n이 글에 대해 궁금한게 있어. 앖이 없으면, "답이 없어"라고 말해줘. {question}',
            "{answers}",
        ],
        [
            '이것을 읽고 질문에 답해줘. 질문에 답할 수 없으면 "답할 수 없다"고 알려줘.\n\n{context}\n\n{question}',
            "{answers}",
        ],
        [
            '이 글에 대한 질문은 뭐야? 질문에 답할 수 없으면 "답할 수 없다"고 말해줘.\n\n{context}\n\n{question}',
            "{answers}",
        ],
        ['{context}\n{question}\n(질문이 대답할 수 없는 질문이면 "답할 수 없음"이라고 말해.)', "{answers}"],
        [
            '{context}\n할 수 있으면, 이 질문에 답해봐 (그렇지 않으면 "답할 수 없음"으로 말해): {question}',
            "{answers}",
        ]
    ],
    "web_questions": [
        ['url : {url}\n위 사이트 내용을 바탕으로 다음 질문에 대답해줘 : "{question}"\n', "{answers}"]
    ],
    "wiki_hop": [
        [
            "다음 문장에 대답해줘 : {question}\n ( 보기 : {candidates})\n단, 아래 문장 집합들을 참고해서 대답해줘\n{supports}",
            "{answer}",
        ]
    ],    
}
