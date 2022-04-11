# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
from cProfile import run


user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1['valid']:
            return fn(*args, **kwargs)
        else:
            print('You are not authenticated')
    return wrapper



@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)