from __future__ import annotations

from os import getenv
from sys import modules

from dotenv import load_dotenv
from flask_fullstack import Flask, SQLAlchemy

from common.constants import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

load_dotenv(".env")

app: Flask = Flask(__name__)
app.config["TESTING"] = "pytest" in modules.keys()
app.secrets_from_env("hope it's local")
app.configure_cors()

db_url: str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app, db_url)  # "echo": True
Base = db.Model

app.configure_error_handlers(print)
app.config["RESTX_INCLUDE_ALL_MODELS"] = True
