from app import db

class TokenBlacklist(db.Model):
    __tablename__ = 'blacklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(40), unique=True)

    @classmethod
    def find_by_jti(cls, jti):
        return cls.query.filter_by(jti=jti).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<TokenBlacklist %r>' % self.jti


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    group = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=True)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User %r>' % self.username

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    raceID = db.Column(db.Integer)
    temp_ground = db.Column(db.Float, nullable=False)
    temp_air = db.Column(db.Float, nullable=False)
    weather_des = db.Column(db.String(120), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    @classmethod
    def find_by_date(cls, datetime):
        return [x for x in cls.query.filter_by(datetime=datetime).all()]

    @classmethod
    def find_by_id(cls, raceID):
        listData = []
        for entry in cls.query.filter_by(raceID=raceID).all():  # .order_by(desc(cls.datetime))
            listData.append({'temp_ground': entry.temp_ground, 'temp_air': entry.temp_air, 'datetime': entry.datetime,
                             'weather_des': entry.weather_des})
        return listData

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class FormelReifendruck(db.Model):
    __tablename__ = 'formelReifendruck'
    id = db.Column(db.Integer, primary_key=True)
    raceID = db.Column(db.Integer,nullable=False)
    air_temp=db.Column(db.Float, nullable=False)
    track_temp=db.Column(db.Float,nullable=False)
    air_pressureFL=db.Column(db.Float,nullable=False)
    air_pressureFR=db.Column(db.Float,nullable=False)
    air_pressureBL=db.Column(db.Float, nullable=False)
    air_pressureBR=db.Column(db.Float, nullable=False)
    variable1=db.Column(db.Float, nullable=False)
    variable2=db.Column(db.Float, nullable=False)
    variable3=db.Column(db.Float, nullable=False)
    variable4=db.Column(db.Float, nullable=False)

    @classmethod
    def get_all(cls,raceID):
        x = cls.query.filter_by(raceID=raceID).first()
        return [{'id': x.id, 'raceID': x.raceID, 'air_temp': x.air_temp,
                 'track_temp': x.track_temp,
                 'air_pressureFL':x.air_pressureFL,'air_pressureFR': x.air_pressureFR,
                 'air_pressureBL':x.air_pressureBL,'air_pressureBR': x.air_pressureBR,
                 'variable1':x.variable1,'variable2':x.variable2,
                 'variable3':x.variable3,'variable4':x.variable4}]
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Timer(db.Model):
    __tablename__ = 'timer'
    id = db.Column(db.Integer, primary_key=True)
    heat_start = db.Column(db.DateTime)
    heat_duration = db.Column(db.Integer)
    order_start = db.Column(db.DateTime)
    order_duration = db.Column(db.Integer)
    raceID = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_all(cls,raceID):
        return [{'heat_start': x.heat_start, 'heat_duration':x.heat_duration,
               'order_start': x.order_start,'order_duration':x.order_duration, 'raceID':x.raceID }
                for x in cls.query.filter_by(raceID=raceID).all()]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Formel(db.Model):
    __tablename__ = 'formel'
    id = db.Column(db.Integer, primary_key=True)
    # raceID = db.Column(db.Integer)
    formel = db.Column(db.String(120), nullable=False)

    @classmethod
    def get_all(cls):
        return [{'n': 'Nr.{} '.format(n), 'formel': x.formel} for n, x in
                enumerate(cls.query)]  # .filter_by(raceID=raceID).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class WheelsStartAstrid(db.Model):
    __tablename__ = 'wheels_start_astrid'
    id = db.Column(db.Integer, primary_key=True)
    raceID = db.Column(db.Integer)
    set = db.Column(db.Integer, nullable=False)
    cat = db.Column(db.String(120), nullable=False)
    subcat = db.Column(db.String(120), nullable=False)
    identifier = db.Column(db.String(120), nullable=False)
    numberOfSets = db.Column(db.String(120), nullable=False)

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_raceID(cls, raceID):
        return [{'id': x.id, 'set': x.set, 'cat': x.cat, 'subcat': x.subcat, 'identifier': x.identifier,
                 'numberOfSets': x.numberOfSets, 'raceID': x.raceID} for x in cls.query.filter_by(raceID=raceID).all()]

    @classmethod
    def find_set_by_id(cls, raceID, set):
        return cls.query.filter_by(raceID=raceID, set=set).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



class Race_Details(db.Model):
    __tablename__ = 'race_details'
    place = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_id(cls, id):
        return [{'place': x.place, 'date': x.date, 'type': x.type} for x in cls.query.filter_by(id=id).all()]

    @classmethod
    def get_all_races(cls):
        return [{'name': 'Rennen_{}'.format(x.date), 'id': x.id} for x in cls.query]

    @classmethod
    def find_by_date(cls, date):
        return [x for x in cls.query.filter_by(date=date).all()]

    @classmethod
    def find_id_by_date(cls, date):
        item = cls.query.filter_by(date=date).first()
        return item.id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


###################Reifenmanagement################################################
class Wheel(db.Model):
    tablename = 'wheel'
    id = db.Column(db.Integer, primary_key=True)
    air_press = db.Column(db.Float)
    hot_air_press = db.Column(db.Float)
    bleed_press =db.Column(db.Float)
    id_scan = db.Column(db.String(120))

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_id(cls, id):
        object = cls.query.filter_by(id=id).first()
        return [{'id': object.id, 'air_press': object.air_press, 'id_scan': object.id_scan}]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Wheels(db.Model):
    __tablename__ = 'wheels'
    id = db.Column(db.Integer, primary_key=True)
    FL = db.Column(db.Integer, db.ForeignKey('wheel.id'))
    FR = db.Column(db.Integer, db.ForeignKey('wheel.id'))
    BL = db.Column(db.Integer, db.ForeignKey('wheel.id'))
    BR = db.Column(db.Integer, db.ForeignKey('wheel.id'))

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_by_id(cls, id):
        x = cls.query.filter_by(id=id).first()
        return [{'id': x.id, 'FL': x.FL, 'FR': x.FR, 'BL': x.BL, 'BR': x.BR}]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class WheelSet(db.Model):
    __tablename__ = 'wheels_set_single'
    id = db.Column(db.Integer, primary_key=True)
    raceID = db.Column(db.Integer)
    setNr = db.Column(db.Integer, nullable=False)
    cat = db.Column(db.String(120), nullable=False)
    subcat = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120))  # 0 or 1
    variant = db.Column(db.String)
    wheels = db.Column(db.Integer, db.ForeignKey('wheels.id'))
    temp_air = db.Column(db.Float)
    temp_heat = db.Column(db.Float)
    bleed_initial = db.Column(db.Float)
    bleed_hot = db.Column(db.Float)
    heat_start = db.Column(db.DateTime)
    heat_duration = db.Column(db.Integer)
    order_start = db.Column(db.DateTime)
    order_duration = db.Column(db.Integer)
    order_end = db.Column(db.DateTime)
    description = db.Column(db.String)
    heat_press_front = db.Column(db.Float)
    heat_press_back = db.Column(db.Float)
    heat_press_timestamp = db.Column(db.DateTime)
    gebleeded = db.Column(db.String)
    runtime = db.Column(db.String)

    @classmethod
    def get(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def getAllRaceID(cls,raceID):
        return [x.id for x in cls.query.filter_by(raceID=raceID).order_by(cls.status,cls.order_start,cls.cat,cls.subcat).all()]

    @classmethod
    def find_by_raceID_cat_setNr(cls, raceID, cat, setNr):
        object = cls.query.filter_by(raceID=raceID, cat=cat, setNr=setNr).first()
        return [{'id': object.id, 'status': object.status}]

    @classmethod
    def find_by_id(cls, id):
        x = cls.query.filter_by(id=id).first()
        return [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels, 'temp_air': x.temp_air, 'variant': x.variant,
                 'order_start': x.order_start, 'order_duration': x.order_duration,
                 'order_end': x.order_end}]

    @classmethod
    def find_status_raceID(cls, raceID):
        return [{'free': [x.id for x in cls.query.filter_by(raceID=raceID).all() if x.status == 'free'],
                 'used': [x.id for x in cls.query.filter_by(raceID=raceID).all() if x.status == 'used']}]

    @classmethod
    def find_by_raceID_cat_subcat(cls, raceID, cat, subcat):
        list_objects = []
        for x in cls.query.filter_by(raceID=raceID, cat=cat, subcat=subcat).all():
            list_objects.append({'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                                 'status': x.status, 'wheels': x.wheels, 'temp_air': x.temp_air, 'variant': x.variant,
                                 'order_start': x.order_start, 'order_duration': x.order_duration,
                                 'order_end': x.order_end})
        return list_objects

    @classmethod
    def find_by_raceID_cat_subcat_status(cls, raceID, cat, subcat, status):
        list_objects = []
        for x in cls.query.filter_by(raceID=raceID, cat=cat, subcat=subcat, status=status).all():
            list_objects.append({'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                                 'status': x.status, 'wheels': x.wheels})
        return list_objects

    @classmethod
    def get_dropdownlist(cls, raceID):
        list_free = [{'name': 'SetNr.{}_{}_{}'.format(x.setNr, x.cat, x.subcat), 'id': x.id}
                     for x in cls.query.filter_by(raceID=raceID).all()]
        list_used = [{'name': 'SetNr.{}_{}_{}'.format(x.setNr, x.cat, x.subcat), 'id': x.id}
                     for x in cls.query.filter_by(raceID=raceID, status='used').all()]
        list_order = [{'name': 'SetNr.{}_{}_{}'.format(x.setNr, x.cat, x.subcat), 'id': x.id}
                      for x in cls.query.filter_by(raceID=raceID, status='order').all()]
        list_astrid = [{'name': 'SetNr.{}_{}_{}_{}'.format(x.description,x.order_start, x.cat, x.subcat), 'id': x.id}
                      for x in cls.query.filter_by(raceID=raceID).all() if x.status != 'free']
        return [list_free, list_order, list_used, list_astrid]


    @classmethod
    def get_wheel_order_dict(cls, raceID):
        cat1 = [x.id for x in cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Cold').all()]
        cat2 = [x.id for x in cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Medium').all()]
        cat3 = [x.id for x in cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Hot').all()]
        cat4 = [x.id for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Inters', subcat='Intermediate').all()]
        cat5 = [x.id for x in cls.query.filter_by(raceID=raceID, status='free', cat='Rain', subcat='DryWet').all()]
        cat6 = [x.id for x in cls.query.filter_by(raceID=raceID, status='free', cat='Rain', subcat='HeavyWet').all()]
        return [[len(cat1), cat1], [len(cat2), cat2], [len(cat3), cat3], [len(cat4), cat4], [len(cat5), cat5],
                [len(cat6), cat6]]

    @classmethod
    def get_wheel_order_dropdown(cls, raceID):
        cat1 = [
            [{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Cold').order_by(cls.status,cls.setNr).all()],
            [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
            for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Cold', status='free').order_by(cls.status, cls.setNr).all()],
            [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
             for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Cold', status='order').order_by(cls.status, cls.setNr).all() ],
            [{'label': 'SetNr.{}_{}_{}'.format(x.setNr, x.status, x.order_start), 'value': x.id}
             for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Cold', status='used').order_by(cls.status,cls.setNr).all()]
        ]
        cat2 = [[{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID,  cat='Slicks', subcat='Medium').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Medium', status ='free').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Medium',status='order').order_by(cls.status,
                                                                                                     cls.setNr).all()],
                [{'label': 'SetNr.{}_{}_{}'.format(x.setNr, x.status, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Medium', status='used').order_by(cls.status,
                                                                                                     cls.setNr).all()]
                ]
        cat3 = [[{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Hot').order_by(cls.status,cls.setNr).order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Hot',status='free').order_by(cls.status,cls.setNr).order_by(
                    cls.status, cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Hot', status='order').order_by(cls.status,cls.setNr).order_by(
                    cls.status, cls.setNr).all()],
                [{'label': 'SetNr.{}_{}_{}'.format(x.setNr, x.status, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Slicks', subcat='Hot',status='used').order_by(cls.status,cls.setNr).order_by(
                    cls.status, cls.setNr).all()]
                ]
        cat4 = [[{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID, cat='Inters', subcat='Intermediate').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Inters', subcat='Intermediate',status='free').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.order_start), 'value': x.id}
                 for x in
                 cls.query.filter_by(raceID=raceID, cat='Inters', subcat='Intermediate', status='order').order_by(
                     cls.status, cls.setNr).all()],
                [{'label': 'SetNr.{}_{}_{}'.format(x.setNr, x.status, x.order_start), 'value': x.id}
                 for x in
                 cls.query.filter_by(raceID=raceID, cat='Inters', subcat='Intermediate', status='used').order_by(
                     cls.status, cls.setNr).all()],
                ]

        cat5 = [[{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID,cat='Rain', subcat='DryWet').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Rain', subcat='DryWet',status='free').order_by(cls.status, cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.order_start), 'value': x.id}
                 for x in
                 cls.query.filter_by(raceID=raceID, cat='Rain', subcat='DryWet', status='order').order_by(cls.status,
                                                                                                          cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in
                 cls.query.filter_by(raceID=raceID, cat='Rain', subcat='DryWet', status='used').order_by(cls.status,
                                                                                                          cls.setNr).all()],
                ]
        cat6 = [[{'label': 'SetNr.{}_{}_{}'.format(x.setNr,x.status,x.order_start) ,'value':x.id }
                for x in cls.query.filter_by(raceID=raceID, cat='Rain', subcat='HeavyWet').order_by(cls.status,cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.status), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Rain', subcat='HeavyWet',status='free').order_by(cls.status,
                                                                                                     cls.setNr).all()],
                [{'label': 'SetNr.{}_{}'.format(x.setNr, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Rain', subcat='HeavyWet',status='order').order_by(cls.status,
                                                                                                     cls.setNr).all()],
                [{'label': 'SetNr.{}_{}_{}'.format(x.setNr, x.status, x.order_start), 'value': x.id}
                 for x in cls.query.filter_by(raceID=raceID, cat='Rain', subcat='HeavyWet', status='used').order_by(cls.status,
                                                                                                     cls.setNr).all()]]
        return [ cat1,  cat2, cat3, cat4, cat5, cat6]

    @classmethod
    def get_wheel_order_dict_old(cls, raceID):
        cat1 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Cold').all()]
        cat2 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Medium').all()]
        cat3 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Slicks', subcat='Hot').all()]
        cat4 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Inters', subcat='Intermediate').all()]
        cat5 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Rain', subcat='DryWet').all()]
        cat6 = [{'id': x.id, 'raceID': x.raceID, 'setNR': x.setNr, 'cat': x.cat, 'subcat': x.subcat,
                 'status': x.status, 'wheels': x.wheels} for x in
                cls.query.filter_by(raceID=raceID, status='free', cat='Rain', subcat='HeavyWet').all()]
        return [{"SlicksCold": [len(cat1), cat1], "SlicksMedium": [len(cat2), cat2], "SlicksHot": [len(cat3), cat3],
                 "IntersIntermediate": [len(cat4), cat4], "RainDryWet": [len(cat5), cat5],
                 "RainHeavyWet": [len(cat6), cat6]}]

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class WheelContigent2(db.Model):
    __tablename__ = 'wheels_contigent'
    id = db.Column(db.Integer, primary_key=True)
    raceID = db.Column(db.Integer)
    set = db.Column(db.Integer, nullable=False)
    cat = db.Column(db.String(120), nullable=False)
    subcat = db.Column(db.String(120), nullable=False)
    # status = db.Column(db.String(120), nullable=False) # 0 or 1
    # wheels = db.Column(db.Integer, db.ForeignKey('wheels.id'))
    identifier = db.Column(db.String(120), nullable=False)
    numberOfSets = db.Column(db.String(120), nullable=False)

    @classmethod
    def find_by_raceID_set(cls, raceID, set):
        return [x.id for x in cls.query.filter_by(raceID=raceID, set=set).all()]

    @classmethod
    def find_by_raceID(cls, raceID):
        return [x for x in cls.query.filter_by(raceID=raceID).all()]

    @classmethod
    def find_status_raceID(cls, raceID):
        return [{'free': [x for x in cls.query.filter_by(raceID=raceID).all() if x.status == 1],
                 'used': [x for x in cls.query.filter_by(raceID=raceID).all() if x.status == 0]}]

    @classmethod
    def get_number_set(cls, raceID):
        cats_value = list(set([x.cat for x in cls.query.filter_by(raceID=raceID).all()]))
        dict_cats = {}
        for entry in cats_value:
            dict_cats.update({entry: {}})
            for item in list(set([x.subcat for x in cls.query.filter_by(raceID=raceID, cat=entry).all()])):
                sets = [{'status': x.status, 'wheels': x.wheels, 'id': x.id} for x in
                        cls.query.filter_by(raceID=raceID, cat=entry, subcat=item).all()]
                dict_cats[entry].update({item: [sets, len(sets)]})
        return [dict_cats]

    @classmethod
    def get_wheels_id(cls, id):
        return cls.join(Wheels).join(Wheel).filter(WheelContigent2.id == id).all()
        # return Wheels.join(Wheel).filter(Wheels.id==id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
