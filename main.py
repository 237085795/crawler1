import requests
import os
import time
import re

INDEX = 0
interval = 2  # 爬取间隔时间

# TOKEN = "d9f914aa0a34ae231318b38fbdf351b2"  # dujinbo@huayiwen.com
#
#
TOKEN = "2c5009b29729c48e2d5c7c501ad3b631"  # huayiwen888@gmail.com

novel_root = './novel_xml_text'
pic_root = './novel_pic_text'
summary_root = './novel_summary_text'


def search(book_name):
    global INDEX, interval, TOKEN
    INDEX = 0  # 重置索引

    url_search = "https://rest3.radishfiction.com/search/v2/stories"
    p_search = {
        "access_token": f"{TOKEN}",
        "keyword": f"{book_name}",  # book name
        "limit": "20",  # item_num
        "page": "1",
        "order": "-1",
        "sort": "popularity",
    }
    resp_search = requests.get(url_search, params=p_search)

    search_dict = resp_search.json()["items"][0:10]  # 获取前10个搜索结果进行严格匹配
    for item in search_dict:
        if item["story"]["title"].lower().strip() == book_name.lower().strip() or \
                item["story"]["seasons"][0]["title"].lower().strip() == book_name.lower().strip():
            season_list = item["story"]["seasons"]
            for s in season_list:
                s_id = s["id"]
                if season(s_id, book_name) == 1:
                    print(f"{book_name}中止爬取")
                    return
            print(f"{book_name}爬取完成")
            return
    # 匹配不到报错
    with open('error.txt', mode='a', encoding='utf-8') as f:
        f.write(f'{book_name}:书名错误,无法爬取内容\n')
    print(f'{book_name}:书名错误,无法爬取内容')


def season(season_id, book_name):
    global interval, TOKEN

    url_season = f'https://rest3.radishfiction.com/story/v2/seasons/{season_id}/episodes'
    p_season = {
        "access_token": f"{TOKEN}",
        "limit": "200",  # item_num
        "page": "1",
    }
    resp_season = requests.get(url_season, params=p_season)

    chapter_list = resp_season.json()["items"]
    for c in chapter_list:
        chapter_id = c["id"]
        if content(book_name, chapter_id) == 1:
            return 1
        time.sleep(interval)


def content(book_name, chapter_id):
    global INDEX, interval, TOKEN

    url_chapter = f'https://rest3.radishfiction.com/episode/v3/episodes/{chapter_id}?access_token={TOKEN}'
    resp_chapter = requests.get(url_chapter)
    # print(resp_chapter.json())

    if 'errorCode' in resp_chapter.json():
        return 1

    # is_free = resp_chapter.json()["episode"]["isFree"]
    # is_purchased = resp_chapter.json()["episode"]["isPurchased"]
    # if not is_free and not is_purchased:
    #     with open('error.txt', mode='a', encoding='utf-8') as f:
    #         f.write(f'{book_name}第{INDEX}章节不是免费或者未购买\n')
    #     print(f'{book_name}第{INDEX}章节不是免费或者未购买')
    #     return 1

    text = resp_chapter.json()["episode"]["text"]
    episode_title = resp_chapter.json()["episode"]["title"]
    replace_dic = {
        '&': '&amp;',
        '?': '？',
        ':': '：',
        '"': '“',
        '/': ' ',
        '\\': ' ',
        '<': ' ',
        '>': ' ',
        '|': ' ',
        '*': ' ',
        '\t': ' ',
    }
    episode_title = replace_by_dic(episode_title, replace_dic)
    book_name = replace_by_dic(book_name, replace_dic)

    INDEX += 1
    if write_to_file(book_name, episode_title, text) == 1:
        return 1


def write_to_file(book_name, episode_title, text):
    global INDEX
    if not os.path.exists(novel_root):
        os.makedirs(novel_root)
    file = f"{novel_root}/{book_name}.txt"
    if not os.path.isfile(file):
        open(file, 'w').close()
    elif INDEX == 1:
        print(book_name, "已存在，跳过爬取，若需要重新爬取，请删除文件后重试")
        return 1

    text = clean_html(text)
    text = f'<chapter>\n\t<number>{INDEX}</number>\n\t<title>{episode_title}</title>\n\t<content>\n{text}\n\t</content>\n</chapter>\n'

    with open(file, mode='a', encoding='utf-8') as f:
        f.write(text)
    print(f"{episode_title}爬取完成")


def clean_html(html):  # 利用nltk的clean_html()函数将html文件解析为text文件
    cleaned = re.sub(r"<p.*?>[\n]*", "", html)
    cleaned = re.sub(r"<b.*?>", "", cleaned)
    cleaned = re.sub(r"<i.*?>", "", cleaned)
    cleaned = re.sub(r"<p.*?>", "", cleaned)
    cleaned = re.sub(r"<g.*?>", "", cleaned)
    cleaned = re.sub(r"<em.*?>", "", cleaned)
    cleaned = re.sub(r"<u.*?>", "", cleaned)
    cleaned = re.sub(r"<sup.*?>", "", cleaned)
    cleaned = re.sub(r"<storng.*?>", "", cleaned)
    cleaned = re.sub(r"<h1.*?>", "", cleaned)

    replace_dic = {
        '。': '.',
        '，': ',',
        '：': ':',
        '；': ';',
        "‘": "'",
        '“': '"',
        '（': '(',
        '）': ')',
        '！': '!',
        '？': '?',
        '”': '"',
        "’": "'",
        "…": "...",
        '\xa0': ' ',
        '</p>': '\n',
        '</i>': '',
        '</b>': '',
        '<br />': ' ',
        '<br>': ' ',
        '</g>': '',
        '</u>': '',
        '</em>': '',
        '</sup>': '',
        '</strong>': '',
        '</h1>': '',
        '&amp;': '&',
        '&quot;': '"',
        '&nbsp;': ' ',
        '￼': '',
        '&': '&amp;',
        # '<': '&lt;',
        # '>': '&gt;',
    }
    cleaned = replace_by_dic(cleaned, replace_dic)
    return cleaned.strip()


def read_catalogue():
    f = open("./catalogue.txt", "r")
    book_name_list = []
    for line in f.readlines():
        line = line.strip()  # 去掉每行头尾空白
        book_name_list.append(line)
    return book_name_list


def get_token():
    url = "https://rest3.radishfiction.com/auth/v1/sign-in"
    d = {
        "type": "normal",
        "username": "",
        "password": ""
    }
    resp = requests.post(url, data=d)
    print(resp.json())


def get_pic(book_name):
    url_search = "https://rest3.radishfiction.com/search/v2/stories"
    p_search = {
        "access_token": f"{TOKEN}",
        "keyword": f"{book_name}",  # book name
        "limit": "20",  # item_num
        "page": "1",
        "order": "-1",
        "sort": "popularity",
    }
    resp_search = requests.get(url_search, params=p_search)

    search_dict = resp_search.json()["items"][:10]
    for item in search_dict:
        if item["story"]["title"].lower().strip() == book_name.lower().strip() or \
                item["story"]["seasons"][0]["title"].lower().strip() == book_name.lower().strip():
            pic_url = item["story"]["seasons"][0]["coverUrl"]
            download_pic(pic_url, book_name)
            return

    with open('error.txt', mode='a') as f:
        f.write(f'{book_name}:书名错误,下载封面失败\n')
    print(f'{book_name}:书名错误,下载封面失败')


def download_pic(url, book_name):
    resp = requests.get(url)

    text = resp.content
    replace_dic = {
        '?': '？',
        ':': '：',
        '"': '“',
        '/': ' ',
        '\\': ' ',
        '<': ' ',
        '>': ' ',
        '|': ' ',
        '*': ' ',
    }
    book_name = replace_by_dic(book_name, replace_dic)

    file = f"{pic_root}/{book_name}.png"
    if not os.path.exists(pic_root):
        os.makedirs(pic_root)
    if os.path.isfile(file):
        print(f"{book_name}:封面已存在")
        return

    with open(file, mode='wb') as f:
        f.write(text)
    print(f"{book_name}:封面下载完成")


def replace_by_dic(s, dic):
    for key, value in dic.items():
        s = s.replace(key, value)
    return s


def get_resume(book_name):
    url_search = "https://rest3.radishfiction.com/search/v2/stories"
    p_search = {
        "access_token": f"{TOKEN}",
        "keyword": f"{book_name}",  # book name
        "limit": "20",  # item_num
        "page": "1",
        "order": "-1",
        "sort": "popularity",
    }
    resp_search = requests.get(url_search, params=p_search)
    # print(resp_search.json())

    search_dict = resp_search.json()["items"][0:5]  # 获取前5个搜索结果进行严格匹配
    for item in search_dict:
        if item["story"]["title"].lower().strip() == book_name.lower().strip() or \
                item["story"]["seasons"][0]["title"].lower().strip() == book_name.lower().strip():
            txt = item["story"]["seasons"][0]["summary"]
            # print(txt)
            replace_dic = {
                '&': '&amp;',
                '?': '？',
                ':': '：',
                '"': '“',
                '/': ' ',
                '\\': ' ',
                '<': ' ',
                '>': ' ',
                '|': ' ',
                '*': ' ',
                '\t': ' ',
            }
            book_name = replace_by_dic(book_name, replace_dic)
            if not os.path.exists(summary_root):
                os.makedirs(summary_root)
            with open(f'{summary_root}/{book_name}.txt', 'w', encoding='utf-8') as f:
                f.write(txt)
            print(f'{book_name}:\t\t\t\tover!!!')
            return
    with open('error.txt', mode='a', encoding='utf-8') as f:
        f.write(f'{book_name}:书名错误,无法爬取内容\n')
    print(f'{book_name}:书名错误,无法爬取内容')


if __name__ == '__main__':
    # get_token()

    for book_name in read_catalogue():
        search(book_name)
        get_pic(book_name)
        get_resume(book_name)

        time.sleep(interval)
    print("列表处理完成")
