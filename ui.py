import streamlit as st
import requests

# Streamlit UI Header
st.set_page_config(page_title="Data Backup & Recovery", page_icon="💾")
st.title("🚀 Data Backup and Recovery System")
st.markdown("Easily restore your backed-up files from IBM Cloud Object Storage.")

# Input fields for user entry
bucket = st.text_input("📦 Enter Bucket Name", "my-storage-bucket")
file_name = st.text_input("📂 Enter File Name to Restore", "backup_data.csv")

# Restore Button
if st.button("🔄 Restore File"):
    try:
        response = requests.get(f"http://127.0.0.1:5000/restore/sindhu_test/sample.txt")
        if response.status_code == 200:
            st.success(response.json().get("message", "✅ File restored successfully!"))
        else:
            st.error(f"❌ Error: {response.json().get('error', 'Unknown error occurred.')}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Failed to connect to server: {e}")
