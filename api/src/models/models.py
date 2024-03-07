from sqlalchemy import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, String, Number
from sqlalchemy.orm import relationship

from db.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True, index=True, unique=True)
    cash_balance = Column(Number, nullable=False)
    # stocks = one to many relationship
    stocks = relationship('StockBuy')
    
class StockBuy(Base):
    __tablename__ = 'stock_buy'
    id = Column(String, primary_key=True, index=True, unique=True)
    user_id = Column(String, ForeignKey('user.id'))
    symbol = Column(String, nullable=False)
    amount = Column(Number, nullable=False)