import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, session, flash
import qrcode

app = Flask(__name__)

# SECRET KEY FOR SESSION
app.secret_key = "change_this_to_something_random"

# FOLDERS
UPLOAD_FOLDER = os.path.join("static", "uploads")
QR_FOLDER = os.path.join("static", "qr")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(QR_FOLDER, exist_ok=True)

# POINTS PER CATEGORY (out of 10, as you asked)
CATEGORY_POINTS = {
    "plastic_bottle": 4,
    "plastic_wrapper": 7,
    "plastic_can": 9,
    "plastic_bag": 8,
    "other_plastic": 5,  # extra category
}

# SIMPLE IN-MEMORY "DATABASE"
waste_items = []  # each item is a dict


@app.route("/", methods=["GET", "POST"])
def home():
    """
    PAGE 1: HOME
    Collects user info: name, phone, email
    Stores in session.
    """
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not phone or not email:
            flash("Please fill all fields", "error")
            return redirect(url_for("home"))

        session["user_name"] = name
        session["user_phone"] = phone
        session["user_email"] = email
        session.setdefault("total_points", 0)

        return redirect(url_for("categories"))

    return render_template("home.html")


@app.route("/categories", methods=["GET", "POST"])
def categories():
    """
    PAGE 2: CATEGORIES
    - Shows plastic categories
    - Lets user click a photo / upload image
    - Generates a unique QR code for that item
    - Assigns points based on category
    """
    if "user_email" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        category = request.form.get("category")
        photo = request.files.get("photo")

        if not category or category not in CATEGORY_POINTS:
            flash("Please select a valid category.", "error")
            return redirect(url_for("categories"))

        if not photo or photo.filename == "":
            flash("Please capture or upload a photo.", "error")
            return redirect(url_for("categories"))

        # Save uploaded image
        ext = os.path.splitext(photo.filename)[1]
        image_filename = f"{uuid.uuid4().hex}{ext}"
        image_path = os.path.join(UPLOAD_FOLDER, image_filename)
        photo.save(image_path)

        # Generate unique ID for the item
        item_id = uuid.uuid4().hex

        # QR text can contain category + item id + user email
        qr_text = f"{category}|{item_id}|{session['user_email']}"
        qr_img = qrcode.make(qr_text)
        qr_filename = f"{item_id}.png"
        qr_path = os.path.join(QR_FOLDER, qr_filename)
        qr_img.save(qr_path)

        # Points for this item
        points = CATEGORY_POINTS.get(category, 0)

        # Save record in memory
        waste_items.append(
            {
                "item_id": item_id,
                "user_email": session["user_email"],
                "category": category,
                "image_filename": image_filename,
                "qr_filename": qr_filename,
                "points": points,
            }
        )

        # Update user's total points in session
        session["total_points"] = session.get("total_points", 0) + points

        flash("Plastic added successfully! QR code generated.", "success")
        return redirect(url_for("wallet"))

    return render_template("categories.html", category_points=CATEGORY_POINTS)


@app.route("/wallet")
def wallet():
    """
    PAGE 3: WALLET
    Shows:
    - Total star points
    - List of items with category, points, QR code and photo
    """
    if "user_email" not in session:
        return redirect(url_for("home"))

    user_email = session["user_email"]

    # Filter items belonging to this user
    user_items = [item for item in waste_items if item["user_email"] == user_email]
    total_points = sum(item["points"] for item in user_items)

    # Keep session in sync
    session["total_points"] = total_points

    # Convert numeric points to "stars" for each item (string of ★)
    for item in user_items:
        item["stars"] = "★" * item["points"]  # careful: many stars if points big

    return render_template(
        "wallet.html",
        user_name=session.get("user_name"),
        total_points=total_points,
        items=user_items,
    )


if __name__ == "__main__":
    # Debug for development; for deployment, use a proper server
    app.run(host="0.0.0.0", port=5000, debug=True)
