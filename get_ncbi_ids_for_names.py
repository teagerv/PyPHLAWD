import os
import sys
import sqlite3

def get_taxid_for_name(cursor, name):
    cursor.execute("select ncbi_id from taxonomy where name = '"+name+"';")
    ttax_id = None
    for j in cursor:
        ttax_id = str(j[0])
    return ttax_id

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "python "+sys.argv[0]+" infile database"
        sys.exit(0)
    inf = open(sys.argv[1],"r")
    dbname = sys.argv[2]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    for i in inf:
        nm = i.strip()
        if len(nm) < 2:
            continue
        tt = get_taxid_for_name(c,nm)
        if tt is not None:
            print tt
    inf.close()
    c.close()
