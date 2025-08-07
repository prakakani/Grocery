#!/usr/bin/env python3

import requests
import datetime
import os
def get_last_24h_range():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    
    from_time = int(yesterday.timestamp() * 1000)
    to_time = int(now.timestamp() * 1000)
    
    return from_time, to_time

def download_csv_data():
    from_time, to_time = get_last_24h_range()
    url = f"https://g-b234af4689.grafana-workspace.us-east-1.amazonaws.com/d/yk_0csuVk/tahms-dashboard-dl-production?orgId=1&from={from_time}&to={to_time}&viewPanel=15"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        today = datetime.date.today().strftime("%Y%m%d")
        csv_filename = f"daily_data_{today}.csv"
        
        with open(csv_filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Data downloaded: {csv_filename}")
        parse_daily_data(csv_filename)
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")

def parse_daily_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print("\nDaily Data Summary:")
        print(f"File: {filename}")
        print(f"Data for last 24 hours ending: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        if content.strip():
            lines = content.split('\n')
            print(f"Total lines: {len(lines)}")
            print(f"File size: {len(content)} bytes")
            
            # Check if it's CSV or HTML
            if content.startswith('<!doctype') or '<html' in content:
                print("Downloaded HTML content (dashboard page)")
            else:
                print("Downloaded data content")
                print(f"First 3 lines:")
                for i, line in enumerate(lines[:3]):
                    if line.strip():
                        print(f"  {line[:100]}..." if len(line) > 100 else f"  {line}")
        else:
            print("No data found")
            
    except Exception as e:
        print(f"Error parsing data: {e}")

def download_daily_data():
    download_csv_data()

if __name__ == "__main__":
    download_daily_data()
