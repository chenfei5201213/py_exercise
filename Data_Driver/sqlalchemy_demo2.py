#-*- coding: utf-8 -*-
# @Time    : 2017/8/21 16:30
# @File    : sqlalchemy_demo2.py
# @Author  : 守望@天空~
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import sessionmaker,relationship,backref
eng = create_engine('mysql+mysqldb://root:admin@localhost/sqlalchemy_demo?charset=utf8')
Base = declarative_base()
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))

car_struct = {'__tablename__':"Cars",
               'Id':Column(Integer, primary_key=True,autoincrement=True),
               "Name":Column(String(length=20)),
                'Price': Column(Integer),
               'AAA':Column(Integer)
               }

Car = type('Car',(Base,),car_struct)
Session = sessionmaker(bind=eng)
ses = Session()
Base.metadata.create_all(eng)
ses.add_all([Car(Name='Audi', Price=52642),
                 Car(Name='Mercedes', Price=57127),
                 Car(Name='Skoda', Price=9000),
                 Car(Name='Volvo', Price=29000),
                 Car(Name='Bentley', Price=350000),
                 Car(Name='Citroen', Price=21000),
                 Car(Name='Hummer', Price=41400),
                 Car(Name='Volkswagen', Price=21600)])
ses.commit()
c1 = Car(**{'Name':u'守望天空', 'Price':52642})
ses.add(c1)
ses.commit()
rs = ses.query(Car).all()
for car in rs:
    print car.Name, car.Price

print ("######")
rs = ses.query(Car).filter(Car.Name.like('%en'))

for car in rs:
    print car.Name, car.Price

print ("######")
rs = ses.query(Car).filter(Car.Id.in_([2, 4, 6, 8]))

for car in rs:
    print car.Id, car.Name, car.Price