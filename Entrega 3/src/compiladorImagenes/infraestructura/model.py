from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LogsImagecompiler(db.Model):
    __tablename__ = "logs_compiladorImagenes"
    id = db.Column(db.String(255), primary_key=True)
    id_cliente = db.Column(db.String(255), nullable=False)
    id_solicitud = db.Column(db.String(255), nullable=False)
    id_zip_file = db.Column(db.String(255), nullable=False)
