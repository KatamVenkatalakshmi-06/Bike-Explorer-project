# Bike-Explorer-project

This is a Flask-based web application that allows users to explore and compare different types of bikes based on categories such as budget-friendly, naked bikes, cruisers, sports bikes, and adventure bikes. The app provides detailed information, images, and EMI calculation options for each bike.

## 🛠 Features

- Browse bikes by category:
  - Budget-Friendly (Gear & Non-Gear)
  - Naked Bikes
  - Cruiser Bikes
  - Sports Bikes
  - Adventure Bikes
- View detailed information for each bike:
  - Name, Price, Launch Year, Special Features, Mileage
  - Color Variants, Manufacturer Website, and Image
- EMI Calculation:
  - Based on selected bike’s price for 12, 24, and 36-month plans

## 📂 Project Structure

```
project-root/
│
├── sample.py               # Main Flask application
├── templates/
│   ├── index.html          # Home page to select bike category
│   └── bikes_list.html     # Displays list of bikes and bike details
├── static/                 # (Optional) Add custom CSS/JS if needed
└── README.md               # Project description and setup guide
```

## 🖥 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML (via Jinja templates)
- **Data Source:** Hardcoded JSON-like dictionary

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the application:**
   ```bash
   python sample.py
   ```

5. **Access the app:**
   Open your browser and go to `http://127.0.0.1:5000/`


## 📌 Notes

- All bike data is stored statically in the `bikes` dictionary inside `sample.py`.
- EMI is calculated by dividing the price by number of months (12/24/36).
- You can customize or expand the dataset by adding new categories or bikes.

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
