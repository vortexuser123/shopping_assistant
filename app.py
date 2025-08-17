from flask import Flask, request, jsonify
app = Flask(__name__)

CATALOG = [
    {"id":1,"name":"Gaming Mouse","price":1499,"rating":4.4},
    {"id":2,"name":"Mechanical Keyboard","price":2999,"rating":4.6},
    {"id":3,"name":"USB-C Hub","price":999,"rating":4.1}
]

@app.get("/search")
def search():
    q = request.args.get("q","").lower()
    return jsonify([p for p in CATALOG if q in p["name"].lower()])

@app.post("/compare")
def compare():
    ids = request.json.get("ids",[])
    picks = [p for p in CATALOG if p["id"] in ids]
    best = max(picks, key=lambda x: (x["rating"], -x["price"])) if picks else None
    return jsonify({"items":picks,"recommendation":best})

if __name__ == "__main__":
    app.run(port=5053)
