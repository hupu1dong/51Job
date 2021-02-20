import sqlite3

dbpath = "./51job2.db"
def init_db(dbpath):
    sql = '''
        create table job
        (
        id integer primary key autoincrement,
        job_link text,
        jname text,
        cname varchar,
        area varchar,
        salary text,
        educate text,
        info text
        )
    '''    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

# init_db(dbpath)

def saveData(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()


    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values (%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()