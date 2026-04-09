# 🌿 PlastiStar  
### AI-Enabled Intelligent Waste System for Sustainable Plastic Management

PlastiStar is a web-based application that promotes responsible plastic waste disposal through awareness, classification, and reward-based engagement. Users can log plastic items, generate QR codes for traceability, and earn reward points while contributing to sustainability.

---

## 🚀 Features

- Plastic waste logging via image upload  
- Category-based reward point system  
- Unique QR code generation for each item  
- User wallet to track reward points  
- History tracking of logged items  
- Admin dashboard to view registrations and activity  

---

## 🧠 Concept

PlastiStar bridges the gap between awareness and action in plastic waste management by:
- Encouraging active user participation  
- Making sustainability engaging through rewards  
- Providing traceability using QR codes  
- Creating a simple data-driven waste tracking system  

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML5, CSS3, Jinja2  
- **Data Storage:** CSV files  

**Libraries Used:** Flask, qrcode, Pillow  

---
## 📂 Project Structure


plastistar_app/
├── app.py
├── requirements.txt
├── data/
│ ├── users.csv
│ └── waste_history.csv
├── static/
│ ├── uploads/
│ └── qr/
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── register.html
│ ├── categories.html
│ ├── wallet.html
│ ├── history.html
│ └── admin.html

--

## ⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/queserasera29/plastistar-app.git

cd plastistar_app


2. Install dependencies:

pip install -r requirements.txt


3. Run the application:

python app.py


4. Open in browser:

http://127.0.0.1:5000


---

## 🌐 Deployment

https://plastistar-app.onrender.com

---

## 📊 Data Handling

- Registrations stored in `users.csv`  
- Logged items stored in `waste_history.csv`  

Includes:
- Timestamp  
- User details  
- Category  
- Image  
- QR code  
- Reward points  

---

## 📌 Future Scope

- AI-based plastic detection  
- Database integration (PostgreSQL/MongoDB)  
- Mobile app development  
- Reward redemption system  
- Analytics dashboard  

---

## 👩‍🔬 Developed By

Ranjana Parab | Mabitha Mani
Department of Bioinformatics  
Guru Nanak Khalsa College  

---

## 🌍 License

Academic and research use only.
