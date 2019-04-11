class Event:

    def _init_(self,conn, event_Id, event_name, user_name, description, picture, start_time, end_time, location, minimum_participants, maximum_participants, restrictions, rank):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.event_Id = event_Id
        self.event_name = event_name
        self.user_name = user_name
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.minimum_participants = minimum_participants
        self.maximum_participants = maximum_participants
        self.restrictions = restrictions
        self.rank = rank

    def save_to_db(self):
        self.rank.save_to_db()
        self.restrictions.save_to_db()
        self.corsur.execute("""INSERT INTO Event event_Manager
            event_Name TEXT,
            event_Description TEXT,
            evet_Picture BLOB,
            event_Start_Time INTEGER,
            event_End_Time INTEGER,
            event_Minimum_Participants INTEGER,
            event_Maximum_Participants INTEGER,
            FOREIGN KEY(restrictions_ID) REFERENCES Restrictions(restrictions_ID)
            FOREIGN KEY(rank_ID) REFERENCES Rank(rank_ID))""")

    @staticmethod
    def init_from_db(event_Id, user_name, location):
