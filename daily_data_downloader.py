#!/usr/bin/env python3

import requests
import datetime
import os

def download_daily_data():
    url = "https://g-b234af4689.grafana-workspace.us-east-1.amazonaws.com/"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Create filename with current date
        today = datetime.datetime.now().strftime("%Y%m%d")
        filename = f"daily_data_{today}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Data downloaded successfully: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_daily_data()