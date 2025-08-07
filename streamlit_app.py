import streamlit as st
import requests
import datetime
import os
from daily_data_downloader import get_last_24h_range, download_csv_data, parse_daily_data

st.title("Grafana Data Downloader")
st.write("Download daily data from Grafana dashboard")

if st.button("Download Last 24 Hours Data"):
    with st.spinner("Downloading data..."):
        from_time, to_time = get_last_24h_range()
        url = f"https://g-b234af4689.grafana-workspace.us-east-1.amazonaws.com/d/yk_0csuVk/tahms-dashboard-dl-production?orgId=1&from={from_time}&to={to_time}&viewPanel=15"
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            today = datetime.date.today().strftime("%Y%m%d")
            csv_filename = f"daily_data_{today}.csv"
            
            with open(csv_filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            st.success(f"Data downloaded: {csv_filename}")
            
            # Display summary
            with open(csv_filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            st.subheader("Data Summary")
            st.write(f"**File:** {csv_filename}")
            st.write(f"**Data for last 24 hours ending:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            st.write(f"**File size:** {len(content)} bytes")
            st.write(f"**Total lines:** {len(content.split('\\n'))}")
            
            if content.startswith('<!doctype') or '<html' in content:
                st.warning("Downloaded HTML content (dashboard page)")
            else:
                st.info("Downloaded data content")
                lines = content.split('\\n')[:3]
                st.text("First 3 lines:")
                for line in lines:
                    if line.strip():
                        st.text(line[:100] + "..." if len(line) > 100 else line)
            
            # Download button
            st.download_button(
                label="Download CSV File",
                data=content,
                file_name=csv_filename,
                mime="text/csv"
            )
            
        except requests.exceptions.RequestException as e:
            st.error(f"Error downloading data: {e}")

st.sidebar.info("This app downloads data from the Grafana dashboard for the last 24 hours.")