import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(host='redis-server', port=6379, db=0)


@app.route("/")
def index():
    count = r.get("visit_counts")
    if not count:
        count = 0
    count = int(count)
    count += 1
    r.set("visit_counts", str(count))
    html = f"<h1>Welcome to Visitor Counter</h1><div><h2>total visit count:{count}</div>"
    return html


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
