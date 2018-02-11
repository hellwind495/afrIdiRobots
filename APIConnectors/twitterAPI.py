import twitter

class twitterAPI:

    def __init__(self,custKey,custSecret,accessToken,accessSecret):
        self.custKey = custKey
        self.custSecret = custSecret
        self.accessToken = accessToken
        self.accessSecret = accessSecret
        self.api = twitter.Api(consumer_key=self.custKey,
        consumer_secret=self.custSecret,
        access_token_key=self.accessToken,
        access_token_secret=self.accessSecret)

    def post(self, message, in_reply_to_status_id = None):
        status = self.api.PostUpdate(message, in_reply_to_status_id = in_reply_to_status_id)
        return status

    def delete(self,id):
        status = self.api.DestroyStatus(id)
        return status

    def postToThread(self, message, in_reply_to_status_id = None):
        username = self.api.VerifyCredentials().screen_name
        status = self.api.PostUpdate('@%s ' % username + message, \
            in_reply_to_status_id = in_reply_to_status_id)
        return status
