import mimetypes
import requests
from lxml import html 

def test_for_meta_redirections(r):
    print("new redirect")
    print(r.text)
    html_tree = html.fromstring(r.text)
    attr = html_tree.xpath("//meta[translate(@http-equiv, 'REFSH', 'refsh') = 'refresh']/@content")
    print(attr)
    wait, text = attr[0].split(";")

    if text.lower().startswith(" url="):
        url = text[7:]
        print(url)
        if not url.startswith('http'):
            # Relative URL, adapt
            url = r.url+url
        return True, url
    return False, None


def follow_redirections(r, s):
    """
    Recursive function that follows meta refresh redirections if they exist.
    """
    redirected, url = test_for_meta_redirections(r)
    if redirected:
        print("follow again, to", url)
        r = follow_redirections(s.get(url), s)
    return r



s = requests.session()
r = s.get('http://challenges.ctfd.io:30034')
# test for and follow meta redirects
r = follow_redirections(r, s)

print(r)