import facebook
import requests

class fbpageAPI:

    def __init__(self, access_token, page_id):
        self.page_id = page_id
        self.access_token = access_token

    def post(self,message):
        graph = facebook.GraphAPI(access_token=self.access_token)
        return graph.put_object(parent_object=self.page_id, connection_name='feed', message=message)

    def delete(self,post_id):
        graph = facebook.GraphAPI(access_token=self.access_token)
        graph.delete_object(post_id)

    def generateNewToken(self,client_id, client_secret):
        r = requests.get('https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=fb_exchange_token&fb_exchange_token=%s' % (client_id,client_secret,self.access_token))
        newtokenString = dict(r.text)
        try:
            self.access_token = newtokenString['access_token']
        except:
            print('There is an issue with generating a new access token\n The error is described below:\n %s' % newtokenString)
        return self.access_token
