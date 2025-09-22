from app.db_api.db_gino import TimedBaseModel

from sqlalchemy import Column, BigInteger, String, sql

class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(20), primary_key=True)
    update_name = Column(String(30), primary_key=True)

    #query: sql.select
