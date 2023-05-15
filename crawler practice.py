from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()
url = 'https://www.jianshu.com/p/85f4624485b9'
r = session.get(url)
r.html.absolute_links

def get_text_link_from_sel(sel):
    mylist = []
    try :
        results= r.html.find(sel)
        for result in results :
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext,mylink))
        return mylist
    except :
        return None

sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
df = pd.DataFrame(get_text_link_from_sel(sel))
df.columns = ['text', 'link']
df.to_csv('E:/大一下学期/SI100/My-own-python-library/output.csv', encoding='gbk', index=False)