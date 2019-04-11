import sqlite3
from Restrictions import Restrictions


class Event:

    def _init_(self,conn, event_id, event_name, user_name, description, picture, start_time, end_time, location_lat, location_lng, minimum_participants, maximum_participants, restrictions, rank):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.id = event_id
        self.name = event_name
        self.user_name = user_name
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.location_lat = location_lat
        self.location_lng = location_lng
        self.minimum_participants = minimum_participants
        self.maximum_participants = maximum_participants
        self.restrictions = restrictions
        self.rank = rank

    def save_to_db(self):
        self.rank.save_to_db()
        self.restrictions.save_to_db()
        self.cursor.execute("""INSERT INTO Event event_Manager VALUES('?','?','?','?','?','?','?')""",
                            self.name, self.description,self.picture,self.start_time,self.end_time,self.location_lat,self.location_lat,self.minimum_participants, self.maximum_participants, Restrictions(self.restrictions).id, self.rank.id)
        self.conn.commit()

    @staticmethod
    def init_events_list_from_db(conn, lat, lng):
        cursor = conn.cursor()
        cursor.execute("""SELECT TOP 10 * FROM Event ORDER BY ABS(event_Location_Lat - ?) + ABS(Location_Lng - ?) ASC
                        """, lat, lng)
        res_list = []
        for i in cursor:
            print(i)
