class Venue():
    __table__ = 'venues'
    attributes = ['foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    @classmethod
    def find_by_foursquare_id(self, foursquare_id, cursor):
        foursquare_query = """SELECT * FROM venues WHERE foursquare_id = %s"""
        cursor.execute(foursquare_query, (foursquare_id,))
        return cursor.fetchone()

    def values(self):
        venue_attrs = self.__dict__
        return [venue_attrs[attr] for attr in self.attributes if attr in venue_attrs.keys()]

    def keys(self):
        venue_attrs = self.__dict__
        selected = [attr for attr in self.attributes if attr in venue_attrs.keys()]
        return ', '.join(selected)


    def save(self, conn, cursor):
        s_str = ', '.join(len(self.values()) * ['%s'])
        venue_str = f"""INSERT INTO {self.__table__} ({self.keys()}) VALUES ({s_str});"""
        cursor.execute(venue_str, list(self.values()))
        conn.commit()


