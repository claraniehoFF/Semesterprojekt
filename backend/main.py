import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd


app = FastAPI() 


class Buchung_get(BaseModel):
    id : int
    datum: str
    betrag: float
    kategorie: str
    buchungstyp: str
    beschreibung: str


class Buchung_post(BaseModel):
    datum: str
    betrag: float
    kategorie: str
    buchungstyp: str
    beschreibung: str
    


@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/buchungen/", response_model = list[Buchung_get])
def get_booking():

    conn = sqlite3.connect("semesterprojekt_buchungen.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM buchungen")
    rows = cursor.fetchall()



    return [Buchung_get(**dict(row)) for row in rows] 
    
    
@app.post("/buchungen/", response_model = Buchung_post)  
def post_booking(buchung : Buchung_post): 
    conn = sqlite3.connect("semesterprojekt_buchungen.db")  
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO buchungen (datum, betrag, kategorie, buchungstyp, beschreibung)
        VALUES (?, ?, ?, ?, ?)
    """, (
        buchung.datum,
        buchung.betrag,
        buchung.kategorie,
        buchung.buchungstyp,
        buchung.beschreibung
    ))

    conn.commit()
    conn.close()

    return buchung



@app.get("/GuV/")
def calculate_guv(datum):
    conn = sqlite3.connect("semesterprojekt_buchungen.db")
    cursor = conn.cursor()
    df = pd.read_sql_query("Select buchungstyp, datum, betrag from buchungen", conn)
    df = df[df["datum"] <= datum]
    einnahmen = df.loc[df["buchungstyp"] == "Einnahme", "betrag"].sum()
    ausgaben = df.loc[df["buchungstyp"] == "Ausgabe", "betrag"].sum()
    gewinn = einnahmen - ausgaben
    return {
        "einnahmen": einnahmen,
        "ausgaben": ausgaben,
        "gewinn": gewinn,
        "datum" : datum
    }




    
