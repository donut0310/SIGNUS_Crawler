from tagname_list import tag_names
from tagname_list import List


#태그 문자열들을 리스트화 시키기
def tag_listing(tag_list):
	tag_done = []
	for tag in tag_list:
		tag_done.append(tag)
	return tag_done

#태그 리스트들을 "태그1/태그2/태그3/.../" 이런 형식으로 만들어주는 함수
def tag_attach(tag_list):
	tag_list_len = len(tag_list)
	tag_done = ''
	for num in range(tag_list_len):
		tag_done = tag_done + tag_list[num] + "/"
	#몽고디비용 태그 리스트화
	tag_done = tag_listing(tag_list)
	return tag_done


#tag_list 에서 중복값 제거해주기
def set_tag(tag_list):
	tag_list = list(set(tag_list))
	return tag_list


#title에서 비교받을 문자 앞뒤 1칸씩 비교하여, 영어문장인지 아닌지 검사하는 함수
def real_word(text, word):
	strlen = int(len(word))
	text = text + " "
	word_num = int(text.find(word))
	alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ck = 0
	if word_num == 0:
		title = text[0:strlen+1]
	else:
		title = text[word_num-1:word_num+strlen+1]

	for i in title:
		if i in alp:
			ck += 1
	return ck


#tagging 메인 함수
def tagging(URL, title):
	tag_list = []
	info = URL['info'].split('_')
	#title_tag = URL['title_tag'].split("/")
	title_tag = URL['title_tag']
	#소문자를 전부 대문자화 시켜준다
	title = title.upper()

	# 데티즌 공모전 + 잡코리아
	elif info[0] in ["sj35", "sj36", "sj37", "sj39", "sj43"]:
		tag_udream(info, title, tag_list, title_tag)
	#씽굿
	elif info[0] == 'sj25':
		tag_thinkgood_info(info, title, tag_list, title_tag)
	#캠퍼스픽
	elif info[0] in ["sj26", "sj28", "sj50"]:
		tag_campuspick(info, title, tag_list, title_tag)
	#캠퍼스픽 스터디
	elif info[0] == 'sj27':
		tag_campuspick_study(info, title, tag_list, title_tag)
	#에브리타임
	elif info[0] == 'sj34':
		tag_everytime(info, title, tag_list ,title_tag)
	#무중력지대
	elif info[0] == 'sj45':
		tag_zero_gravity(info, title, tag_list ,title_tag)			
	#애드캠퍼스	
	elif info[0] == 'sj46':
		tag_addCampus(info, title, tag_list ,title_tag)
	#애드캠퍼스	
	elif info[0] == 'sj47':
		tag_20slab(info, title, tag_list ,title_tag)
	#VMS	
	elif info[0] == 'sj48':
		tag_vms(info, title, tag_list ,title_tag)
	#네이버 뉴스 '대학교'
	elif info[0] == 'sj49':
		tag_naver_news(info, title, tag_list ,title_tag)
	#대학내일'
	elif info[0] == 'sj51':
		tag_univ20(info, title, tag_list ,title_tag)
	#온라인 청년센터
	elif info[0] == 'sj52':
		tag_youthcenter(info, title, tag_list ,title_tag)
	#한국 장학재단
	elif info[0] == 'sj53':
		tag_kosaf(info, title, tag_list ,title_tag)

	#태그들을 하나의 문자열로 만든 string 반환
	#tag_list = set_tag(tag_list)
	#tag_done = tag_attach(tag_list)
	tag_done = set_tag(tag_list)
	return tag_done

#무중력 지대
def tag_zero_gravity(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#애드 캠퍼스
def tag_addCampus(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#20대 연구소
def tag_20slab(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#20대 연구소
def tag_vms(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#네이버 뉴스 '대학교'
def tag_naver_news(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#대학 내일
def tag_univ20(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#온라인 청년 센터
def tag_youthcenter(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)
	
#한국 장학재단
def tag_kosaf(info, title, tag_list, title_tag):
	title = title.upper()
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)	
	tagging_public(title, tag_list)

#세종대 메인사이트 tagging 함수
def tag_main(info, title, tag_list, title_tag):
	title = title.upper() # 모든 title 은 대문자로 만들어준다.
	
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	#공지사항을 만들기위해서 중요태그를 달아준다
	if info[2] == 'student':
		if title.find("신청") != -1 or title.find("안내") != -1 or title.find("공지") != -1:
			tag_list.append("중요")

	if title.find("입학") != -1:
		tag_list.append("입학")
	
	tagging_public(title, tag_list)

#세종대 에브리타임 tagging 함수
def tag_everytime(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)

#씽굿 tagging 함수
def tag_thinkgood_info(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)

#캠퍼스픽 tagging 함수
def tag_campuspick(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)

#캠퍼스픽 스터디 tagging 함수
def tag_campuspick_study(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)

	if "알바&구인" in tag_list:
		tag_list.remove("알바&구인")






#tagging 공통 함수
def tagging_public(title, tag_list):

	for tag_name in tag_names:
		words = List[tag_name][1].split("/")

		if any((word in title) and (tag_check(title, word)) for word in words):
			tag_list.append(List[tag_name][0])

#예외처리
def tag_check(title, tag):
	if tag == 'IT':
		if real_word(title, tag)== 2 and title.find("IT IS") == -1 and title.find("DO IT") == -1: return True
		else: return False
	elif tag == 'SW':
		if real_word(title, tag)==2: return True
		else: return False
	elif tag == 'DBA':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'AI':
		if real_word(title, tag)==2: return True
		else: return False
	elif tag == 'SE':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'IOS':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'API':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'UX':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'UI':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'VR':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == '학식':
		if title.find("입학식") != -1: return False
		else: return True
	elif tag == '로펌':
		if title.find("윌로펌프") != -1: return False
		else: return True
	elif tag == '정규직':
		if title.find("비정규직") != -1: return False
		else: return True
	elif tag == '카페':
		if title.find("네이버 카페") != -1 or title.find("네이버카페") != -1 or title.find("다음 카페") != -1 or title.find("다음카페") != -1 or title.find("인터넷 카페") != -1 or title.find("인터넷카페")\
		 or title.find("NAVER 카페") != -1 or title.find("DAUM 카페") != -1:
			return False
		else: return True
	elif tag == '학사':
		if title.find("대학사") != -1: return False
		else: return True
	elif tag == '국제':
		if title.find("자유학기") != -1: return False
		else: return True
	elif tag == '스포츠':
		if title.find("1운동") != -1: return False
		elif title.find("18운동") != -1: return False
		elif title.find("화운동") != -1: return False
		elif title.find("화 운동") != -1: return False
		else: return True
	elif tag == '학사':
		if title.find("학사상") != -1 or title.find("학사고") != -1:
			return False
	else: return True