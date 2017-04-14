import pymysql

class PyMariaRepl(object):
    """

    """
    def __init__(self, connection, name):
        """
        Initalises the PyMariaRepl object
        :param connection: The MariaDB connection to obtain replication info from
        :return:
        """

        try:
            # shoudl test the version here and adjust for the old SHOW SLAVE STATUS syntax
            if name is None: # Only from MariaDB 10.0+ https://mariadb.com/kb/en/mariadb/show-slave-status/
                sql = "SHOW ALL SLAVES STATUS"
            else:
                sql = "SHOW SLAVE '{0}' STATUS".format(name)

            with connection.cursor() as cursor:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print(result)
        except:
            pass
        finally:
            if connection:
                connection.close()
