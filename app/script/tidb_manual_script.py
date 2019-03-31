#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tidb_manual_script.py
# @Author: lucas
# @Date  : 3/31/19
# @Desc  :

from sqlalchemy import create_engine, Column, DateTime, Index, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, TINYINT
from sqlalchemy.ext.declarative import declarative_base

from pprint import pprint

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('idx_id_deleted', 'id', 'deleted'),
    )

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(500))
    avatar = Column(String(500))
    deleted = Column(TINYINT(1), server_default=text("'0'"))
    created_time = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP"))
    modified_time = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP"))
    deleted_time = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP"))

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


local_tidb_engine = create_engine('mysql+pymysql://root:@127.0.0.1:4000/frodo?charset=utf8')
LocalTiDBSession = sessionmaker(bind=local_tidb_engine)


def query_tidb_user(size=100):
    ti_db_session = LocalTiDBSession()

    users = ti_db_session.query(User). \
        order_by(User.id.desc()). \
        limit(size).all()
    ti_db_session.close()
    return users


def add_user(**user_create_dto):
    print(user_create_dto)

    if not user_create_dto:
        return

    user = User()
    for k, v in user_create_dto.items():
        setattr(user, k, v)

    tidb_session = LocalTiDBSession()
    tidb_session.add(user)

    try:
        tidb_session.commit()
        tidb_session.close()
    except Exception as ex:
        tidb_session.rollback()
        pprint('error:%s' % ex)


def run():
    users = query_tidb_user()
    if not users:
        return

    for user in users:
        pprint(user)

    user = User()
    user.name = u'gandalf'
    user.avatar = u'avatar'
    user.deleted = 0
    add_user(**user.__dict__)


if __name__ == '__main__':
    run()
