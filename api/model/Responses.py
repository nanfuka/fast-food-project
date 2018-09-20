#Request Responses
registration_successful={
        'success':True,
        'message':"User Registered Succesfully.",
        }
login_successful={
        'success':True,
        'message':"Logined in Succesfully.",
        }
login_fail={
        'success':False,
        'message':"Login Failed."
        }
auth_fail={
        'success':False,
        'message':"You are not authorised to access this page."
        }
request_fail={
        'success':False,
        'message':"Not a valid Request ID."
        }
create_request_fail={
        'success':False,
        'message':"All fields required."
        }
create_request_successful={
        'success':True,
        'message':"Your request was submitted successfully.",
        }
requests = [{'id': 20003,'title': u'Range Rover','type': u'Repair','category': u'Cars','status':u'Completed'},{'id': 20004,'title': u'Samsung S7','type': u'Repair','category': u'Phones and Tablet','status':u'In Progress'}]