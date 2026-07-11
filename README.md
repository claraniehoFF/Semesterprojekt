# semesterprojekt

## Lokales Starten
Das Projekt besteht aus einem Frontend und einem Backend. Im Grundverzeichnis des Projekts werden die folgenden Befehle ausgeführt, um die Komponenten zu starten. 
Es ist wichtig zu beachten, dass zuerst das Backend geladen wird, da ansonsten kein Zugriff auf die Datenbank besteht:
uv run uvicorn backend.main:app --reload

uv run streamlit run frontend/app.py


**Grupenmitglieder**
1. Clara Nienhoff
2. Romy Münchberg

**Aufbau des Projekts:**
Im Hauptverzeichnis liegen pyproject.toml, uv.lock, die lokale Datenbank, sowie die README.md. Im Frontend befindet sich lediglich eine Datei namens app.py, in der der Code des Frontends liegt. In einem weiteren Verzeichnis namens backend liegt die Datei main.py, die den Code des Backends enthält. 


**Was macht die Anwendung:**
Die Anwendung hat die folgenden Funktionen : 
1. Ausgabe bereits bestehender Buchungen
2. Eine Buchung hinzufügen. 
3. Eine GuV für den alle Buchungen bis zu einem angegebenen Datum erhalten.
4. Eine Warnung ausgeben, falls eine festgelegte Gewinn/Verlustsumme unterschritten wurde. 





**Hauptsächlicher Einsatz von AI:**
Lernen von Konzepten und Detailnachfragen. Ausarbeitung von Grundideen und Verbesserung von Code. Beispiel: „Wie kann ich mithilfe von FastAPI einen neuen Eintrag in meine Datenbank hinzufügen und welche Schritte passieren dabei im Hintergrund?“

Unterteilung in die verschiedenen Komponenten des Projekts
---

**Welche Teile wurden ohne AI von mir erstellt?**
Grundidee, Struktur des Projekts, Ansätze (beispielsweise, dass die Optionen über ein simples Dropdown-Menü ausgewählt werden können), Pydantic-Grundstruktur, GuV-Berechnung im Backend, Frontend und die Visualisierung der GuV.

---

**Verwendung von AI:**
Ich habe ausschließlich ChatGPT verwendet. https://chatgpt.com/

## Backend:

**Prompt:** „Welche Datentypen sollte ich in meine Pydantic-Klasse packen, um die Rückgabe der Buchungen aus meiner SQLite3-Tabelle zu validieren?“
**Rückgabe:** Klasse mit den entsprechenden Datentypen.

**Prompt:** „Wie verbinde ich meine Datenbank namens "" mit meinem FastAPI-Backend?“
**Rückgabe:** Benötigte Imports und Vorgehensweise.

**Prompt:** „Wieso zeigst du mir in deinem Beispiel an, dass die Schemas in einer eigenen Datei liegen?“
**Antwort:** Für eine bessere Übersicht sollten die Schemas für Pydantic in einer eigenen Datei liegen.

**Bugfixing:**
Ich erhielt nach dem Testen meines Backends eine Fehlermeldung. Diese habe ich mithilfe von ChatGPT gelöst. Dafür habe ich die Fehlermeldung kopiert und die Antwort übernommen (eine Root-Funktion fehlte).

ChatGPT hat außerdem Inkonsistenzen zwischen Pydantic und meiner Funktion zum Erhalten der Buchungen behoben.

---

## Frontend:

**GenAI:** ChatGPT

**Unterstützungsfall:** JSON-Rückgabe der lokalen Datenbank in einen DataFrame [1] umwandeln, um diesen mit Streamlit darzustellen.

**Prompt:** „Wie kann ich Daten von meiner Datenbank anfragen und die JSON-Rückgabe in einen Pandas DataFrame umwandeln, um diesen anschließend mit Streamlit darzustellen?“

**Rückgabe:** Code, der die Anfrage, eine korrekte Umwandlung und eine Abspeicherung als DataFrame enthält.

**Verwendung:** Code-Snippet erhalten und eingefügt.

---

**Unterstützungsfall:** Buchungsanfrage an das Backend stellen.

**Kontext:** Alle wichtigen Informationen zur Buchung hat der Nutzer bereits abgespeichert.

**Prompt:** „Wie kann ich die abgespeicherten Variablen in die gewünschte Form [Ausschnitt des Pydantic-Schemas] bringen und korrekt an das FastAPI-Backend übermitteln?“

**Rückgabe:** Umwandlung meiner Variablen in das gewünschte Format, Einfügung eines `st.button()` und eine Anweisung, dass nach dem Drücken des Buttons die Buchung an die entsprechende URL gesendet wird.

---

**Unterstützung:** Es wird automatisch die erste Option ausgeführt, wenn ich `streamlit selectbox` verwende.


**Prompt:** „Wie kann ich verhindern, dass bei der Verwendung von `st.selectbox` automatisch die erste Option ausgeführt wird?“

**Antwort:** Auswahl mehrerer Möglichkeiten, um das gewünschte Verhalten herbeizuführen. Ich habe ein Code-Snippet zurückerhalten.

---

**Unterstützung:** Mein Plot wurde nicht angezeigt.

**Antwort:** Eine zusätzliche Streamlit-Funktion wird benötigt.

---

## Kreative Zusatzerweiterung:


Ich möchte eine grafisch ansprechende Warnung/Entwarnung, beruhend auf Verlusten/Gewinnen in einem gegebenen Zeitraum geben. Die Idee ist dabei Mitarbeiter mit grafischer Untermalung darauf aufmerksam zu machen, falls zu hohe Verluste erzielt werden. Die Summe beläuft sich zurzeit auf 20 Tausend Euro Verlust, aber kann entsprechend angepasst werden.

**KI-Unterstützung für die Zusatzerweiterung:**
ChatGpt hat mir Markdown-Code ausgegeben, um eine entsprechende Grafik zu erhalten, da ich kein Widget gefunden habe, was die Aufgabe adäquat erfüllt.

Der Markdown Code wurde vollständig von ChatGPT übernommen.

## README:
Die Rechtschreibung, Grammatik und Grafische Aufmachung wurden von ChatGpt verbessert.
