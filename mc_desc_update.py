from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from DBModels import MC_DESC, MC_DESC_SEARCH_KWRD

MINER=228

with open("mc_desc_update.txt", "r") as f:
    av_list = f.readlines()

engine = create_engine('mysql+pymysql://root:dldnwo1004@10.250.252.103/hacking_url_c2?charset=utf8', convert_unicode=True, echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

for av in av_list:
    print av.rstrip()
    continue

    q = session.query(MC_DESC_SEARCH_KWRD)
    q = q.filter(MC_DESC_SEARCH_KWRD.SEARCH_KWRD == av.rstrip())
    print q
    try:
        record = q.one()
        record.MC_DESC_SEQ = 228
    except Exception as ex:
        print ex
        continue

session.close()

