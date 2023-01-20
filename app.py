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




app.route("/list_kayu/<id>/delete")
def delete_pendafar(id):
    obj = Kayu.query.filter_by(id=id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect('/list_kayu')
if "__main__" ==__name__:
     app.run(debug= True,port =3000)
