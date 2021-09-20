import sqlalchemy as sa 

dialect = "mysql" 
driver = "mysqlconnector" 
username = "root" 
password = "pw1"
host = "localhost" 
port = 3306 
uri = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/python"

engine = sa.create_engine(uri)                                                                                                                                                                             
conn = engine.connect()

file = open("data_from_db.csv", "w")

with conn:
    raw = conn.execute("SELECT * FROM test_data")

    data = raw.fetchall()

    for d in data:
        s = str(d)[1:-1]+"\n"
        file.writelines(s)

engine.dispose()
file.close()
