class Event:

    def _init_(self, event_name, user_name, description, picture, start_time, end_time, minimum_participants, maximum_participants, restrictions, rank):
        self.event_name = event_name
        self.user_name = user_name
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.minimum_participants = minimum_participants
        self.maximum_participants = maximum_participants
        self.restrictions = restrictions
        self.rank = rank

    def save_to_server(self):
        self.rank.save_to_server()
        self.restrictions.save_to_server()
        c.execute("""INSERT INTO Event event_Manager
            event_Name TEXT,
            event_Description TEXT,
            evet_Picture BLOB,
            event_Start_Time INTEGER,
            event_End_Time INTEGER,
            event_Minimum_Participants INTEGER,
            event_Maximum_Participants INTEGER,
            FOREIGN KEY(restrictions_ID) REFERENCES Restrictions(restrictions_ID)
            FOREIGN KEY(rank_ID) REFERENCES Rank(rank_ID))""")
