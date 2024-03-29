from bs4 import BeautifulSoup
from selenium import webdriver
from url_list import List
from post_wash import post_wash
import datetime
import campuspick
from driver_agent import chromedriver
from date_cut import date_cut
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from img_size import img_size



#게시판 page_url 을 받으면, 그 페이지의 포스트 url 들을 반환
def Parsing_list_url(URL, page_url):
	List = []
	domain = Domain_check(URL['url'])

	#만약 driver이 켜져있으면 끄고, 없으면 그냥 진행
	try:
		driver.quit()
	except:
		pass

	driver = chromedriver()

	List.append(page_url)

	data = (driver, List)

	return data



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(driver, post_url, URL, recent_post):
	post_data_prepare = []
	domain = Domain_check(URL['url'])
	end_date = date_cut(URL['info'])
	now_num = 0
	repeat_num = 0
	post_driver = chromedriver()	# 포스트 페이지를 위한 드라이버
	driver.get(post_url)
	last_posts = [0]
	while 1:
		driver.find_element_by_tag_name("body").send_keys(Keys.END)
		time.sleep(1)

		html = driver.page_source
		bs = BeautifulSoup(html, 'html.parser')
		posts = bs.find("div", {"class": 'grid'}).find("div", {"class": 'grid-item'}).find_all("div",{"class":"grid-item"})
		#더이상 내릴 수 없으면 break
		if len(last_posts) == len(posts):
			break
		else:
			last_posts = posts


		for post in posts[now_num:]:
			if post.find("div",{"class":"item onclick"}) is None or post.find("div",{"class":"item_wrap"}) is None:
				pass
			else:
				try:
					post_data = {}
					url = post.find("div",{"class":"item onclick"}).get("onclick").split("'")[1]
					try:
						post_driver.get(url)
						#driver.get(url)
					except:
						if len(post_data_prepare) == 0:
							recent_post = None
						else:
							recent_post = post_data_prepare[0]['title']
						data = (post_data_prepare, recent_post)
						return data
					try:
						WebDriverWait(post_driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "time"))) #a.item을 발견하면 에이작스 로딩이 완료됬다는 가정
					except:
						if len(post_data_prepare) == 0:
							recent_post = None
						else:
							recent_post = post_data_prepare[0]['title']
						data = (post_data_prepare, recent_post)
						return data
					html_post = post_driver.page_source
					bs_post = BeautifulSoup(html_post, 'html.parser')

					title = bs_post.find("div",{"class":"col-md-12 start_article_info mobile_pre_article"}).find("h1").get_text(" ", strip = True)
					date = bs_post.find("div",{"class":"col-md-12 start_article_info mobile_pre_article"}).find("h3").get_text(" ", strip = True)
					date = date + " 00:00:00"
					date = str(datetime.datetime.strptime(date, "%Y . %m . %d %H:%M:%S"))
					post = bs_post.find("div",{"class":"col-md-12 content_start"}).get_text(" ",strip = True)
					post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
					if bs_post.find("div", {"class": "col-md-12 single_header no_pc"}) is None:
						img = 3
					else:
						img = bs_post.find("div", {"class": "col-md-12 single_header no_pc"}).find("img")["src"]		#게시글의 첫번째 이미지를 가져옴.
						if 1000 <= len(img):
							img = 3
						else:
							if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
								pass
							elif img.startswith("//"):
								img = "http:" + img
							else:
								img = domain + img
					if img != 3:
						if img_size(img):
							pass
						else:
							img = 3	
					post_data['title'] = title.upper()
					post_data['author'] = ""
					post_data['date'] = date
					post_data['post'] = post.lower()
					post_data['img'] = img
					post_data['url'] = url
					print(date, "::::", title)

					if (date < end_date) or (title.upper() == recent_post):
						break
					else:
						post_data_prepare.append(post_data)
				except:
					continue

		now_num = len(posts)
		repeat_num += 1
		if (date <= end_date) or (title.upper() == recent_post):
			break
	if len(post_data_prepare) == 0:
		recent_post = None
	else:
		recent_post = post_data_prepare[0]['title']
	data = (post_data_prepare, recent_post)
	post_driver.close()
	return data

#url을 받으면 url 그대로 반환해준다. => Page number이 필요하지 않는 url
def Change_page(url, page):
	return url


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출
	return domain