import sqlite3
from Restrictions import Restrictions


class Event:

    def __init__(self,conn, event_id,manager_user_name, event_name, description, picture, start_time, end_time, location_lat, location_lng, minimum_participants, maximum_participants, restrictions):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.id = event_id
        self.manager_user_name = manager_user_name
        self.name = event_name
        self.description = description
        self.picture = picture
        self.start_time = start_time
        self.end_time = end_time
        self.location_lat = location_lat
        self.location_lng = location_lng
        self.minimum_participants = minimum_participants
        self.maximum_participants = maximum_participants
        self.restrictions = restrictions

    def save_to_db(self):
        self.restrictions.save_to_db()
        self.cursor.execute("""INSERT INTO Event VALUES(null,?,?,?,?,?,?,?,?,?,?,?)""",
                            (self.manager_user_name,self.name,  self.description,self.picture,self.start_time,self.end_time,self.location_lat,self.location_lng,self.minimum_participants, self.maximum_participants, self.restrictions.id))
        self.conn.commit()

    

    @staticmethod
    def init_events_list_from_db(conn, lat, lng):
        cursor = conn.cursor()
        restriction_cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Event ORDER BY ABS(event_Location_Lat - ?) + ABS(event_Location_Lng - ?) ASC LIMIT 10""", (lat, lng))
        res_list = []
        for res in cursor:
            restriction = Restrictions.get_from_db(conn, 2)
            res_list.append(Event(conn, res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], restriction))
        return res_list