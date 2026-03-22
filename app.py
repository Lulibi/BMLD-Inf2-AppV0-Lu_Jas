import pandas as pd
import streamlit as st

# --- DataManager und LoginManager initialisieren ---
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(
    fs_protocol='webdav',
    fs_root_folder="Informatik_2"  # <-- hier euren gemeinsamen Ordnernamen eintragen
)

login_manager = LoginManager(data_manager)
login_manager.login_register()  # stoppt die App, wenn nicht eingeloggt

# --- Nutzerspezifische Daten laden ---
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )

# --- App-Konfiguration und Navigation ---
st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/Halbwertszeit_Rechner.py", title="Halbwertszeit Rechner", icon=":material/info:")

pg = st.navigation([pg_home, pg_second])
pg.run()