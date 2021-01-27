from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class MC_DESC(Base):
    __tablename__ = "MC_DESC"

    SEQ = Column(Integer, primary_key=True)
    MC_COMM_NAME = Column(String)
    OS = Column(String)
    DESC = Column(String)
    YARA_FILE_PATH = Column(String)
    REF = Column(String)
    USE_YN = Column(String)

    def __init__(self, _name, _os, _desc, _path, _ref):
        self.SEQ = None
        self.MC_COMM_NAME = _name
        self.OS = _os
        self.DESC = _desc
        self.YARA_FILE_PATH = _path
        self.REF = _ref
        self.USE_YN = 0

class MC_DESC_SEARCH_KWRD(Base):
    __tablename__ = "MC_DESC_SEARCH_KWRD"

    SEQ = Column(Integer, primary_key=True)
    MC_DESC_SEQ = Column(Integer)
    SEARCH_KWRD = Column(String)
    SEARCH_TYPE = (Integer)

    def __init__(self, _desc_seq, _search_kwrd):
        self.SEQ = None
        self.MC_DESC_SEQ = _desc_seq
        self.SEARCH_KWRD = _search_kwrd
        self.SEARCH_TYPE = 0


