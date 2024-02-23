import base64
from dataclasses import dataclass
from config_file import config

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from sqlalchemy import Column, Integer, Text, desc, null, insert, DateTime
from sqlalchemy import create_engine,  or_
from sqlalchemy.orm import scoped_session, sessionmaker, Query
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()
metadata = Base.metadata
engine = create_engine(config["sqlalchemy"]["engine"])
db_session = scoped_session(sessionmaker(autoflush=True, bind=engine))
Base.query = db_session.query_property(Query)

app = Flask(__name__)
api = Api(app)

app.secret_key = config["sqlalchemy"]["app_secret_key"]


@dataclass
class SteinSchereResult(Base):
    __tablename__ = 'stein_schere_results'

    id: int
    date: str
    amount_of_wins: int
    rock: int
    paper: int
    scissors: int
    lizard: int
    spock: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=func.now())
    amount_of_wins = Column(Integer)
    rock = Column(Integer)
    paper = Column(Integer)
    scissors = Column(Integer)
    lizard = Column(Integer)
    spock = Column(Integer)

    def serialize(self):
        return {'id' : self.foto_id,
                'date':  self.date,
                'amount_of_wins': self.amount_of_wins,
                'rock': self.rock,
                'paper': self.paper,
                'scissors': self.scissors,
                'lizard': self.lizard,
                'spock': self.spock}


class SteinSchereResultsService(Resource):
    def get(self, id):
        get_result = SteinSchereResult.query.get(id)
        if SteinSchereResult.query.get(id) is None:
            return jsonify({'Message': 'Result doesnt exists'})
        stein_schere_result = SteinSchereResult(id=get_result.id, amount_of_wins=get_result.amount_of_wins,
                                                rock=get_result.rock,
                                                paper=get_result.paper, scissors=get_result.scissors,
                                                lizard=get_result.lizard,
                                                spock=get_result.spock)
        return jsonify({"SteinSchereResult": stein_schere_result})

    def put(self, id):
        result_data = request.get_json(force=True)
        if SteinSchereResult.query.get(id):
            return jsonify({"Message": "Result already exists!"})
        result = SteinSchereResult(amount_of_wins=result_data['amount_of_wins'], rock=result_data['rock'],
                                 paper=result_data['paper'], scissors=result_data['scissors'], lizard=result_data['lizard'],
                                 spock=result_data['spock'])
        db_session.add(result)
        db_session.commit()
        db_session.flush()
        return jsonify({"Message": "Result successfully added to DB"})


@app.route('/results')
def get_all_results():
    results = SteinSchereResult.query.all()
    if not results:
        return jsonify({'Message': 'No results found'})

    return jsonify({'Results': results})


api.add_resource(SteinSchereResultsService, '/result/<int:id>')

@app.teardown_appcontext
def shutdown_session(exception=None):
    print("Shutdown Session")
    db_session.remove()


def init_db():
    # Erzeugen der Tabellen für die Klassen, die oben deklariert sind (muss nicht sein, wenn diese schon existiert)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    #init_db()
    app.run(debug=True)