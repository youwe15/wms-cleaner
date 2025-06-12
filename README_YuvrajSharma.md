# WMS Assignment – Yuvraj Sharma

## Overview
This Streamlit app allows you to upload a sales CSV file and map SKUs to MSKUs using a second CSV file.

## How It Works
- Upload `sales_data.csv` with a column "SKU"
- Upload a mapping file with columns `SKU` and `MSKU`
- The app maps each SKU or combo SKUs to their MSKUs
- You can download the cleaned output

## Tech Stack
- Python
- Streamlit
- Pandas

## Instructions to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```