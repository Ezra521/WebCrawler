import requests
import json
from pyecharts import Bar

# url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=568cec564ccadb5f1b29311ece2288f1'
# 后来-刘若英  网易云音乐
url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_254574?csrf_token=28ed1d804ba9ca1311a0c002053bef6a'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    #'Referer': 'http://music.163.com/song?id=551816010',

    'Referer': 'http://music.163.com/#/song?id=254574',#后来
    'Origin': 'http://music.163.com',
    'Host': 'music.163.com'
}
# 加密数据，直接拿过来用
user_data = {
   # 'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
   # 'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'

    'params':'fe7DvwzHO6HkkEpj7dl7bjsMcXWDbyNq7i8qBBVUBA6Pc8ja/KOi8kBpUCTcH5Pa+3QPMGTjzDn4dOGhPmVSuAHCsKRqG2Alb+6kc4oSpdxEUA4LjyHRWDSkmzdVp3joYnezX58xk7eAjVM5LKRIJn9Ji+vKfkzDBEN4ffPYAZ3EMVhccfdoEPD84Epz3f41hduRAge5AFKg5xwZVyKzYVxMDymQQv4+WXLUtq1he+w=',
    'encSecKey':'0215454db5a90ee639e83711f43a678a2b7d3cdc889dc3eab5c8eac9eff6e6525d0f0e67f8fb486c5593821f5811dce900c1c5a53a5cf36e7165e1876a92eb8d9d04d0e936cb5698b8adda4be580941e60af31d9c90d9e955ef763616c17ecce5b06bd3100e59f50c65eb1dd18b022bbb3d43f16d188b346ad92840a67b7be17'
}

response = requests.post(url, headers=headers, data=user_data)

data = json.loads(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
    item = {
        'nickname': hotcommment['user']['nickname'],
        'content': hotcommment['content'],
        'likedCount': hotcommment['likedCount']
    }
    hotcomments.append(item)

# 获取评论用户名，内容，以及对应的获赞数
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

bar = Bar("热评中点赞数示例图")
bar.add( "点赞数",nickname, liked_count, is_stack=True,mark_line=["min", "max"],mark_point=["average"])
bar.render()


from wordcloud import WordCloud
import matplotlib.pyplot as plt

content_text = " ".join(content_list)
wordcloud = WordCloud(font_path=r"D:\simhei.ttf",max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()