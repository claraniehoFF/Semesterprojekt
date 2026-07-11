import streamlit as st
import pandas as pd
import http
import requests
import json 
import matplotlib.pyplot as plt
import numpy as np


st.title("Buchungsübersicht")



optionen = ["Buchung hinzufügen", "Buchungen abrufen", "Gewinn und Verlustrechnung", "Verlustwarnung"]

auswahl = st.selectbox("Welche Aktion möchten Sie ausführen?", options =optionen, index=None,
    placeholder="Bitte auswählen...")


if auswahl == optionen[0]:
    datum = st.date_input("Wähle ein Datum für die Buchung")
    betrag = st.text_input("Betrag in Euro")
    kategorie = st.text_input("Kategorie")
    buchungstyp = st.selectbox(
    "Buchungstyp",
    ["Einnahme", "Ausgabe"])
    beschreibung = st.text_input("Beschreibung")
    if st.button("Buchung speichern"):
        buchung = {
            "datum": str(datum),
            "betrag" : float(betrag),
            "kategorie": kategorie,
            "buchungstyp": buchungstyp,
            "beschreibung": beschreibung,
        }
        response = requests.post(
            "http://127.0.0.1:8000/buchungen/",
            json=buchung,
        )
        if response.ok:
            st.success("Buchung gespeichert!")
            st.write(response.json())
        else:
            st.error(f"Fehler {response.status_code}: {response.text}")

if auswahl == optionen[1]:
    response = requests.get(
        "http://127.0.0.1:8000/buchungen/"
    )

    if response.ok:
        data = response.json()

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

if auswahl == optionen[2]:
    date = st.date_input("Wähle ein Datum, um die GuV bis einschließlich des gewählten Datums zu berechnen")
    response = requests.get(
        "http://127.0.0.1:8000/GuV/?datum=" + str(date)
    )   
    data = response.json()
    einnahmen = data["einnahmen"]
    ausgaben = data["ausgaben"]
    gewinn = data["gewinn"]
    datum = data["datum"]
    x = np.array(["Einnahmen", "Ausgaben", "Gewinn"])
    y = np.array([einnahmen, ausgaben, gewinn])
    fig, ax = plt.subplots()
    plt.bar(x,y)
    st.pyplot(fig)



if auswahl == optionen[3]:
    date = st.date_input("Wähle ein Datum, um eine Verlustwarnung auszugeben")
    response = requests.get(
        "http://127.0.0.1:8000/GuV/?datum=" + str(date)
    )   
    data = response.json()
    einnahmen = data["einnahmen"]
    ausgaben = data["ausgaben"]
    gewinn = data["gewinn"]
    datum = data["datum"]

    if gewinn <= -20000:
        st.markdown(
            f"""
            <div style="
                background-color:#ffcccc;
                padding:20px;
                border-radius:10px;
                border:3px solid red;
                text-align:center;
            ">
                <h1 style="color:red;">
                    ⚠️ WARNUNG ⚠️
                </h1>
                <h2 style="color:red;">
                    Verlust von {abs(gewinn):,.2f} €!
                </h2>
                <p style="font-size:20px;">
                    Der Verlust beträgt mehr als 20.000 €.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif gewinn > -20000:
        st.markdown(
            f"""
            <div style="
                background-color:#ccffcc;
                padding:20px;
                border-radius:10px;
                border:3px solid green;
                text-align:center;
            ">
                <h1 style="color:green;">
                    ✅ ENTWARNUNG ✅
                </h1>
                <h2 style="color:green;">
                    Gewinn von {gewinn:,.2f} €!
                </h2>
                <p style="font-size:20px;">
                    Der Gewinn liegt über 20.000 €.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )





    