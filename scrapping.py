from requests_html import HTMLSession


def scrapping():
    session = HTMLSession()
    file_web = open('web.html','w+')
    url = input("Please insert a web to scrap: ")
    r = session.get(url)
    r.html.render()
    file_web.write(r.html.html)
    file_web.close()

if __name__ == '__main__':
    scrapping()
    
