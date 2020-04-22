import MySQLdb

class DatabaseUtil:
    HOST = "34.87.229.96"
    USER = "root"
    PASSWORD = "banana"
    DATABASE = "carsharesystem"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(DatabaseUtil.HOST, DatabaseUtil.USER,
                DatabaseUtil.PASSWORD, DatabaseUtil.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    ##Create User and Car DB

        def createUserTable(self):
            with self.connection.cursor() as cursor:
                cursor.execute("""
                create table if not exists User (
                    UserID int not null auto_incremnet,
                    FirstName not null,
                    LastName not null,
                    constraint PK_User primary key (UserID)
                ) """)
        self.connection.commit()

        def insertUser(self, fname, lname):
            with self.connection.cursor() as cursor:
                cursor.execute("insert into User (FirstName, LastName)", (fname, lname,))
            self.connection.commit()

            return cursor.rowcount == 1
        
        def getPerson(self):
            with self.connection.cursor() as cursor:
                cursor.execute("select PersonID, Name from Person")
                return cursor.fetchall()
