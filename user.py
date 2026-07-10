class User:
    def __init__(self, database):
        self.database = database

    def login(self):
        self.database.connect()
        print("User logged in.")
        self.database.disconnect()