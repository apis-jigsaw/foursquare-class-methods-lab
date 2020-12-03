from src.orm import *
from src.db_utilities import *

class Category:
    __table__ = 'categories'
    attributes = ['id', 'name']

    @classmethod
    def find_by_name(self, name, cursor):
        category_query = """SELECT * FROM categories WHERE name = %s """
        cursor.execute(category_query, (name,))
        category_record =  cursor.fetchone()
        category = build_from_record(self, category_record)
        return category

    @classmethod
    def find_or_create_by_name(self, name, conn, cursor):
        category = self.find_by_name(name, cursor)
        if not category:
            new_category = Category()
            new_category.name = name
            save(new_category, conn, cursor)
            category = self.find_by_name(name, cursor)
        return category


