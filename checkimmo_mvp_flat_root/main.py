
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage():
    with open("index.html", "r") as file:
        return HTMLResponse(content=file.read())

@app.post("/generate")
async def generate_pdf(adresse: str = Form(...)):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Audit Immobilier - Checkimmo", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 10, f"Adresse analysée : {adresse}")
    pdf.ln(5)
    pdf.cell(0, 10, "Score de fiabilité : 89/100", ln=True)
    pdf.cell(0, 10, "Prix au m² estimé : 6 150 EUR", ln=True)
    pdf.cell(0, 10, "Loyer moyen : 27 EUR/m²", ln=True)
    pdf.cell(0, 10, "Rentabilité : 5,2%", ln=True)
    pdf.cell(0, 10, "Classe énergétique : C", ln=True)
    pdf.cell(0, 10, "Criminalité : Modérée", ln=True)
    pdf.cell(0, 10, "Recommandations : Vérifier règlement de copropriété", ln=True)
    os.makedirs("static", exist_ok=True)
    pdf.output("static/audit_demo.pdf")
    return FileResponse("static/audit_demo.pdf", media_type='application/pdf', filename="audit_checkimmo.pdf")
