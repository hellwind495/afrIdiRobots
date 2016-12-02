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

    def post(self, message):
        status = self.api.PostUpdate(message)
        return status

    def delete(self,id):
        status = self.api.DestroyStatus(id)
        return status
