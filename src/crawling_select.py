from bs4 import BeautifulSoup
from url_parser import URLparser
from url_parser import URLparser_EUCKR
from url_parser import URLparser_UTF8
from db_manager import db_manager
from db_manager import get_lastly_post
from db_manager import push_lastly_post
from date_cut import date_cut
from error_handler import error_handler
from error_handler import continue_handler
from db_health import is_crawling
import time
import sj25, sj26, sj27, sj28, sj35,\
sj36, sj37, sj39, sj43, sj45, sj46, sj47, sj48, sj49,\
sj50, sj51, sj52, sj53



def Crawling(URL, db):
	driver = None
	info_name = URL['info'].split('_')
	crawling_name = info_name[0]	#게시판 크롤링 선택
	page = 1
	main_url = URL['url']	#게시판 url 추출 : 페이지 바꾸는 데에 사용
	page_url = eval(crawling_name + '.Change_page(main_url, page)')	#현재 페이지 포스트 url 반환
	print("page_url : ", page_url)
	end_date = date_cut(URL['info'])	# end_date 추출
	# if crawling_name in ["sj34"]:		# 동적 게시판 예외
	# 	sj34.everytime_all_board(URL, end_date, db)
	# 	return
	# if crawling_name in ["sj20"]:		# 제외 게시판
	# 	return

	#현재 크롤링하는 게시판 info 출력
	print("Target : ", URL['info'])
	continue_handler(URL['info'], URL, page_url)

	#크롤링 유무판단
	if is_crawling(db, URL['info']) == False:
		return

	while True:
		# if crawling_name in ["sj23", "sj26", "sj27", "sj28", "sj30", "sj44"]:
		if crawling_name in ["sj26", "sj27", "sj28",  "sj49", "sj50", "sj51"]:
			lastly_post = get_lastly_post(URL, db)
		try:
			print("\npage_url :::: ", page_url)	#현재 url 출력
			print("Page : ", page)				#현재 페이지 출력
			#driver_page 생성---------------------------
			driver_page = URLparser(page_url)
			#-------------------------------------------
			#Selenium을 쓰는 경우----------------------------------------------------------------------------------------------
			if crawling_name in ["sj26", "sj27", "sj28", "sj49", "sj50", "sj51", "sj52"]:
				data = eval(crawling_name + '.Parsing_list_url(URL, page_url)')
				driver = data[0]
				post_urls = data[1]
			#Requests를 쓰는 경우----------------------------------------------------------------------------------------------
			else:
				#로그인을 하는 경우-------------------------------------------------------------------------------
				if URL['login'] == 1:
					post_urls = eval(crawling_name + '.Parsing_list_url(URL, page_url)')
				#로그인을 하지않는 경우---------------------------------------------------------------------------
				else:
					if driver_page is None:		#Connect Failed 이면 break
						error_handler("driver_none", URL, page_url, db)
						break
					else:
						#parsing 형태--------------------------------------------------
						# if crawling_name in ['sj10']:
						# 	bs_page = BeautifulSoup(driver_page, 'lxml')
						# else:
						bs_page = BeautifulSoup(driver_page, 'html.parser')
						#--------------------------------------------------------------
					#20대연구소 예외
					if crawling_name == "sj47":
						pageidx = page_url.split('=')[1]
						post_urls = eval(crawling_name + '.Parsing_list_url(URL, bs_page, pageidx)')
					else:		
						post_urls = eval(crawling_name + '.Parsing_list_url(URL, bs_page)')
				#-----------------------------------------------------------------------------------------------
			#-----------------------------------------------------------------------------------------------------------------
			#get_post_data 형식 : [게시글정보dictionary, title, date]-------------------------------------------------------------------------------------------------------
			#date 규격은 "0000-00-00 00:00:00"
			post_data_prepare = []
			for post_url in post_urls:
				#Selenium인 경우--------------------------------------------------------------------------------------------------------------------
				#------------------게시판 규격인 경우
				if crawling_name in ['sj49', 'sj52']:
					try:
						get_post_data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL)')
					except:
						try:
							get_post_data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL)')
						except:
							continue
				# ----------------------------게시판 규격이 아닌 경우
				elif crawling_name in ['sj26', 'sj27', 'sj28', 'sj44', 'sj50', 'sj51']:
					try:
						data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL, lastly_post)')
					except:
						try:
							data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL, lastly_post)')
						except:
							continue
					post_data_prepare = data[0]
					lastly_post = data[1]
					if lastly_post is None:
						pass
					else:
						push_lastly_post(URL, lastly_post, db)
				#Requests인 경우--------------------------------------------------------------------------------------------------------------------
				# elif crawling_name == "sj49":
				# 	get_post_data = eval(crawling_name + '.Parsing_post_data(post_url, URL)')
				else:
					#driver_post 생성--------------------------------
					# if crawling_name in ["sj21", "sj4", "sj5", "sj8", "sj16"]: #---driver_post가 필요없는 경우
					# 	pass
					# elif crawling_name in ['sj10', 'sj33']:
					# 	driver_post = URLparser_EUCKR(post_url)
					# elif crawling_name in ['sj12']:
					# 	driver_post = URLparser_UTF8(post_url)
					# else:
					driver_post = URLparser(post_url)
					#------------------------------------------------
					if driver_post is None:		#Connect Failed 이면 continue
						error_handler("driver_none", URL, page_url, db)
						break
					else:
						#parsing 형태-------------------------------------------
						# if crawling_name in ['sj10']:
						# 	bs_post = BeautifulSoup(driver_post, 'lxml')
						# elif crawling_name in ['sj12']:
						# 	bs_post = driver_post
						# else:
						bs_post = BeautifulSoup(driver_post, 'html.parser')
						#-------------------------------------------------------
					try:
						print("첫번째 시도 : ",post_url)
						get_post_data = eval(crawling_name + '.Parsing_post_data(bs_post, post_url, URL)')
					except:
						try:
							print("내가 문제다 : ",post_url)
							get_post_data = eval(crawling_name + '.Parsing_post_data(bs_post, post_url, URL)')
						except:
							continue
				#-----------------------------------------------------------------------------------------------------------------------------------
				
				#post_data_prepare이 이미 완성된 경우-----------------------------------------------------------------------
				# if crawling_name in ["sj4", "sj5", "sj8", "sj16", "sj23", "sj26", "sj27", "sj28", "sj44"]:
				if crawling_name in ["sj26", "sj27", "sj28", "sj50", "sj51"]:
					pass
				#post_data_prepare이 완성되지 않은 경우---------------------------------------------------------------------
				else:
					if get_post_data == None:	#잘못된 포스트 데이터인 경우
						continue
					title = get_post_data[1]
					date = get_post_data[2]
		
					print(date, "::::", title)	#현재 크롤링한 포스트의 date, title 출력
		
					#게시물의 날짜가 end_date 보다 옛날 글이면 continue, 최신 글이면 append
					if str(date) <= end_date:
						continue
					else:
						post_data_prepare.append(get_post_data[0])
			#----------------------------------------------------------------------------------------------------------
			#--------------------------------------------------------------------------------------------------------------------------------------------------------------
			add_cnt = db_manager(URL, post_data_prepare, db)
			print("add_OK : ", add_cnt)	#DB에 저장된 게시글 수 출력
			
			#dirver 종료 [Selenium 을 사용했을 시]
			if crawling_name in ["sj26", "sj27", "sj28", "sj49", "sj50", "sj51", "sj52"]:
				driver.quit()
			
			#DB에 추가된 게시글이 0 이면 break, 아니면 다음페이지
			if add_cnt == 0:
				break
			# elif crawling_name == "sj49":
			# 	page += 10
			# 	page_url = eval(crawling_name + '.Change_page(main_url, page)')
			else:
				page += 1
				page_url = eval(crawling_name + '.Change_page(main_url, page)')
		# Error handler : 만약 크롤링이 실패했을 경우, 에러를 logging 하고 크롤링을 중단한다.
		except Exception as e:
			error_handler(e, URL, page_url, db)
			break