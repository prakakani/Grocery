# Grafana Data Downloader

A simple tool to download daily data from Grafana dashboard.

## Files

- `daily_data_downloader.py` - Core script for downloading data
- `streamlit_app.py` - Web interface using Streamlit
- `requirements.txt` - Python dependencies

## Usage

### Command Line
```bash
python daily_data_downloader.py
```

### Web Interface
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Features

- Downloads last 24 hours of data from Grafana
- Saves data with timestamp in filename
- Provides data summary and parsing
- Web interface for easy access