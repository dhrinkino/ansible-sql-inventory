import mysql.connector



if __name__ == "__main__":

    # prefill with your MySQL credentials
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "ansible_sql"
    try:
        sql_con = mysql.connector.connect(host=host,user=user,password=password,database=database)
    except:
        print("Failed to Login")
        exit() 
    sql_cur = sql_con.cursor()
    # making top level children reference

    try:
        sql_cur.execute("SELECT * FROM land")
        res_land = sql_cur.fetchall()
        for land in res_land:
            print("[{}:children]".format(land[1]))
            sql_cur.execute("SELECT * FROM loc WHERE land={} ".format(land[0]))
            res_loc = sql_cur.fetchall()
            for loc in res_loc:
                print("{}".format(loc[1]))
    except:
        print("Error during making SQL query")
        exit()

    try:
        sql_cur.execute("SELECT * FROM type")
        res_type = sql_cur.fetchall()
        print("\n")
        sql_cur.execute("SELECT * FROM loc")
        res_loc = sql_cur.fetchall()
        
        for loc in res_loc:
            print("\n[{}:children]".format(loc[1]))
            for s_type in res_type:
                print("{}_{}".format(s_type[1],loc[1]))
        print("\n")
    except:
        print("Error during SQL query")
        exit()
    
    try:
        for s_type in res_type:
            for loc in res_loc:
                
                sql_cur.execute("SELECT * FROM hosts WHERE type={} AND loc={}".format(s_type[0],loc[0]))
                res_hosts = sql_cur.fetchall()
                print("[{}_{}]".format(s_type[1],loc[1]))
                for host in res_hosts:
                    print(host[1])
                print("\n")
    except:
        print("Error during SQL query")
        exit() 
    try:
        for s_type in res_type:
            print("[{}]".format(s_type[1]))
            sql_cur.execute("SELECT * FROM hosts WHERE type={}".format(s_type[0]))
            res_hosts = sql_cur.fetchall()
            for host in res_hosts:
                print(host[1])
    except:
        print("Error during SQL query")
        exit() 
    

