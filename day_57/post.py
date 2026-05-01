import requests

class Post:
    def __init__(self):
        self.data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    def get_data(self):
        return self.data
    
    def get_post_data(self, post_id):
        for post in self.data:
            if post["id"] == post_id:
                return post