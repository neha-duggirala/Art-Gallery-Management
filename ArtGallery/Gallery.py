from flask import Flask, render_template, request, url_for, redirect
import MySQLdb
from _mysql_exceptions import IntegrityError
app = Flask(__name__)
db=MySQLdb.connect("localhost","neha","password","gallery" )
cur = db.cursor()
q1="INSERT into customers VALUES(%s %s %s %s)"
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/Home')
def home_page():
	return render_template('nav-bar.html')


@app.route('/customers',methods=['POST','GET'])
def customers():
	cur.execute("SELECT * from customers")
	customers_details= cur.fetchall()
	x = len(customers_details)
	# print x,customers_details
	return render_template('customers.html',c=customers_details,z=x)

@app.route('/artist',methods=['POST','GET'])
def artist():
	cur.execute("SELECT * from artist")
	artist_details= cur.fetchall()
	x = len(artist_details)
	# print x,artist_details
	return render_template('artist.html',c=artist_details,z=x)

@app.route('/artworks',methods=['POST','GET'])
def artworks():
	cur.execute("SELECT * from artwork")
	artworks_details= cur.fetchall()
	x = len(artworks_details)
	# print x,artworks_details
	return render_template('artworks.html',c=artworks_details,z=x)

@app.route('/gonewcust')
def gonewcust():
	return render_template('newcustomer.html')

@app.route('/godel')
def dele():
	return render_template('del.html',)

@app.route('/del',methods = ['POST', 'GET'])
def delcustomer():
	q="DELETE FROM customers where customer_id=%s "
	try:
		CID =int(request.form['DID'])
		print CID
		cur.execute(q,(CID,))
		db.commit()
	except:
		return render_template('del.html',msg="Cannot delete")
	return render_template('del.html',msg="Successfully Deleted")

@app.route('/newcustomer',methods = ['POST', 'GET'])
def newcustomer():
	try:
		CID = (request.form['XID'])
		name = (request.form['x_name'])
		addre =(request.form['addre'])
		cur.execute("""INSERT INTO customers (customer_id,name_,address) values (%s,%s,%s)""",(CID,name,addre))
		db.commit()
	except:
		return render_template('newcustomer.html',msg="Already Exists")
	return render_template('newcustomer.html',msg="Successfully Registered")

	# except Exception as e:
	# 	return (str(e))
	    

	# return redirect(url_for('newcustomers'))

@app.route('/Arts')
def Arts():
	cur.execute("SELECT a.title,a.price,ar.a_name,a.typess FROM artwork as a,artist as ar where a.typess=ar.art_style;")
	art=cur.fetchall()
	print art
	return render_template('Arts.html',f=art)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

