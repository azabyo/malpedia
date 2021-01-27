#-*-coding:utf8-*-
import os
import urllib2
import pickle
import argparse
from pyquery import PyQuery as pq
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from DBModels import MC_DESC, MC_DESC_SEARCH_KWRD


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
YARA_DIR = os.path.join(ROOT_DIR, "yara_rules")

class myDB:
    NO_DESC = "There is no description at this point."
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:dldnwo1004@10.250.252.103/hacking_url_c2?charset=utf8', convert_unicode=True, echo=True)
        self.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))

    def insert_mc_desc(self, _obj):
        if _obj.desc == self.NO_DESC:
            tmp_desc = None
        else:
            tmp_desc = _obj.desc
        if len(_obj.reference) == 0:
            tmp_ref = None
        else:
            tmp_ref = ",".join(_obj.reference)

        tmp_dbdesc = MC_DESC(_obj.name ,_obj.os, tmp_desc, _obj.yararules_filepath, tmp_ref)
        self.session.add(tmp_dbdesc)
        # self.session.refresh(tmp_dbdesc)
        self.session.commit()
        # print tmp_dbdesc.SEQ
        # exit()
        tmp_search_kwrd = MC_DESC_SEARCH_KWRD(tmp_dbdesc.SEQ, _obj.name.lower())
        self.session.add(tmp_search_kwrd)
        self.session.commit()

class MalpediaManage:
    MALPEDIA_BASE_URL = u"https://malpedia.caad.fkie.fraunhofer.de"
    MALPEDIA_URL = MALPEDIA_BASE_URL + "/families"
    RESULT_DATA_FILE = os.path.join(ROOT_DIR, "result.data")

    def __init__(self, _read_data):
        self.read_data = _read_data
        self.malpedia_objs = list()
        if not os.path.exists(YARA_DIR):
            os.makedirs(YARA_DIR)
        self.my_csv = None
    
    def getDetailURL(self):
        try:
            response = urllib2.urlopen(MalpediaManage.MALPEDIA_URL).read()
            return self.__getLink(response)
        except Exception as ex:
            print "getDetailURL {}".format(ex)
            return []
        
    def __getLink(self, _response):
        a_link_list = list()
        pq_response = pq(_response)
        for tr in pq_response("tbody.list tr"):
            a_link_list.append(MalpediaManage.MALPEDIA_BASE_URL + pq(tr).attr["data-href"])
        return a_link_list

    def getDetail(self, _detail_url):
        malpedia = Malpedia()
        malpedia.getPage(_detail_url)
        self.malpedia_objs.append(malpedia)

    def __saveResult(self):
        try:
            with open(MalpediaManage.RESULT_DATA_FILE, "wb") as f:
                pickle.dump(self.malpedia_objs, f)
        except Exception as ex:
            print "Failed Save Result Data"

    def __del__(self):
        if self.my_csv is not None:
            self.my_csv.close()

    def run(self):
        if self.read_data:
            self.my_csv = open("output.csv", "wb")
            wr = csv.writer(self.my_csv)
            wr.writerow(["NAME", "OS", "DESC", "YARA_FILE", "REFERENCE"])
            if not os.path.exists(MalpediaManage.RESULT_DATA_FILE):
                print "Not Found Result Data File"
            else:
                # TODO : how to save to db
                try:
                    with open(MalpediaManage.RESULT_DATA_FILE, "rb") as f:
                        data = pickle.load(f)
                    mydb = myDB()
                    for _d in data:
                        print _d
                        mydb.insert_mc_desc(_d)
                except Exception as ex:
                    print "Exception Result Data File Read. {}".format(ex)
                    exit()
                # for d in data:
                #     # print "name : {}".format(d.name)
                #     # print "os : {}".format(d.os)
                #     print "desc : {}".format(d.desc.encode('utf-8'))
                #     # print "yara : {}".format(d.yararules_filepath)
                #     # print "reference : {}".format(d.reference)
                #     wr.writerow([d.name, d.os, d.desc.encode('utf-8'), d.yararules_filepath, ",".join(d.reference)])

                    # exit()

        else:
            for _d_url in self.getDetailURL():
                self.getDetail(_d_url)
            self.__saveResult()

class Malpedia:
    def __init__(self):
        self.os = None
        self.name = None
        self.desc = None
        self.reference = list()
        self.yararules_filepath = None

    def __saveYararules(self, _yara_url):
        try:
            response = urllib2.urlopen(_yara_url)
            savefile = os.path.join(YARA_DIR, self.name+".zip")
            with open(savefile, "wb") as f:
                f.write(response.read())
            self.yararules_filepath = savefile
            return True
        except Exception as ex:
            print "__saveYararules {}".format(ex)
            return False

    def __pageParse(self, response):
        pq_response = pq(response)
        h2 = pq_response('h2')
        self.os = pq(pq(pq(h2)).find('i')).attr["title"]
        pq(pq(h2).find('button')).remove()
        self.name = pq(h2).text()
        tmp_desc = pq(pq(pq(pq_response).find("hr:eq(1)")).next("p")).text()
        if len(tmp_desc) > 0:
            self.desc = tmp_desc
        else:
            self.desc = pq(pq(pq(pq_response).find("hr:eq(1)")).next("p")).next("p").text()
        self.reference = [pq(x).text() for x in pq(pq_response).find('.ellipsis')]
        yara_down_btn = pq(pq_response).find('a.btn-secondary')

        if len(yara_down_btn) > 0:
            yara_down_url = MalpediaManage.MALPEDIA_BASE_URL + pq(yara_down_btn).attr["href"]
            if self.__saveYararules(yara_down_url):
                print "YARA File Save OK"
            else:
                print "Failed Save YARA  file"
        else:
            print "not found Yara files : {}".format(self.name)



    def getPage(self, _detail_url):
        try:
            detail_response = urllib2.urlopen(_detail_url).read()
        except Exception as ex:
            print "getPage {} {}".format(_detail_url, ex)
            exit()
        self.__pageParse(detail_response)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--read-data", dest="read_data", action="store_true", default=False)
    args = parser.parse_args()
    MalpediaManage(args.read_data).run()


if __name__ == "__main__":
    main()