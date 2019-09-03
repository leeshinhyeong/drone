import pymysql

def db_insert(a, b, c) :
    # DB Connect
    conn = pymysql.connect(host='52.231.75.145', user='root', password='1234',db='mysql', charset='utf8')
    curs = conn.cursor()

    sql = """insert into dust_airkorea(gps_id, pm10Value, pm25Value, datecreated) values(%s, %s, %s, now())""";
    curs.execute(sql, (a, b, c))
    conn.commit()
    conn.close()
    #@sys.exit(1)

db_insert('test',12,35)

