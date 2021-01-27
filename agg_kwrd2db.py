#-*-coding:utf8-*-
import json
import urllib2
from malpedia import myDB
from DBModels import MC_DESC_SEARCH_KWRD

class aggKwrd:
    MAX_SIZE = 10000

    def __init__(self):
        self.mydb = myDB()

    def __getAV(self):
        query = {
            "query":{
                "match":{
                    "data_type":"URL"
                }
            },"size":0,
            "aggs":{
                "g":{
                    "terms":{
                        "field":"av", "size":aggKwrd.MAX_SIZE
                    }
                }
            }
        }

        _header = {
            "content-type":"application/json"
        }
        try:
            req = urllib2.Request("http://10.250.252.103:9200/hacking_url_c2_*/_search", json.dumps(query), _header)
            res = urllib2.urlopen(req)
            return res.read()
        except Exception as ex:
            print ex
            return False

    def __insertKwrd(self, _kwrd):
        tmp_search_kwrd = MC_DESC_SEARCH_KWRD(0, _kwrd)
        self.mydb.session.add(tmp_search_kwrd)
        self.mydb.session.commit()

    def run(self):
        result = self.__getAV()
        if result is not False:
            loaded_result = json.loads(result)
            for bkt in loaded_result["aggregations"]["g"]["buckets"]:
                self.__insertKwrd (bkt["key"])

    def __del__(self):
        self.mydb.engine.dispose()

def main():
    aggKwrd().run()

if __name__ == "__main__":
    main()