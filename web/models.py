from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Loc(db.Model):
    __tablename__ = 'loc'
    locid = db.Column(db.Integer, primary_key=True)
    locname = db.Column(db.String)
    locregname = db.Column(db.String)
    locareaname = db.Column(db.String)
    loctername = db.Column(db.String)

    unique_constraint = db.UniqueConstraint('locname', 'locregname', 'loctername')

    educate_organisations = db.relationship('EducateOrganisation', back_populates='loc')


class EducateOrganisation(db.Model):
    __tablename__ = 'educate_organisation'
    eoid = db.Column(db.Integer, primary_key=True)
    eoname = db.Column(db.String)
    eoregname = db.Column(db.String)
    eoareaname = db.Column(db.String)
    eotername = db.Column(db.String)
    eoparent = db.Column(db.String)
    eotypename = db.Column(db.String)
    locid = db.Column(db.Integer, db.ForeignKey('loc.locid'))

    unique_constraint = db.UniqueConstraint('eoname', 'eotypename', 'eoparent')

    loc = db.relationship('Loc', back_populates='educate_organisations')


class Participants(db.Model):
    __tablename__ = 'participants'
    outid = db.Column(db.String, primary_key=True)
    birth = db.Column(db.Numeric)
    sextypename = db.Column(db.String)
    regtypename = db.Column(db.String)
    classprofilename = db.Column(db.String)
    classlangname = db.Column(db.String)
    regname = db.Column(db.String)
    areaname = db.Column(db.String)
    tername = db.Column(db.String)
    tertypename = db.Column(db.String)
    zno_year = db.Column(db.Integer)
    locid = db.Column(db.Integer, db.ForeignKey('loc.locid'))

    loc = db.relationship('Loc', back_populates='participants')


class Test(db.Model):
    __tablename__ = 'test'
    testid = db.Column(db.Integer, primary_key=True)
    outid = db.Column(db.String, db.ForeignKey('participants.outid'))
    test = db.Column(db.String)
    testlang = db.Column(db.String)
    teststatus = db.Column(db.String)
    ball100 = db.Column(db.Numeric)
    ball12 = db.Column(db.Numeric)
    ball = db.Column(db.Numeric)
    adaptscale = db.Column(db.Numeric)
    dpalevel = db.Column(db.String)
    locid = db.Column(db.Integer, db.ForeignKey('loc.locid'))

    loc = db.relationship('Loc', back_populates='tests')
    participant = db.relationship('Participants', back_populates='tests')


class ParticipantsEO(db.Model):
    __tablename__ = 'participants_eo'
    outid = db.Column(db.String, db.ForeignKey('participants.outid'), primary_key=True)
    eoid = db.Column(db.Integer, db.ForeignKey('educate_organisation.eoid'), primary_key=True)

    participant = db.relationship('Participants', back_populates='participants_eo')
    educate_organisation = db.relationship('EducateOrganisation', back_populates='participants_eo')
