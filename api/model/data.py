from werkzeug.security import safe_str_cmp
import jwt
import datetime
from flask import jsonify
from api.model.Responses import * 
from functools import wraps
from flask import request

class DataStore:

	#innitialise datastore
	def __init__(self,users=[], orders=[]):
		self.users=users
		
		self.orders = orders
		self.key="my Jesus I love thee"

	def createUser(self,user):
		self.users.append(user)
		return user

	#Methods handling CRUD operations for Requests
	def modifyRequest(self, user_request):
		i=0
		for req in self.requests:
			if req.getId() == user_request.getId():
				self.requests[i]=user_request
				return user_request.getDictionary()
			i=i+1
		return None

	def updateOrder(self, order):
		i=0
		for req in self.orders:
			if req.getOrderId() == order.getOrderId():
				self.orders[i]=order
				return order.getDictionary()
			i=i+1
		return None





	def addOrders(self, req):
		self.orders.append(req)
		return req



	def getRequestSize(self):
		return len(requests)

	def getAllUsers(self):
		return self.users

	def getAllOrders(self):
		return self.orders


	def getAllOrdersForUser(self,order):
		response=[]
		for req in self.orders:
			if req.getOwner() == order:
				response.append(req.getDictionary())
		return response

	def getASpecificRequestsForUser(self,requestId):
		for req in self.orders:
			if req.getOrderId() == requestId:
				return req.getDictionary()
		return None

	def getASpecificOrderForUser(self,requestId):
		for req in self.orders:
			if req.getOrderId() == requestId:
				return req.getDictionary()
		return None

	def searchList(self,username):
		for item in self.users:
			if item.getUserName() == username:
				return item
			else:
				return None

	#Checking Authorization 
	def generate_auth_token(self, user):
		try:
			payload ={
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1200),
                'iat': datetime.datetime.utcnow(),
                'user': user
            }
			return  jwt.encode(
                payload,
                self.key,
                algorithm='HS256'
            ).decode('utf-8')
		except Exception as e:
			return e

	def token_required(self,func):
		@wraps(func)
		def decorated(*args,**kwargs):
			token = None
			if "Authorization" in request.headers:
				token =request.headers['Authorization']
			else:
				return jsonify(auth_fail), 401
			try:
				data = jwt.decode(token,self.key)
				current_user = self.searchList(data['user']['username'])
			except:
				return jsonify(auth_fail), 401
			return func(current_user,*args,**kwargs)
		return decorated