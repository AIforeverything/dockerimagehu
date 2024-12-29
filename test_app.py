#this is for unit testing
#pytest can recognise if the file name starts with test, so this file name test_
from app import app

def test_home():
    response=app.test_client().get("/") #we get responce from homw
    #checking responce using assert
    assert response.status_code==200 #if successful
    assert response.data=="successful"
    