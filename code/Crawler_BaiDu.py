import requests
import re  # 要用正则表达式需引入re库


def crawler_search_BaiDu(search_word):
    """爬虫-爬取百度翻译"""
    try:
        url = 'https://fanyi.baidu.com/sug'
        word = search_word
        dat = {
            'kw': word
        }
        req = requests.post(url, data=dat)
        result1 = str(req.json())
        reg = re.compile("'v': '(?P<word>.*?)'")  # 这行和下面两行代码下个步骤再做解释
        result2 = reg.search(result1)
        return result2.group(0).split(':')[1].strip().strip("'")
    except:
        return '查询失败'


