import facebook

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
