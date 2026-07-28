# 把 fetch_data.py 里的 INDICES 替换为这段即可：
INDICES = {
    "EARNINGS_YIELD": [
        {"name": "上证50", "code": "000016", "type": "sh"},
        {"name": "上证红利", "code": "000015", "type": "sh"},
        {"name": "中证红利", "code": "000922", "type": "sh"},
        {"name": "恒生指数", "code": "HSI", "type": "hk"},
        {"name": "恒生国企", "code": "HSCEI", "type": "hk"}
    ],
    "BOGLE_PE": [
        {"name": "沪深300", "code": "000300", "type": "sh"},
        {"name": "中证500", "code": "399905", "type": "sz"},
        {"name": "创业板指", "code": "399006", "type": "sz"},
        {"name": "科创50", "code": "000688", "type": "sh"},
        {"name": "主要消费", "code": "000036", "type": "sh"},
        {"name": "医药100", "code": "000109", "type": "sh"}
    ],
    "BOGLE_PB": [
        {"name": "证券公司", "code": "399975", "type": "sz"},
        {"name": "中证银行", "code": "399986", "type": "sz"},
        {"name": "地产等权", "code": "399983", "type": "sz"},
        {"name": "中证煤炭", "code": "399998", "type": "sz"}
    ]
}
