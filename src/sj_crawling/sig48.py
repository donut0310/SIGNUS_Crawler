from url_list import List
from post_wash import post_wash
from datetime import timedelta
import datetime
from date_cut import date_cut_dict
from img_size import img_size



#게시판 n페이지를 받으면, 그 페이지의 포스트 url 리스트 반환
def Parsing_list_url(URL, bs):
	List = []
	domain = Domain_check(URL['url'])
	posts = bs.find("div", {"class": 'boardList boardListService'}).find("ul",{"class":"list_wrap"}).find_all("li")
	for post in posts:
		url = post.find("a")["href"]
		url = domain + "/partspace/" + url
		List.append(url)
	return List

#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(bs, post_url, URL):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])
	title = bs.find("div", {"class": "viewTitle"}).find("p",{"class":"tit"}).get_text(" ", strip = True)
	author = ''

	current_time = datetime.datetime.now()
	non_splited_date = bs.find("div", {"class": "group"}).find("dd").get_text(" ", strip = True).split(" ~ ")
	date = non_splited_date[0]
	date = date + " 00:00:00"
	end_date = non_splited_date[1]
	end_date = end_date + " 00:00:00"
	date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
	if (date-current_time).days > 0:
		date = str(current_time).split(".")[0]
	else:
		date = str(date)
	post = bs.find("div", {"class": "con"}).get_text(" ", strip = True)
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	if bs.find("meta", {"property": "og:image"}) is None:
		img = 7
	else:
		try:
			img = bs.find("meta", {"property": "og:image"}).get("content")	#게시글의 첫번째 이미지를 가져옴.
			img = domain + img
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

	post_data['title'] = title.upper()
	post_data['author'] = author
	post_data['date'] = date
	post_data['post'] = post.lower()
	post_data['img'] = img
	post_data['url'] = post_url
	post_data['end_date'] = str(end_date)

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