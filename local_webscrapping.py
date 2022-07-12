from bs4 import BeautifulSoup

with open('.gitignore/_ Restaurante Universitário.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('p')
    for tag in tags:
        print(tag.text)
