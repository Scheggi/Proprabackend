import crypt
from loguru import logger
from hmac import compare_digest as compare_hash
from app import app, request, create_refresh_token, create_access_token, jsonify, jwt_refresh_token_required, \
    get_jwt_identity, jwt, get_raw_jwt, jwt_required
from models import *
from datetime import datetime


@app.route('/race/create', methods=['POST'])
def race_create():
    json_data = request.json
    new_Race = Race_Details(
        type=json_data["type"],
        place=json_data["place"],
        date=json_data["date"]
    )
    new_Race.save_to_db()
    new_id = new_Race.id
    resp = {'status': 'success',
            'message': 'Race created',
            'id': int("{}".format(new_id)),
            }
    return jsonify(resp, 200)

"""
@app.route('/user/order/create', methods=['POST'])
def order_create():
    json_data = request.json
    new_wheel = Wheels(
        raceID=json_data["raceid"],
        tyretype=json_data["tyretype"],
        tyremix= json_data["tyremix"],
        term= json_data["term"],
        variant=json_data["variant"],
        number = json_data["number"],
        orderdate= json_data["orderdate"],
        ordertime=json_data["ordertime"],
        pickuptime=json_data["pickuptime"]
    )
    new_wheel.save_to_db()
    new_id = new_wheel.id

    resp = {'status': 'success',
            'message': 'wheel set created',
            'id': "{}".format(new_id)
            }
    return jsonify(resp, 200)

"""
@app.route('/user/weather/create', methods=['POST'])
def weather_create():
    json_data = request.json
    new_data = Weather(
        raceID=json_data["raceID"],
        temp_ground=json_data["temp_ground"],
        temp_air=json_data["temp_air"],
        weather_des=json_data["weather_des"],
        datetime=datetime.now()
    )
    new_data.save_to_db()
    new_id = new_data.id
    resp = {'status': 'success',
            'message': 'Data created',
            'id': "{}".format(new_id),
            }
    return jsonify(resp, 200)


@app.route("/wheels_start_astrid/create",methods=['POST'])
def wheels_start_astrid_create():
    json_data = request.json
    new_data = WheelsStartAstrid(
        raceID = json_data["raceID"],
        set = json_data["set"],
        cat = json_data["cat"],
        subcat =json_data["subcat"],
        identifier = json_data["identifier"],
        numberOfSets =json_data["numberOfSets"]
    )
    new_data.save_to_db()
    new_id = new_data.id
    # create Timer
    
    resp = {'status': 'success',
            'message': 'wheel start created',
            'id': "{}".format(new_id),
            }
    return jsonify(resp, 200)


@app.route('/formel/create', methods=['POST'])
def formel_create():
    json_data = request.json
    new_data = Formel(
        formel=json_data["formel"]
    )

    new_data.save_to_db()
    resp = {'status': 'success',
            'message': 'Data created'
            }
    return jsonify(resp, 200)


@app.route('/formel/get', methods=['POST'])
@jwt_required
def formel_get():
    resp = {'status': 'success',
            'data': Formel.get_all()
            }
    return jsonify(resp, 200)


@app.route('/wheels_start/get', methods=['POST'])
@jwt_required
def get_wheels_start():
    json_data = request.json
    logger.debug(json_data)
    resp = {'status': 'success',
            'data':  WheelsStartAstrid.find_by_raceID((json_data["raceID"]))
            }
    return jsonify(resp, 200)


@app.route('/user/weather/getlast10', methods=['POST'])
@jwt_required
def get_weather_data():
    json_data = request.json
    resp = {'status': 'success',
            'data':  Weather.find_by_id(int(json_data["raceID"]))
            }
    return jsonify(resp, 200)


@app.route('/user/race/get', methods=['POST'])
@jwt_required
def get_race_data():
    resp = {'status': 'success',
            'data':  Race_Details.get_all_races()
            }
    return jsonify(resp, 200)


#user/raceDetails/get
@app.route('/user/raceDetails/get', methods=['POST'])
@jwt_required
def get_raceDetails_data():
    json_data = request.json
    resp = {'status': 'success',
            'data':  Race_Details.find_by_id(json_data["raceID"])
            }
    return jsonify(resp, 200)