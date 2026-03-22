import streamlit as st
import pandas as pd
import math

st.title("Halbwertszeit Rechner")
st.write("Berechne die verbleibende Menge eines radioaktiven Stoffes oder die Halbwertszeit.")

choice = st.radio("Was möchtest du berechnen?", ["Verbleibende Menge", "Halbwertszeit", "Zeit bis eine bestimmte Restmenge"])

if choice == "Verbleibende Menge":
    element = st.text_input("Gib ein radioaktives Element ein (z.B. Uran-238):")
    N0 = st.number_input("Anfangsmenge (N₀)", min_value=0.0, value=100.0)
    t = st.number_input("Verstrichene Zeit (t)", min_value=0.0, value=10.0)
    T_half = st.number_input("Halbwertszeit (T₁/₂)", min_value=0.1, value=5.0)

    if st.button("Berechne verbleibende Menge"):
        N = N0 * (0.5) ** (t / T_half)
        st.success(f"Die verbleibende Menge nach {t} Zeiteinheiten beträgt: {N:.2f}")
        result = {"Berechnung": "Verbleibende Menge", "Element": element, "N0": N0, "t": t, "T_half": T_half, "Ergebnis": round(N, 2)}
        st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])], ignore_index=True)

elif choice == "Halbwertszeit":
    element = st.text_input("Gib ein radioaktives Element ein (z.B. Uran-238):")
    N0 = st.number_input("Anfangsmenge (N₀)", min_value=0.0, value=100.0)
    N = st.number_input("Endmenge (N)", min_value=0.0, value=25.0)
    t = st.number_input("Verstrichene Zeit (t)", min_value=0.0, value=10.0)

    if st.button("Berechne Halbwertszeit"):
        if N <= 0 or N >= N0:
            st.error("Endmenge muss zwischen 0 und Anfangsmenge liegen!")
        else:
            T_half = t / (math.log2(N0 / N))
            st.success(f"Die Halbwertszeit beträgt: {T_half:.2f} Zeiteinheiten")
            result = {"Berechnung": "Halbwertszeit", "Element": element, "N0": N0, "t": t, "T_half": round(T_half, 2), "Ergebnis": round(T_half, 2)}
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])], ignore_index=True)

elif choice == "Zeit bis eine bestimmte Restmenge":
    element = st.text_input("Gib ein radioaktives Element ein (z.B. Uran-238):")
    N0 = st.number_input("Anfangsmenge (N₀)", min_value=0.0, value=100.0)
    N = st.number_input("Gewünschte Restmenge (N)", min_value=0.0, value=25.0)
    T_half = st.number_input("Halbwertszeit (T₁/₂)", min_value=0.1, value=5.0)

    if st.button("Berechne benötigte Zeit"):
        if N <= 0 or N >= N0:
            st.error("Restmenge muss zwischen 0 und Anfangsmenge liegen!")
        else:
            t = T_half * (math.log2(N0 / N))
            st.success(f"Die benötigte Zeit bis zur Restmenge beträgt: {t:.2f} Zeiteinheiten")
            result = {"Berechnung": "Zeit bis Restmenge", "Element": element, "N0": N0, "T_half": T_half, "Ergebnis": round(t, 2)}
            st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame([result])], ignore_index=True)

st.dataframe(st.session_state['data_df'])