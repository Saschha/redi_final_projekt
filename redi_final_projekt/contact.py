from flask import Flask, render_template, request, redirect, url_for, jsonify
from objekts import Contact

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return "Please fill in all fields.", 400

    c = Contact(name=name, email=email, message=message)
    c.save()
    return redirect(url_for("contact_page", success=1))

@app.route("/api/contacts", methods=["GET"])
def api_contacts():
    return jsonify(Contact.get_all())

if __name__ == "__main__":
    print("URL map:", app.url_map)
    app.run(debug=True)
