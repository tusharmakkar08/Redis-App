import redis
import MySQLdb as mdb
import sys

con=None

try:

    con=mdb.connect('localhost', 'testuser','test623', 'tio')
    cur=con.cursor()
    cur.execute("select * from student")
    data=cur.fetchall()
    r_server = redis.Redis("localhost")
    k=len(data)
    for i in xrange(k):
        r_server.rpush("students",data[i])
    print r_server.lrange("students",0,-1)
    r_server.delete("students")
    
except mdb.Error,e:
    
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
    
