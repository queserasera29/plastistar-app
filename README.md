🌿 PlastiStar

AI-Enabled Intelligent Waste System for Sustainable Plastic Management

PlastiStar is a web-based application designed to promote responsible plastic waste disposal through awareness, classification, and reward-based engagement. The platform allows users to log plastic items, generate QR codes for traceability, and earn reward points while contributing to sustainable practices.

🚀 Features
♻️ Plastic Waste Logging
Upload images of plastic items and classify them into categories.
🔍 Category-Based Scoring System
Assigns reward points based on type of plastic waste.
🔗 QR Code Generation
Generates a unique QR code for each logged item for traceability.
⭐ Reward Wallet System
Tracks total points earned by users for sustainable actions.
📊 History Tracking
Displays previously logged items with category, image, QR, and points.
🧑‍💻 Admin Dashboard
View all user registrations and logged data in tabular format.
🧠 Concept

Plastic waste management is a growing global issue. PlastiStar bridges the gap between awareness and action by:

Encouraging users to actively log plastic waste
Making sustainability engaging through rewards
Providing traceability using QR codes
Creating a data-driven model for waste tracking
🛠️ Tech Stack
Backend: Python, Flask
Frontend: HTML5, CSS3, Jinja2
Data Storage: CSV-based storage
Libraries Used:
Flask
qrcode
Pillow
📂 Project Structure
plastistar_app/
│
├── app.py
├── requirements.txt
├── data/
│   ├── users.csv
│   └── waste_history.csv
│
├── static/
│   ├── uploads/
│   └── qr/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── register.html
│   ├── categories.html
│   ├── wallet.html
│   ├── history.html
│   └── admin.html
⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/your-username/plastistar-app.git
cd plastistar_app
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open in browser:
http://127.0.0.1:5000
🌐 Deployment

The application is deployed using Render:

👉 https://plastistar-app.onrender.com

🔐 Admin Access

To view user registrations and logged data:

/admin

(Optional: secured using an admin key in production)

📊 Data Handling
User registrations are stored in users.csv
Logged plastic items are stored in waste_history.csv
Data includes:
Timestamp
User details
Category
Uploaded image
QR code
Reward points
📌 Future Scope
AI-based plastic detection using image classification
Integration with real databases (PostgreSQL / MongoDB)
Mobile application version
Real-world reward redemption system
Analytics dashboard for sustainability insights

👩‍🔬 Developed By
Ranjana Parab | Mabitha Mani
Department of Bioinformatics
Guru Nanak Khalsa College

🌍 License

This project is for academic and research purposes.

If you want, I can next:

Add badges (GitHub, Python, Flask)
Create a cool banner/logo for README
Or make it more startup/pitch style instead of academic
