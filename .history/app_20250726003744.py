from flask import Flask, render_template
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT"))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True, db=0)


@app.route("/health")
def health_check():
    return jsonify{}

@app.route("/")
def home_page():
    r.incr("count")
    return render_template("home.html")


@app.route("/count")
def count_page():
    count = r.get('count') or 0
    return render_template("count.html",count=int(count))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)