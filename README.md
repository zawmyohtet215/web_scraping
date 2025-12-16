# 📱 Mobile Phone Price Extractor (Web Scraping Project)

This project is a **Python web scraping script** that extracts **mobile phone product information** from the *Unique Myanmar* website and exports the results into an **Excel file**.

The script automatically:

* Detects the **last page number**
* Loops through **all product pages**
* Extracts **product name**, **price**, and **inventory status**
* Saves the data as a timestamped `.xlsx` file

---

## 🚀 Features

* ✅ Automatic pagination handling
* ✅ Extracts:

  * Product Name
  * Product Price
  * Product Inventory Status
* ✅ Progress bar using `tqdm`
* ✅ Exports data to Excel
* ✅ Beginner-friendly structure with reusable functions

---

## 🛠️ Technologies & Libraries Used

* **Python 3**
* `requests` – HTTP requests
* `BeautifulSoup (bs4)` – HTML parsing
* `pandas` – Data handling & Excel export
* `tqdm` – Progress bar
* `datetime` – Timestamped filenames
* `time` – Request throttling

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/mobile-phone-price-extractor.git
cd mobile-phone-price-extractor
```

2. Install required libraries:

```bash
pip install requests beautifulsoup4 pandas tqdm html5lib
```

---

## ▶️ How to Run the Script

Run the Python file:

```bash
python price_extractor.py
```

After execution, an Excel file will be created in the project folder:

```text
Output HH-MM-SS.xlsx
```

---

## 📊 Output Example

| Product Name       | Product Price | Product Status |
| ------------------ | ------------- | -------------- |
| Samsung Galaxy A15 | 389000        | In stock       |
| iPhone 13          | 1899000       | Low stock      |

---

## 📂 Project Structure

```text
.
├── price_extractor.py
├── Output 12-30-45.xlsx
└── README.md
```

---

## ⚠️ Notes & Disclaimer

* This project is created **for educational purposes only**.
* Website structure may change, which can break the scraper.
* Please respect the website’s **robots.txt** and **terms of service**.
* Avoid excessive requests to prevent server overload.

---

## 📌 Possible Improvements

* Add error logging
* Save data to a database (PostgreSQL / SQLite)
* Add proxy & headers handling
* Convert to reusable class-based scraper
* Schedule automated runs

---

## 👨‍💻 Author

Developed by **Zawmyo Htet**
Data Analyst | Python & BI Enthusiast

If you find this project useful, feel free to ⭐ the repository!
