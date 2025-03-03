from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LogsImagecompiler(db.Model):
    __tablename__ = "logs_imagecompiler"
    id = db.Column(db.String(255), primary_key=True)
    id_zip_file = db.Column(db.String(255), nullable=False)
