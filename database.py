class Database:
    def connect(self):
        print("Connecting to database...")

    def disconnect(self):
        return False

    def connect_alternative(self):
        """Initialize database connection."""
        print("Connection alternative established")

    def disconnect_alternative(self):
        print("Disconnecting alternative database")
