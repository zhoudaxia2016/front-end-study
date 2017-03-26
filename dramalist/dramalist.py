import bottle
import os
import sqlite3
import dramas
app = application = bottle.Bottle()

@app.route('/')
def index():
    return bottle.template('templates/index.html')

@app.route('/static/css/<filename>')
def static(filename):
    return bottle.static_file(filename,root='./static/css/')

@app.route('/static/js/<filename>')
def static(filename):
    return bottle.static_file(filename,root='./static/js/')

@app.route('/getdramas')
def getDramas():
    conn = sqlite3.connect('dramas.db')
    cu = conn.cursor()
    cu.execute('select * from dramas')
    result = cu.fetchall()
    conn.close()
    return {'dramas': result}

@app.route('/postdramas',method='POST')
def postDramas():
    data = bottle.request.json.get('data')
    filename = 'dramas.db'
    if os.path.exists(filename):
          dramas.delete()
    else:
        dramas.createTable()
    conn = sqlite3.connect('dramas.db')
    cu = conn.cursor()
    for item in data:
        sql = 'insert into dramas(name,isSeen,type) values("%s",%d,%d)' %(item['name'],item['isSeen'],item['type'])
        #print(sql)
        cu.execute(sql)
    conn.commit()
    conn.close()
    return '<p> Updated! </p>'

