# 3rd SEM Minor Project- 

# 📊 Social Media Usage Visualization (Hourly Analysis)
This project visualizes hourly social media usage trends using data stored in an Excel file. Each social media platform is plotted in a separate subplot, highlighting peak usage hours and overall daily engagement patterns.

## 🚀 Features
- Reads multiple sheets from an Excel file (UserUsageData.xlsx)
- Each sheet represents a different social media app
- Converts 24-hour time into 12-hour AM/PM format
- Line plots showing Active Users (in Millions)
- Automatically highlights and annotates peak usage time
- Clean visualization using Seaborn and Matplotlib

## 🗂️ Project Structure
Social-Media-Usage-Visualization/
├── UserUsageData.xlsx
├── social_media_usage.py
└── README.md

## 📄 Dataset Format
Each Excel sheet should follow this format:
Hour | Active Users (Millions)
00:00 | 12.5
01:00 | 10.8
...
23:00 | 18.2
Hour → Time in 24-hour format  
Active Users (Millions) → Usage count in millions

## 🛠️ Technologies Used
Python, Pandas, Seaborn, Matplotlib, Excel (.xlsx)

## ▶️ How to Run
1. Install required libraries:
pip install pandas seaborn matplotlib openpyxl
2. Place UserUsageData.xlsx in the project folder
3. Run the script:
python social_media_usage.py

## 📈 Output
- 2×2 grid of line charts
- One chart per social media app
- Peak usage hour highlighted with annotation
- Clean axis labels and styling
<img width="933" height="694" alt="image" src="https://github.com/user-attachments/assets/d92550ca-e7c4-4185-811b-1bc7094406a6" />

## 🎯 Use Cases
Academic data visualization, social media trend analysis, time-series analysis, portfolio projects

## 📌 Future Improvements
Interactive plots, support for more apps, export charts, demographic analysis

## 👤 Author
Naman Dewangan
