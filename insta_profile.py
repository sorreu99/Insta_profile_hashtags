class InstaProfile:
    def __init__(self, json):
        self.json = json
        # self.followers = self.get_followers()
        self.user_name = self.get_followers()

    def get_followers(self):
        value = self.json["graphql"]
        value1 = value["user"]
        value2 = value1["edge_followed_by"]
        value3 = value2["count"]
        return value3

    def get_username(self):
        value = self.json["graphql"]
        value1 = value["user"]
        value2 = value1["username"]
        return value2
