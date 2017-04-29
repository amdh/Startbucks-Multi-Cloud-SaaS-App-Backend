from flask import Flask, render_template, request, session, flash, redirect, jsonify, json, Response
from flask.views import MethodView
import uuid
from starbucksAPIService import StarbucksAPIService

application = Flask(__name__)
application.debug=True
service = StarbucksAPIService()
# API list

'''

GET     /v1/starbucks/ping
        Ping the applciation to test its access
        
POST    /v1/starbucks/order
        Create a new order, and upon success,
        receive a Location header specifying the new order’s URI.

GET     /v1/starbucks/order/{order_id}
        Request the current state of the order specified by the URI.

PUT     /v1/starbucks/order/{order_id}
        Update an order at the given URI with new information,
        providing the full representation.

DELETE  /v1/starbucks/order/{order_id}
        Logically remove the order identified by the given URI.

POST    /v1/starbucks/order/{order_id}/pay
        Process payment for the order.

GET     /v1/starbucks/orders
        Get list of Open Orders
'''
@application.route("/store1/v1/starbucks/ping", methods=['GET'])
def testPing():
    print("ping successfull")
    return json.dumps({'status' : 'ok' , 'message': 'Starbucks API service :v1'})

@application.route("/store1/v1/starbucks/order/<string:id>", methods=['GET'])
def getOrder(id):
    resp = Response(json.dumps(service.getOrder(id)))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@application.route("/store1/v1/starbucks/order", methods=['POST'])
def placeOrder():
    data = request.get_json(force=True)
    resp = Response(json.dumps(service.postOrder(data)))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@application.route("/store1/v1/starbucks/order/<string:id>", methods=['PUT'])
def updateOrder(id):
    data = request.get_json(force=True)
    print(data,id)
     
    resp = Response(json.dumps(service.putOrder(data,id)))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@application.route("/store1/v1/starbucks/order/<string:id>", methods=['DELETE'])
def removeOrder(id):
     
    resp = Response(json.dumps(service.deleteOrder(id)))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@application.route("/store1/v1/starbucks/order/<string:id>/pay", methods=['POST'])
def payOrder(id):
     
    resp = Response(json.dumps(service.payOrder(id)))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@application.route("/store1/v1/starbucks/orders", methods=['GET'])
def getOrders():
    order = service.getOrders();
     
    resp = Response(json.dumps(order))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    print("running on 0.0.0.0")
    application.run(host='0.0.0.0')