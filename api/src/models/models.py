from sqlalchemy import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, String, Integer, Float
from sqlalchemy.orm import relationship

from db.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True, index=True, unique=True)
    cash_balance = Column(Float, nullable=False)
    stocks = relationship('StockTransaction')
    
class StockTransaction(Base):
    __tablename__ = 'stock_transaction'
    id = Column(String, primary_key=True, index=True, unique=True)
    user_id = Column(String, ForeignKey('user.id'))
    symbol = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)