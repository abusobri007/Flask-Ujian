from flask import Flask, render_template , request,  redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kayu.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Kayu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jenis = db.Column(db.String(50))
    ukuran = db.Column(db.Integer())
    berat = db.Column(db.Integer())
    variabel = db.Column(db.Integer())
    harga = db.Column(db.Integer())

    def __repr__(self):
        return self.jenis




       
@app.route("/list_kayu/<id>/edit")
def edit_peserta(id):
    obj = Kayu.query.filter_by(id=id).first()
    return render_template("edit_kayu.html",obj=obj)

@app.route("/list_kayu/<id>/update", methods=['POST'])
def update_peserta(id):
    obj = Kayu.query.filter_by(id=id).first()#data from db
 #data from cline server
    f_jenis =request.form.get("jenis")
    f_ukuran =request.form.get("ukuran")
    f_berat =request.form.get("berat")
    f_variabel =request.form.get("variabel")
    f_harga=request.form.get("harga")    
    #data form db whiht data from cline server
    obj.jenis=f_jenis
    obj.ukuran=f_ukuran
    obj.berat=f_berat
    obj.variabel=f_variabel
    obj.harga=f_harga

    #save perubahan data ke db

    db.session.add(obj)
    db.session.commit()
    return redirect('/list_kayu')   

