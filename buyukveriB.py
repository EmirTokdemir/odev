import lib as k

terlık = k.sql.connect('vt.db')

vt = terlık
imlec = vt.cursor()
def gelme():    
    t_Data = """    
    CREATE TABLE IF NOT EXISTS kab(id INTEGER PRIMARY KEY AUTOINCREMENT,ad NOT NULL,yas NOT NULL)    
    """
    imlec.execute(t_Data)
    vt.commit()
