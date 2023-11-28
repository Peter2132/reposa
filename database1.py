import sqlite3
class Database:
    def __init__(self, db_path):
        self._db_path = db_path

    def execute_query(self, query, parameters=None):
        connection = sqlite3.connect(self._db_path)
        cursor = connection.cursor()

        try:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

            connection.commit()
            return cursor
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()