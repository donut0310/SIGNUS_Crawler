from url_list import List
from bs4 import BeautifulSoup

from post_wash import post_wash
from datetime import timedelta
import datetime
from date_cut import date_cut_dict
import tag
from img_size import img_size
from url_parser import URLparser



#게시판 n페이지를 받으면, 그 페이지의 포스트 url 리스트 반환
def Parsing_list_url(URL, bs):
	List = []
	posts = bs.find("div", {"class": 'news mynews section _prs_nws'}).find("ul",{"class":"type01"}).find_all("li", id = True)
	for post in posts:
		List.append(post)
	return List

# 날짜 form 변경
def change_date_form(dateform):
	#일 => 7일 max
	#시간 => 23시간
	#분 =>59분
	#초 => 59초
	current_time = datetime.datetime.now()
	date=''
	timeCheck = ['일','시간','분','초']
	for time in timeCheck:
		if time in dateform:
			if time == "일":
				parsing_date = int(dateform.split("일")[0])
				date = str(current_time - datetime.timedelta(days = parsing_date)).split('.')[0]
				return date
			elif time == "시간":
				parsing_date = int(dateform.split("시간")[0])
				date = str(current_time - datetime.timedelta(hours = parsing_date)).split('.')[0]
				return date
			elif time == "분":
				parsing_date = int(dateform.split("분")[0])
				date = str(current_time - datetime.timedelta(minutes= parsing_date)).split('.')[0]
				return date
			elif time == "초":
				parsing_date = int(dateform.split("초")[0])
				date = str(current_time - datetime.timedelta(seconds = parsing_date)).split('.')[0]
				return date		
	date = str(dateform).split('.')[0]
	return date

#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(bs, URL):
	return_data = []
	post_data = {}
	title = bs.find("dt").get_text(" ", strip = True)
	author = ''
	date = ''
	domain = ''
	dateform = bs.find("dd",{"class":"txt_inline"}).get_text(" ",strip = True).split(" ")[1]
	date = change_date_form(dateform)
	post = bs.find("dd", {"class": "txt_inline"}).find_next('dd').get_text(" ", strip = True)
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	tag_done = tag.tagging(URL, title)
	list_url = bs.find("dt").find("a")['href']
	list_post = URLparser(list_url)
	list_post = BeautifulSoup(list_post,'html.parser')

	if list_post.find("meta", {"property": "og:image"}) is None:
		img = 7
	else:
		try:
			img = list_post.find("meta", {"property": "og:image"}).get("content")	#게시글의 첫번째 이미지를 가져옴.
			if 1000 <= len(img):
				img = 7
			else:
				if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
					pass 
				elif img.startswith("//"):
					img = "http:" + img
				else:
					img = domain + img
		except:
			img = 7
	if img != 7: 
		if img_size(img):
			pass
		else:
			img = 7
	
	#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[], img:1, 'view':0} 같은 형식
	post_data['title'] = title.upper()
	post_data['author'] = author
	post_data['date'] = date
	post_data['post'] = post.lower()
	post_data['tag'] = tag_done 	
	post_data['img'] = img
	post_data['url'] = list_url

	return_data.append(post_data)
	return_data.append(title)
	return_data.append(date)
	return return_data



#url을 받으면 Page를 변환시켜서, 변환된 url 반환
def Change_page(url, page):	
	url_done = url + str(page)
	return url_done


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출
	# domain = https://www.example.com
	return domain