# -*- coding: utf-8 -*-
pw = ''
user_name = ''
import json
import MySQLdb
from flask import Flask, request, jsonify,render_template


app = Flask(__name__)
def createDrinker(name,type):
    connector = MySQLdb.connect(
    user= user_name,
    passwd=pw ,
    host=("localhost"),
    db='drinker'
    )

    cursor = connector.cursor()
    cursor.execute("insert into drinkers (name,type) values ('%s','%d');" %(name,int(type)))
    connector.commit()
    cursor.close()
    connector.close()

def deleteDrinker():
    connector = MySQLdb.connect(
    user= user_name,
    passwd=pw ,
    host=("localhost"),
    db='drinker'
    )

    cursor = connector.cursor()
    cursor.execute("delete from drinkers where 1")
    connector.commit()
    cursor.close()
    connector.close()

def selectDrinker():
    connector = MySQLdb.connect(
    user= user_name,
    passwd=pw ,
    host=("localhost"),
    db='drinker'
    )

    cursor = connector.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from drinkers")
    result = cursor.fetchall()
    connector.commit()
    cursor.close()
    connector.close()

    return result

"""R1outing: リクエストの URI とメソッドに応じた処理を呼び出し、結果を返す。"""
@app.route('/')
def index():
    deleteDrinker()
    return render_template('index.html')

@app.route('/matching')
def matching():
    return render_template('matching.html')

@app.route('/ranking')
def ranking():
    return render_template('ranking.html')

@app.route('/make_json',methods=['GET'])
def getjson():
    result = selectDrinker()
    return jsonify(ResultSet = {"result":result})


@app.route('/post_request',methods=['POST'])
def post_request():
    name = request.form["name"]
    type = request.form["type"]
    result = {"name":name,"type":type,"status":True}
    createDrinker(name,type)
    print(result)
    return jsonify(ResultSet=result)


if __name__ == '__main__':
    # print(selectDrinker())
    app.run(host="0.0.0.0",port=3000,debug=True)
