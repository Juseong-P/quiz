import requests
import re
from bs4 import BeautifulSoup

# res = requests.get('http://google.com')
# print('응답코드 : ', res.status_code)  # 200 이면 정상
#
# if res.status_code == requests.codes.ok:
#     print('정상입니다.')
# else:
#     print('문제가 생겼습니다.')
#
# print(len(res.text))
# print(res.text)

# with open('mygoogle.html', 'w', encoding = 'utf-8') as f: # html 파일로 저장
#     f.write(res.text)

# def print_match(m):
#     if m:
#         print('m.group() : ', m.group()) # 일치하는 문자열 반환
#         print('m.string  : ', m.string)  # 입력받은 문자열
#         print('m.start() : ', m.start()) # 일치하는 문자열의 시작 index
#         print('m.end()   : ', m.end())   # 일치하는 문자열의 끝 index
#         print('m.span()  : ', m.span())  # 일치하는 문자열의 시작/끝 index
#     else:
#         print('No matching')
#
# p = re.compile('ca.e')
# m = p.match('careless')
# print_match(m)
#
# se = p.search('good care')
# print_match(se)
#
# fi = p.findall('good careless cafe')
# print(fi)

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)           # soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs)     # a element 의 속성 정보를 출력
# print(soup.a["href"])   # a elemanet 의 href 속성 '값' 정보를 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))     # class="Nbtn_upload" 인 a element 찾기
# print(soup.find(attrs={"class":"Nbtn_upload"}))          # class="Nbtn_upload" 인 어떤 element 찾기
# print(soup.find("li", attrs={"class":"rank01"}))          # class="Nbtn_upload" 인 어떤 element 찾기
rank1 = soup.find("li", attrs={"class":"rank01"})          # class="Nbtn_upload" 인 어떤 element 찾기
# print(rank1.a)
print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling     # = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# ranks = rank1.find_next_siblings("li")
# print(ranks)

cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())
    link = cartoon.a["href"]
    print("https://comic.naver.com"+link)
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)