from url_list import List
from post_wash import post_wash
import datetime
from date_cut import date_cut_dict
from img_size import img_size



#게시판 n페이지를 받으면, 그 페이지의 포스트 url 리스트 반환
def Parsing_list_url(URL, bs):
	List = []
	domain = Domain_check(URL['url'])

	posts = bs.find("tbody").findAll('tr')

	for post in posts:
		if post.find("a") is None:
			continue
		else:
			post_url = post.find("a")["href"]
			post_url = post_url.replace("¤", "&curren")	#"&curren" 문자가 "¤"로 가져와지는 문제로 인해 추가
		#post_url 이 외부링크면 바로 List 추가, 아니면 domain 추가한 후 List 추가
		if post_url.startswith("http://"):
			List.append(post_url)
		else:
			post_url = domain + "/bbs/" + post_url
			List.append(post_url)
	return List



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(bs, post_url, URL):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])

	title = bs.find("thead").find("td", {"class": "subject-value"}).get_text(" ", strip = True)
	author = bs.find("thead").find("td", {"class": "writer"}).text.strip()
	if author.find("관리자") != -1:
		author = "0"
	date = bs.find("thead").find("td", {"class": "date"}).text.strip()
	date = date + " 00:00:00"
	date = str(datetime.datetime.strptime(date, "%Y.%m.%d %H:%M:%S"))
	post = bs.find("tbody").find("td", {"class": "content"}).get_text(" ", strip = True)
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	if bs.find("tbody").find("img") is None:
		img = 1
	else:
		img = bs.find("tbody").find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
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

	post_data['title'] = title.upper()
	post_data['author'] = author.upper()
	post_data['date'] = date
	post_data['post'] = post.lower()
	post_data['img'] = img
	post_data['url'] = post_url

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

	return domain