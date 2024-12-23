def is_user_authenticated():
    return False
def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            print("User is NOT authenticated")
        raise Exception("User is not authenticated")
    
    return wrapper

@check_user_auth
def do_sensitive_job():
    # do some tasks only if user is authenticated
    print("Results of some sensetive tasks")
try:
    do_sensitive_job()
except Exception as e: 
    print(e)