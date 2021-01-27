import sqlite3


def test_db_anyname():
    connection = sqlite3.connect("AnyName.db")
    cursor = connection.cursor()
    sql_command = "SELECT * FROM people"
    cursor.execute(sql_command)
    result = cursor.fetchall()
    assert 'AnyName' == result[0][1]