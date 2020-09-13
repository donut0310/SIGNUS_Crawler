from bs4 import BeautifulSoup
from url_list import List
from post_wash import post_wash
import datetime
from date_cut import date_cut_dict
import tag
from img_size import img_size


#게시판 page_url 을 받으면, 그 페이지의 포스트 url 들을 반환
def Parsing_list_url(URL, bs):
	List = []
	domain = Domain_check(URL['url'])

	#리스트 반환
	#posts = bs.find("table", {"class": 'bbs_ltype tbl30'}).findAll("tr")
	posts = bs.find("table", {"class": 'bbs_ltype interview tbl30'}).findAll("tr")
	posts = posts[1:]
	for post in posts:
		target = post.find("a")['href']
		page = target
		List.append(domain + '/' + page)

	return List



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(bs, post_url, URL):
	try:
		return_data = []
		post_data = {}
		domain = Domain_check(URL['url'])

		title = bs.find("span", {"class": "col_blue"}).get_text(" ", strip = True)
		author = "0"
		date = bs.find("dl", {"class": "explainInfoBx"}).find("dd").text.strip()
		date = date + " 00:00:00"
		date = str(datetime.datetime.strptime(date, "%Y.%m.%d %H:%M:%S"))
		post = bs.find("p", {"class": "tx"}).get_text(" ", strip = True)
		post = post_wash(post)
		tag_done = tag.tagging(URL, title)
		if bs.find("div", {"class": "img"}).find("img") is None:
			img = 1
		else:
			img = bs.find("div", {"class": "img"}).find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
			if 1000 <= len(img):
				img = 1
			else:
				if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
					pass
				elif img.startswith("//"):
					img = "http:" + img
				else:
					img = domain + img
		if img != 1:
			if img_size(img):
				pass
			else:
				img = 1

		#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[],'fav_cnt':0,'view':0} 같은 형식
		post_data['title'] = title.upper()
		post_data['author'] = author.upper()
		post_data['date'] = date
		post_data['post'] = post.lower()
		post_data['tag'] = tag_done 	# 태그1/태그2/태그3/태그4/.../ 같은 형식의 태그string이 들어간다.
		post_data['img'] = img
		post_data['url'] = post_url

		return_data.append(post_data)
		return_data.append(title)
		return_data.append(date)
		return return_data
	except:
		return None



#url을 받으면 Page를 변환시켜서, 변환된 url 반환
def Change_page(url, page):
	url_done = url + str(page)

	return url_done


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2] + "/" + url.split('/')[3]		#도메인 url 추출

	return domain