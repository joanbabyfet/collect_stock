from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def main():
    try:
        url = 'https://www.taifex.com.tw/cht/9/futuresQADetail' # 加權股價指數成分股暨市值比重
        resp = requests.get(url)
        resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
        soup = BeautifulSoup(resp.text, 'html.parser') # 通过html dom解析器采集数据
        items = soup.find_all('tr')

        odd_data = [] 
        even_data = []
        data = [] 
        for index in range(len(items)): # 通过索引遍历
            if index == 0: continue # 第1行为栏目略过
            tds         = items[index].find_all('td')
            sort        = tds[0].get_text(strip=True) # 排行, strip干掉字符串首尾空白
            stock_id    = tds[1].get_text(strip=True) # 證券代号
            stock_name  = tds[2].get_text(strip=True) # 證券名稱
            proportion  = tds[3].get_text(strip=True) # 市值佔大盤比重
            if stock_name != '': # 没有证券名忽略
                odd_data.append([sort, stock_id, stock_name, proportion])

            sort        = tds[4].get_text(strip=True) # 排行
            stock_id    = tds[5].get_text(strip=True) # 證券代号
            stock_name  = tds[6].get_text(strip=True) # 證券名稱
            proportion  = tds[7].get_text(strip=True) # 市值佔大盤比重
            if stock_name != '':
                even_data.append([sort, stock_id, stock_name, proportion])
        data = odd_data + even_data # 排行正序完整数据
        
        col_1 = []
        col_2 = []
        col_3 = []
        col_4 = []
        for index in range(len(data)):
            col_1.append(data[index][0])
            col_2.append(data[index][1])
            col_3.append(data[index][2])
            col_4.append(data[index][3])

        headers  = ['排行', '證券代号', '證券名稱', '市值佔大盤比重']
        export_data = {} # 组装数据, 类型为字典
        export_data[headers[0]] = col_1
        export_data[headers[1]] = col_2
        export_data[headers[2]] = col_3
        export_data[headers[3]] = col_4
        df = pd.DataFrame(export_data)
        filename = 'stock_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.csv' # 导出文件名
        df.to_csv(filename, index=False, header=True, encoding='utf-8-sig') # utf-8-sig 解决csv乱码
        print('导出csv成功')
    except:
        print('导出csv失败')

if __name__ == '__main__': # 主入口
    main()