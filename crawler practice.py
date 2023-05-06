from requests_html import HTMLSession
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

sel = 'body > div.note > div.post > div.article > div.show-content > div > p:nth-child(6) > a'
print(get_text_link_from_sel(sel))
