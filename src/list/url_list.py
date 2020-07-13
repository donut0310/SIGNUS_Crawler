#URL 리스트 모음
#'url' : 게시판url, 별값, 'info' : 게시판정보, 'title_tag' : 검색속도를 빠르게하기 위한 게시판 대표 태그, 'login' : 비로그인에도 볼 수 있으면 0
#																											   로그인 해야만 볼 수 있으면 1

List = (\
	#1
	{'url': "https://www.thinkcontest.com/Contest/CateField.html?s=ing&page=",\
	'info': "sj25_thinkgood_info",\
	'title_tag' : ["씽굿", "공모전&대외활동"], 'login' : 0},\
	#캠퍼스픽 [sj26_campuspick_...]
	#2
	{'url': "https://www.campuspick.com/activity",\
	'info': "sj26_campuspick_activity",\
	'title_tag' : ["캠퍼스픽", "공모전&대외활동"], 'login' : 0},\
	#3
	{'url': "https://www.campuspick.com/contest",\
	'info': "sj26_campuspick_contest",\
	'title_tag' : ["캠퍼스픽", "공모전&대외활동"], 'login' : 0},\
	#캠퍼스픽 스터디 [sj27_campuspick_...]
	#4
	{'url': "https://www.campuspick.com/study/list?category1=1&category2=0",\
	'info': "sj27_campuspick_language",\
	'title_tag' : ["캠퍼스픽", "동아리&모임"], 'login' : 1},\
	#5
	{'url': "https://www.campuspick.com/study/list?category1=2&category2=0",\
	'info': "sj27_campuspick_job",\
	'title_tag' : ["캠퍼스픽", "취업&진로", "동아리&모임"], 'login' : 1},\
	#6
	{'url': "https://www.campuspick.com/study/list?category1=3&category2=0",\
	'info': "sj27_campuspick_certificate",\
	'title_tag' : ["캠퍼스픽", "동아리&모임"], 'login' : 1},\
	#7
	{'url': "https://www.campuspick.com/study/list?category1=4&category2=0",\
	'info': "sj27_campuspick_study",\
	'title_tag' : ["캠퍼스픽", "동아리&모임"], 'login' : 1},\
	#캠퍼스픽 동아리 [sj28_campuspick_club]
	#8
	{'url': "https://www.campuspick.com/club?category=2",\
	'info': "sj28_campuspick_club",\
	'title_tag' : ["캠퍼스픽", "동아리&모임"], 'login' : 0},\
	#9
	#에브리타임 모든 게시판 [sj34_everytime_all]
	{'url': "https://everytime.kr",\
	'info': "sj34_everytime_all",\
	'title_tag' : ["커뮤니티"], 'login' : 1},
	#데티즌 공모전 [sj35_detizen_...]
	#10
	{'url': "http://www.detizen.com/contest/?Category=1&IngYn=Y&PC=",\
	'info': "sj35_detizen_contest",\
	'title_tag' : ["공모전&대외활동"], 'login' : 0},\
	#11
	{'url': "http://www.detizen.com/activity/?Category=3&IngYn=Y&PC=",\
	'info': "sj35_detizen_activity",\
	'title_tag' : ["공모전&대외활동"], 'login' : 0},\
	#잡코리아
	#잡코리아 꿀팁[sj36_jobkoreatip_tip]
	#12
	{'url': "http://www.jobkorea.co.kr/goodjob/Tip?schCtgr=0&TipKwrdArray=알바생&TipKwrdArray=정보&TipKwrdArray=대화&TipKwrdArray=대기업&TipKwrdArray=뉴스&TipKwrdArray=상식퀴즈&TipKwrdArray=면접&TipKwrdArray=직장인&TipKwrdArray=연봉&TipKwrdArray=취준생&Page=",\
	'info': "sj36_jobkoreatip_tip",\
	'title_tag' : ["취업&진로"], 'login' : 0},\
	#잡코리아 [sj37_jobkorea_...]
	#13
	{'url': "http://www.jobkorea.co.kr/starter/?&schWork=2&isSaved=1&LinkGubun=0&Page=",\
	'info': "sj37_jobkorea_job",\
	'title_tag' : ["취업&진로"], 'login' : 0},\
	#14
	{'url': "http://www.jobkorea.co.kr/Starter/?&LinkGubun=0&Page=",\
	'info': "sj37_jobkorea_public",\
	'title_tag' : ["취업&진로"], 'login' : 0},\
	#15
	{'url': "http://rndjob.or.kr/yard/notice.asp?&cur_pack=0&sfield=&gtxt=&gbn=A01&page=",\
	'info': "sj39_rndjob_job",\
	'title_tag' : ["취업&진로"], 'login' : 0},\
	#인디드 [sj43_indeed_job]
	#16
	{'url': "https://kr.indeed.com/jobs?q=&l=서울&start=",\
	'info': "sj43_indeed_job",\
	'title_tag' : ["취업&진로"], 'login' : 0},\
	# 17 무중력지대
	{'url': "http://youthzone.kr/program_applies?page=",\
	'info': "sj45_infor_notice",\
	'title_tag' : ["모집"], 'login' : 0},\
	# 18
	{'url': "http://youthzone.kr/external_programs?page=",\
	'info': "sj45_external_notice",\
	'title_tag' : ["모집"], 'login' : 0},\
	# 19
	{'url': "http://youthzone.kr/reviews?page=",\
	'info': "sj45_review_data",\
	'title_tag' : ["모집"], 'login' : 0},\
	# 20 애드캠퍼스
	{'url': "https://addcampus.com/community/board/1?page=1&search_txt=",\
	'info': "sj46_addcampus_board",\
	'title_tag' : ["커뮤니티"], 'login' : 0},\
	# 21 20대연구소
	{'url': "https://www.20slab.org/SNSColumn?pageidx=",\
	'info': "sj47_20lab_column",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 22
	{'url': "https://www.20slab.org/Infographics?pageidx=",\
	'info': "sj47_20lab_infographics",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 23
	{'url': "https://www.20slab.org/Press?pageidx=",\
	'info': "sj47_20lab_announcement",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 24
	{'url': "https://www.20slab.org/Data?pageidx=",\
	'info': "sj47_20lab_data",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 25
	{'url': "https://www.20slab.org/Report?pageidx=",\
	'info': "sj47_20lab_report",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 26 VMS
	{'url': "https://www.vms.or.kr/partspace/recruit.do?area=&areagugun=&acttype=&status=1&termgbn=&page=",\
	'info': "sj48_vms_volunteer",\
	'title_tag' : ["봉사"], 'login' : 0},\
	# 27 Naver news 대학교
	{'url': "https://search.naver.com/search.naver?&where=news&query=%EB%8C%80%ED%95%99%EA%B5%90&start=",\
	'info': "sj49_naver_news",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 28 캠퍼스픽 커뮤니티 - 알바
	{'url': "https://www.campuspick.com/community?id=3098",\
	'info': "sj50_campuspick_parttime",\
	'title_tag' : ["알바&구인"], 'login' : 0},\
	# 29 대학내일
	{'url': "https://univ20.com/",\
	'info': "sj51_univ20_main",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 30 온라인 청년센터
	{'url': "https://www.youthcenter.go.kr/board/boardList.do?bbsNo=3&ntceStno=&pageUrl=board%2Fboard&orderBy=REG_DTM&orderMode=DESC&pageIndex=",\
	'info': "sj52_youthcenter_info",\
	'title_tag' : ["소식"], 'login' : 0},\
	# 31 한국 장학재단 공지사항
	{'url': "https://www.kosaf.go.kr/ko/notice.do?&page=",\
	'info': "sj53_kosaf_info",\
	'title_tag' : ["소식"], 'login' : 0},\
	)