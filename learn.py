# import os
# import requests
# import aiofiles
# import aiohttp
# import asyncio
# import time
# import re
# from Crypto.Cipher import AES
#
# n = 0
# base_url = "https://www.91kanju.com/vod-play/59831-1-5.html"
#
# def get_m3m8(url):
#     obj = re.compile(r"url: '(?P<url>.*?)',", re.S)
#     resp = requests.get(url)
#     # print(resp.text)
#     url_m3u8_first = obj.search(resp.text).group('url')
#     # print(url_m3u8_first)
#     resp_m3u8_first = requests.get(url_m3u8_first, verify=False)
#     print(resp_m3u8_first.text)
#
# def get_key():
#     return b'df407ac49fa8e99d'
#
# async def download(url, session, aes):
#     global n
#     n += 1
#     index = str(n).zfill(4)
#     async with session.get(url) as resp:
#         async with aiofiles.open(f"./video/{index}.ts", mode='wb') as f:
#             bs = await resp.content.read()
#             # await f.write(aes.decrypt(bs))
#             await f.write(bs)
#     print(index, "over")
#
# async def aio_download(key):
#     tasks = []
#     aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
#     async with aiohttp.ClientSession() as session:
#         async with aiofiles.open('luoji.m3u8', mode='r') as f:
#             async for line in f:
#                 if line.startswith('#'):
#                     continue
#                 line = line.strip()
#                 # line = 'https://v2.88zy.site' + line
#                 # '/20210710/coeq6dlx/1500kb/hls/WScSUVCx.ts'
#                 # "https://v2.88zy.site/20210710/coeq6dlx/1500kb/hls/kymiTz0S.ts"
#                 task = asyncio.create_task(download(line, session, aes))
#                 tasks.append(task)
#
#             await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     # get_m3m8(base_url)
#
#     t1 = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(aio_download(get_key()))
#     t2 = time.time()
#     print(t2 - t1)
#
#     # os.system('copy /b .\\video\\*.ts .\\video\\luoji.mp4')
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# import time
# web = Chrome()
# # web.get("http://www.lagou.com")
# # time.sleep(1)
# # web.find_element_by_xpath('//*[@id="cboxClose"]').click()
# # time.sleep(1)
# # web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
# # time.sleep(1)
# # web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# # web.switch_to.window(web.window_handles[-1])
# # print(web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text)
# # web.close()
# # web.switch_to.window(web.window_handles[0])
# # print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
# web.get('https://www.meijuttb.com/play/96997-2-5.html')
# time.sleep(5)
# iframe_1 = web.find_element_by_xpath('//*[@id="cciframe"]')
# web.switch_to.frame(iframe_1)
# iframe_2 = web.find_element_by_xpath('//*[@id="player"]/iframe')
# web.switch_to.frame(iframe_2)
# src= web.find_element_by_xpath('//*[@id="playerCnt"]/video').get_property('src')
# print(src)
# web.switch_to.default_content()
# title = web.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div[1]/a').text
# print(title)
# web.switch_to.default_content()
# print(web.find_element_by_xpath('/html/body/div[5]/div/div[1]/b').text)

# import time
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
#
# opt = Options()
# opt.add_argument('--headless')
# base_url = 'http://www.zyshow.net/11dianrechaodian/'
# page_num = 5
# web_list = []
# save_file_name = 'topic_11point.txt'
# web_list.append(base_url)
# for i in range(1, page_num + 1):
#     web_list.append(f'{base_url}{i}.html')
#
# for url in web_list:
#     web = Chrome(options=opt)
#     web.get(url)
#     trs = web.find_elements_by_xpath('//*[@id="event_detail"]/div/table/tbody/tr')
#     # '//*[@id="event_detail"]/div/table/tbody/tr[2]'
#     index = 1
#     # '//*[@id="event_detail"]/div/table/tbody/tr[2]/td[2]'
#     for tr in trs:
#         flag = tr.get_attribute('onmouseover')
#         if flag == None:
#             continue
#         content = tr.find_element_by_xpath('./td[2]').text + '\n'
#         with open(save_file_name, 'a', encoding='utf-8') as f:
#             f.write(content)
#     print(url, "over")
# print('all over')
# import time
#
# from selenium.webdriver import Chrome
# from chaojiying import Chaojiying_Client
#
# web= Chrome()
# web.get('http://www.chaojiying.com/user/login/')
#
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('13110768226')
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('12345678')
# img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# chaojiying = Chaojiying_Client('13110768226', '12345678', '920350')
# verify_code = chaojiying.PostPic(img, 1902)['pic_str']
#
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
# time.sleep(4)
#
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
#
# from xml.dom import minidom
#
# #  ??????????????????
#
# # ??????doc?????????chapter????????????
# impl = minidom.getDOMImplementation()
# doc = impl.createDocument(None, 'chapter', None)
# # ?????????element??????
# chapter = doc.documentElement
#
# # doc = minidom.Document()
# # chapter = doc.createElement('chapter')
# # doc.appendChild(chapter)
#
# # ??????????????????
# number = doc.createElement('number')
# title = doc.createElement('title')
# content = doc.createElement('content')
#
# # ????????????????????????????????????????????????
# number.appendChild(doc.createTextNode('111111111'))
# number.setAttribute('a_n', '111')  # ????????????
# title.appendChild(doc.createTextNode('chapter1'))
# content.appendChild(doc.createTextNode('??????'))
#
# # ?????????????????????????????????????????????
#
# chapter.appendChild(number)
# chapter.appendChild(title)
# chapter.appendChild(content)
#
# # print(doc.toprettyxml())  # ????????????????????????
# # print(doc.toxml())  # ???????????????
#
# with open('test.xml', 'w', encoding='utf-8') as fp:
#     doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
# # ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????xml???????????????
#
# from xml.dom import minidom
#
# # ??????dco??????
# doc = minidom.parse('test.xml')
# # doc = minidom.parseString('<a>foo<b>thing</b></a>')
# root = doc.documentElement
# # ??????tag??????????????????
# li = root.getElementsByTagName('number')
# for l in li:
#     print(l.childNodes[0].data)  # ??????????????????????????????data????????????'TEXT_NODE'???????????????????????????
#     print(l.getAttribute('a_n'))  # ????????????
#     # ???????????????????????????
#     print(l.parentNode.nodeName)  # ????????????
#
# # ???????????????'ELEMENT_NODE'?????????????????? 'TEXT_NODE'?????????????????? 'ATTRIBUTE_NODE'???????????????
# print(root.nodeType)  # out:


# from xml.etree import ElementTree as ET
#
# tree = ET.parse('test.xml')
# root = tree.getroot()  # ?????? XML ???????????????????????? Element
#
# # root = ET.fromstring('<a>foo<b>thing</b></a>')  # ????????????????????????
# # tree = ET.ElementTree(root)
#
# tree_node = ET.Element("node1", {'a': '1', 'b': '2', 'c': '3'})
# tree_node.text = "Hello world"
# tree_node.tail = "Bye"
# tree_node.set('d', '2')  # ??????????????????????????????????????????
# print(tree_node.tag)  # ?????? node1
# print(tree_node.text)  # ?????? "Hello world"
# print(tree_node.tail)  # ?????? "Bye"
# print(tree_node.attrib)  # ?????? {'a': '1', 'b': '2', 'c': '3', 'd': '2'}
# child = ET.SubElement(tree_node, "child1", {'att': '123'})
# # child = ET.Element("child", {'att': '123'})
# # tree_node.append(child)
# # tree_node.remove(child)
# # =========================================================
#
# for child in root:
#     for item in child:  # ???????????????????????????????????????????????????????????????
#         print(item.tag)
#
# # print(root[0].tag, root[0][0].tag)  # ????????????????????????
# for country in root.findall('country'):  # ??????????????????
# # for country in root.iter("country"):  # ??????????????????
#     # print("index.tag",index.tag)
#     rank = country.find('rank').text  # ?????????????????????????????????Element
#     name = country.get('name')  # ???????????????
#     print(rank, name)
#
# # =========================================================
# print(ET.tostring(tree_node, encoding='unicode'))
# # ?????? tostring() ??????????????? encoding="unicode"?????????????????? byte ??????
# tree.write("out.xml", encoding="UTF-8")
# # ??????????????????????????????UTF-8????????????????????????"utf-8"???????????????????????????

# import xml.etree.ElementTree as ET
# #
# tree = ET.parse('file1.txt')
#
# root = tree.getroot()
# for child in root:
#     print(child.tag)
#     print(child.text)
# print(root.tag)


# str = '@@@###$$%%^^^&&&&'
# dict = {
#     '@': '1',
#     '#': '2',
#     '$': '3'
# }
#
# str = replace_by_dic(str, dict)
# print(str)

# chapter_node = ET.Element('chapter')
# number_node = ET.Element('number')
# title_node = ET.Element('title')
# content_node = ET.Element('content')
#
# number_node.text = "1"
# title_node.text = "change"
# content_node.text = "tst & 2333"
#
# chapter_node.append(number_node)
# chapter_node.append(title_node)
# chapter_node.append(content_node)
#
# tree = ET.ElementTree(chapter_node)
#
# tree.write('file1.txt', 'utf-8', xml_declaration=True)

# from xml.dom import minidom
# open('test.txt', 'w').close()
# for i in range(5):
#     impl = minidom.getDOMImplementation()
#     doc = impl.createDocument(None, 'chapter', None)
#     # ?????????element??????
#     chapter = doc.documentElement
#
#     number = doc.createElement('number')
#     title = doc.createElement('title')
#     content = doc.createElement('content')
#
#     number.appendChild(doc.createTextNode(str(i)))
#     title.appendChild(doc.createTextNode(f'chapter{i}'))
#     content.appendChild(doc.createTextNode(f'??????{i}'))
#
#     chapter.appendChild(number)
#     chapter.appendChild(title)
#     chapter.appendChild(content)
#
#     with open('test.txt', 'a', encoding='utf-8') as f:
#         doc.writexml(f, indent='', addindent='\t', newl='\n', encoding="UTF-8")

# def tol(file1, gui):  # ?????????????????????????????????or ????????????
#     import re
#     patt = re.compile(gui)
#     # print(type(patt))
#     f = open(file1, 'r', encoding='utf-8')
#     # print(type(f))
#     try:
#         return len(patt.findall(f.read()))  # findall??????str?????????????????????file ?????????????????????????????????
#     finally:  # ?????????????????????????????????finally???????????????
#         f.close()


#
# print(tol('./novel/A SECOND CHANCE AT LOVE... OR ABSOLUTE RUIN/1.A SECOND CHANCE AT LOVE... OR ABSOLUTE RUIN._A SECOND CHANCE AT LOVE... OR ABSOLUTE RUIN._Episode #1 - Sage.txt', r'\w+'))

#
import os
import re

#
# COUNT = 0
# NUM = 0
#
# def replace_by_dic(s, dic):
#     for key, value in dic.items():
#         s = s.replace(key, value)
#     return s
#
#
# def clean_html(html):  # ??????nltk???clean_html()?????????html???????????????text??????
#     # cleaned = re.sub(r"<p.*?>[\n]*", "", html)
#     # cleaned = re.sub(r"<b.*?>", "", cleaned)
#     # cleaned = re.sub(r"<i.*?>", "", cleaned)
#     # cleaned = re.sub(r"<p.*?>", "", cleaned)
#
#     replace_dic = {
#       '&nbsp;': ' ',
#         # '???': '.',
#         # '???': ',',
#         # '???': ':',
#         # '???': ';',
#         # "???": "'",
#         # '???': '"',
#         # '???': '(',
#         # '???': ')',
#         # '???': '!',
#         # '???': '?',
#         # '???': '"',
#         # "???": "'",
#         # "???": "...",
#         # '\xa0': ' ',
#         # # '<p>': '',
#         # '</p>': '\n',
#         # # '<i>': '',
#         # '</i>': '',
#         # # '<b>': '',
#         # '</b>': '',
#         # '<br />': ' ',
#         # '<br>': ' ',
#         # '&quot;': '"',
#         # '???': '',
#         # '': '',
#         # '': '',
#         # '': '',
#         # '&': '&amp;',
#         # '<': '&lt;',
#         # '>': '&gt;',
#     }
#     cleaned = replace_by_dic(html, replace_dic)
#     return cleaned.strip()
#
#
# # signal = '&amp;amp;'
# # signal_1 = '&amp;nbsp;'
# # signal_2 = '&amp;quot;'
#
# for root, dirs, files in os.walk(r"./novel_xml"):
#     for file in files:
#         # print(file)
#         with open(f"./novel_xml/{file}", mode='r', encoding='utf-8') as f:
#             txt = f.read()
#             # if signal_2 in txt:
#             txt = clean_html(txt)
#             with open(f"./novel_xml/{file}", 'w', encoding='utf-8') as fin:
#                 fin.write(txt)
#





# signal = '\n\n'
#
# for root, dirs, files in os.walk(r"./novel_xml"):
#     for file in files:
#         # print(file)
#         with open(f"./novel_xml/{file}", mode='r', encoding='utf-8') as f:
#             txt = f.read()
#             if signal in txt:
#                 for i in range(10):
#                     txt = txt.replace('\n\n', '\n')
#                     # txt = clean_html(txt)
#             with open(f"./novel_xml/{file}", 'w', encoding='utf-8') as fin:
#                 fin.write(txt)






# signal = '\n\n'
#
# for root, dirs, files in os.walk(r"./novel_xml"):
#     for file in files:
#         # print(file)
#         with open(f"./novel_xml/{file}", mode='r', encoding='utf-8') as f:
#             txt = f.read()
#             if signal in txt:
#                 print(f'{file}')

# print('all over')

# from pynput.mouse import Button, Controller
# import time
#
# mouse = Controller()
# # print(mouse.position)
# # time.sleep(3)
# # print('The current pointer position is {0}'.format(mouse.position))
# #
# #
# # ??????1???
# for i in range(10000):
#     mouse.click(Button.left, 1)
#     time.sleep(1)

# INDEX=1
#
# # text = f'<chapter>\n\t<number>{INDEX`}</number>\n\t<title>{episode_title}</title>\n\t<content>\n{text}\n\t</content>\n</chapter>\n'
# chapter = 'Kapitel'
#
# with open('3.txt','r',encoding='utf-8') as f:
#     with open('Verheiratet mit Schwager.txt','a',encoding='utf-8') as fin:
#         for line in f:
#             if chapter in line:
#                 if INDEX==1:
#                     line=line.replace('\n', '').replace('\r', '')
#                     fin.write(f'<chapter>\n\t<number>{INDEX}</number>\n\t<title>{line}</title>\n\t<content>\n')
#                     INDEX+=1
#                 else:
#                     line = line.replace('\n', '').replace('\r', '')
#                     fin.write(f'\n\t</content>\n</chapter>\n<chapter>\n\t<number>{INDEX}</number>\n\t<title>{line}</title>\n\t<content>\n')
#                     INDEX += 1
#             else:
#                 fin.write(line)
#         fin.write(f'\n\t</content>\n</chapter>\n')
#
# print('over')

# chapter = 'Kapitel'
#
# with open('3.txt','r',encoding='utf-8') as f:
#     for line in f:
#         if chapter in line:
#             print(line)
# with open('3.txt','a',encoding='utf-8') as fin:
#     for line in f:
#         if chapter in line:
#             line = line.replace(' - ',' ').replace(': ',' ').replace(' ??? ',' ').replace('  ',' ')
#             fin.write(line)
#         else:
#             fin.write(line)
