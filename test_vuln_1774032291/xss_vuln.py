from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    """VULNERABLE: Reflected XSS — user input rendered without escaping."""
    query = request.args.get("q", "")
    return f"<html><body><h1>Results for: {query}</h1></body></html>"

@app.route("/profile")
def profile():
    """VULNERABLE: Stored XSS potential."""
    name = request.form.get("name", "")
    return "<div>Welcome, " + name + "</div>"
