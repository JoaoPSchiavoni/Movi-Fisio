from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///movifisio.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    name = Column("name", String, nullable=False)
    cpf = Column("cpf", String, unique=True, nullable=False)
    phone = Column("phone", String, nullable=False)
    lgpd_accepted = Column("lgpd_accepted", Boolean, nullable=False)
    is_admin = Column("is_admin", Boolean, nullable=False)
    active = Column("active", Boolean, nullable=False, default=True)

    def __init__(self, email, password, name, cpf, phone, lgpd_accepted=False, is_admin=False, active=True):
        self.email = email
        self.password = password
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.lgpd_accepted = lgpd_accepted
        self.is_admin = is_admin
        self.active = active


class Schedule(Base):
    __tablename__ = 'schedules'
    # STATUS_SCHEDULE = (
    #     ("pending", "Pending"),
    #     ("confirmed", "Confirmed"),
    #     ("cancelled", "Cancelled")
    # )


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    therapist_id = Column("therapist_id", Integer, ForeignKey("users.id"), nullable=False)
    client_id = Column("client_id", Integer, ForeignKey("users.id"), nullable=False)
    date = Column("date", String, nullable=False)
    time = Column("time", String, nullable=False)
    service = Column("service", String, nullable=False)
    price = Column("price", Float, nullable=False)
    is_paid = Column("is_paid", Boolean, nullable=False)
    status = Column("status", String, nullable=False)

    def __init__(
        self, 
        therapist_id, 
        client_id, date, 
        time, service, price, 
        is_paid=False,
        status="pending"
        ):
        self.therapist_id = therapist_id
        self.client_id = client_id
        self.date = date
        self.time = time
        self.service = service
        self.price = price
        self.is_paid = is_paid
        self.status = status


class medical_record(Base):
    __tablename__ = 'medical_records'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    therapist_id = Column("therapist_id", Integer, ForeignKey("users.id"), nullable=False)
    client_id = Column("client_id", Integer, ForeignKey("users.id"), nullable=False)
    date = Column("date", String, nullable=False)
    description = Column("description", String, nullable=False)

    def __init__(self, therapist_id, client_id, date, description):
        self.therapist_id = therapist_id
        self.client_id = client_id
        self.date = date
        self.description = description

    
class service(Base):
    __tablename__ = 'services'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    price = Column("price", Float, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

class appointment_file(Base):
    __tablename__ = 'appointment_files'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50), nullable=False)
    path = Column("path", String(500), nullable=False)
    size = Column("size", Integer, nullable=False)
    medical_record_id = Column("medical_record_id", Integer, ForeignKey("medical_records.id"), nullable=False)

    def __init__(self, name, path, size, medical_record_id):
        self.name = name
        self.path = path
        self.size = size
        self.medical_record_id = medical_record_id

