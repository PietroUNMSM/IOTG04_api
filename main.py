# main.py
# =============================================================================
# common
import os
import json
# requirements
from dotenv import load_dotenv
from fastapi import FastAPI
import pandas as pd

# -----------------------------------------------------------------------------

load_dotenv('./.env')

app = FastAPI()


# => routers
@app.get('/')
async def mainIndex() -> ...:
    return main_index()

#variable_riego (temperatura, humedad)-> float64 || fecha -> object
@app.get('/fecha/{fecha}')
async def variable_riegoInfo(fecha: str) -> ...:
    return variable_riegoInfo(fecha)


# => functions
def main_index() -> dict:
    return {'message': 'use esta api para tu visualizacion'}


def variable_riegoInfo(fecha: str) -> dict:
    host_data = os.environ['HOST_DATA']


    df = pd.read_csv(f'{host_data}/lectura_revisadaV2.csv', sep=',', encoding='utf-8')
    subdf = df[df['fecha'] == fecha]
    return json.loads(subdf.to_json(orient='records', date_format='iso'))