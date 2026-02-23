from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "DevOps EKS Project Running"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/config")
def config():
    return jsonify({
        "env": os.getenv("ENV", "local"),
        "db_user": os.getenv("DB_USER", "none")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)