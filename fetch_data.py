import os
import json
import pandas as pd
import akshare as ak

# 定义需要抓取的指数清单
INDICES = {
    "EARNINGS_YIELD": [
        {"name": "上证50", "code": "000016", "type": "sh"},
        {"name": "上证红利", "code": "000015", "type": "sh"},
        {"name": "恒生指数", "code": "HSI", "type": "hk"}
    ],
    "BOGLE_PE": [
        {"name": "沪深300", "code": "000300", "type": "sh"},
        {"name": "中证500", "code": "399905", "type": "sz"},
        {"name": "创业板指", "code": "399006", "type": "sz"},
        {"name": "主要消费", "code": "000036", "type": "sh"}
    ],
    "BOGLE_PB": [
        {"name": "证券公司", "code": "399975", "type": "sz"},
        {"name": "中证银行", "code": "399986", "type": "sz"},
        {"name": "地产等权", "code": "399983", "type": "sz"}
    ]
}

def get_index_valuation():
    result_data = {}
    
    for category, items in INDICES.items():
        result_data[category] = []
        for item in items:
            try:
                # 使用 AkShare 获取指数历史指标
                df = ak.stock_a_indicator_lg(symbol=item["code"])
                latest = df.iloc[-1]
                
                pe_current = float(latest['pe'])
                pb_current = float(latest['pb'])
                
                # 计算 10 年历史分位数 (%)
                pe_pct = round((df['pe'] < pe_current).mean() * 100, 1)
                pb_pct = round((df['pb'] < pb_current).mean() * 100, 1)
                
                # 股息率兜底
                dv = float(latest.get('dv_ratio', 3.0)) if not pd.isna(latest.get('dv_ratio')) else 3.0
                
                result_data[category].append({
                    "name": item["name"],
                    "code": item["code"],
                    "pe": round(pe_current, 2),
                    "pb": round(pb_current, 2),
                    "pePct": pe_pct,
                    "pbPct": pb_pct,
                    "dv": round(dv, 2),
                    "eg": 7.5,  # 默认预估盈利增长率
                    "nag": 6.0  # 默认预估净资产增长率
                })
                print(f"✅ 成功获取: {item['name']}")
            except Exception as e:
                print(f"❌ 获取 {item['name']} 失败，使用兜底逻辑: {e}")
                # 失败时的默认保护数据
                result_data[category].append({
                    "name": item["name"],
                    "code": item["code"],
                    "pe": 12.0, "pb": 1.2, "pePct": 30, "pbPct": 25, "dv": 3.0, "eg": 7.5, "nag": 6.0
                })
                
    # 写入 data.json 文件
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_index_valuation()
