from datetime import datetime, timedelta
from pymongo import MongoClient

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_minus = datetime.now() + timedelta(days = -1)
now_minus = now_minus.strftime("%Y-%m-%d %H:%M:%S")


date_cut_dict = {}

date_cut_dict_before = {
	#마감날짜 기준이므로 항상 현재까지만 긁는다.
	"sj25": now,\
	"sj26": now_minus,\
	"sj27": "2009-01-01 00:00:00",\
	"sj28": now_minus,\
	"sj34": "2009-01-01 00:00:00",\
	"sj35": now,\
	"sj36": "2009-01-01 00:00:00",\
	"sj37": now,\
	"sj39": "2009-01-01 00:00:00",\
	"sj43": "2009-01-01 00:00:00",\
	"sj45": "2009-01-01 00:00:00",\
	"sj46": "2009-01-01 00:00:00",\
	"sj47": "2009-01-01 00:00:00",\
	"sj48": "2009-01-01 00:00:00",\
	"sj49": "2009-01-01 00:00:00",\
	"sj50": "2009-01-01 00:00:00",\
	"sj51": "2009-01-01 00:00:00",\
	"sj52": "2009-01-01 00:00:00",\
	"sj53": "2009-01-01 00:00:00"\
}

def date_init(db):
	date_db = db.date.find()
	for date_one in date_db:
		date_cut_dict[date_one['crawler']] = date_one['date_exp']



def date_cut(info):
	if info.split("_")[2].find("FAQ") != -1:		#FAQ이므로 전체긁기를 위해 예외처리
		end_date = date_cut_dict['sj1_main_FAQ']
	else:
		name = info.split("_")[0]
		end_date = date_cut_dict[name]

	return end_date