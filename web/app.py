from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from contact import get_tables
from connect import get_engine
from models import db, Loc, EducateOrganisation, Participants, Test, ParticipantsEO



app = Flask(__name__)
envpath = "config/zno_norm.env"

tables = get_tables(envpath)
tables.pop("participants_eo")

@app.route('/')
def index():
    return render_template('index.html', table_names=tables.keys(), tables=tables)

@app.route('/table/<table_name>')
def show_table(table_name):
    return render_template(f'{table_name}.html', data=tables[table_name])

# New route for the "loc" table
@app.route('/table/loc')
def show_loc_table():
    return render_template('loc.html', data=tables['loc'])

# New route for the "educate_organisation" table
@app.route('/table/educate_organisation')
def show_educate_organisation_table():
    return render_template('educate_organisation.html', data=tables['educate_organisation'])

# New route for the "participants" table
@app.route('/table/participants')
def show_participants_table():
    return render_template('participants.html', data=tables['participants'])

# TEST TABLE
@app.route('/table/test')
def show_test_table():
    return render_template('test.html', data=tables['test'])




@app.route('/delete/<testid>', methods=['POST', 'DELETE'])
def delete_row(testid):
    try:
        test_data = Test.query.filter_by(testid=testid).first()
        locid = test_data.locid
        outid = test_data.outid

        row_test = Test.query.get(testid)
        row_participant = Participants.query.get(outid)
        row_loc = Loc.query.get(locid)

        db.session.delete(row_test)
        db.session.delete(row_participant)
        db.session.delete(row_loc)

        db.session.commit()
        return redirect(url_for('show_test_table'))

    except SQLAlchemyError as e:
        error_message = f"Ошибка SQLAlchemy: {str(e)}"
        print(error_message)
        return render_template('test.html', data=tables['test'], error_message=error_message)



if __name__ == '__main__':
    app.run(debug=True)
