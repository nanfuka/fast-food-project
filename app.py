from flask import Flask, jsonify,request
from api.model.Responses import * 
from api.model.User import User
from api.model.UserRequest import UserRequest
from api.model.orderRequest import OrderRequest
from api.model.data import *
import jwt

app = Flask(__name__)

temp_orders =[OrderRequest("bacon","fresh","3","Deb")]
temp_users=[User("Nsubuga","Kalungiowak","llkldf@gmail.com","Deb","boosiko",True)]
data_store = DataStore(temp_users,temp_orders)


@app.route('/')
def api_documentation():
    return "WELCOME TO FAST FOOD FAST APPLICATION"
#login
@app.route('/api/v1/login',methods=['POST'])
def api_login():
    data = request.get_json(force=True)
    username = data.get('username', None)
    password = data.get('password', None)

    print(username)

    user = data_store.searchList(username)
    if user is not None:
        if user.verify_password(password):
            response = user.getDictionary()
            response["token"]=data_store.generate_auth_token(response)
            response["success"]=True
            print(str(response))
            return jsonify(response)
        else:
            return jsonify(login_fail), 200
    else:
        return jsonify(login_fail) ,200

#signup user
@app.route('/api/v1/register', methods=['POST'])
def register_user():
    data = request.args
    firstName = data.get("first_name")
    lastName = data.get("last_name")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if firstName is not None and lastName  is not None and email  is not None and username is not None and password is not None:
        user = data_store.searchList(username)
        if user is None :
            response = data_store.createUser(User(firstName,lastName,email,username,password)).getDictionary()        
            response["token"]=data_store.generate_auth_token(response)
            registration_successful["user"]=response
            return jsonify(registration_successful)
           
        else:
            return jsonify(login_fail) ,401
    else:
        return jsonify(create_request_fail)



if __name__ == '__main__':
    app.run(debug=True)
