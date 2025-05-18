
import streamlit as st
from datetime import datetime, timedelta

st.title("Calculadora de Sintrom (DTS y Próximo Control)")

def calcular_dts_pc(inr_actual, inr_anterior, dts_previa, fecha_actual):
    if inr_actual <= 1.6:
        nueva_dts = dts_previa * 1.10
        dias_pc = 14
    elif 1.7 <= inr_actual <= 1.8:
        nueva_dts = dts_previa * 1.05
        dias_pc = 14 if inr_anterior < 2 or inr_anterior > 3 else 21
    elif inr_actual == 1.9:
        nueva_dts = dts_previa
        dias_pc = 28
    elif 2.0 <= inr_actual <= 3.0:
        nueva_dts = dts_previa
        dias_pc = 28 if inr_anterior < 2 or inr_anterior > 3 else 35
    elif 3.1 <= inr_actual <= 3.3:
        nueva_dts = dts_previa
        dias_pc = 28
    elif 3.4 <= inr_actual <= 3.9:
        nueva_dts = dts_previa * 0.95
        dias_pc = 14 if inr_anterior < 2 or inr_anterior > 3 else 21
    elif inr_actual >= 4.0:
        nueva_dts = dts_previa * 0.90
        dias_pc = 14
    else:
        nueva_dts = dts_previa
        dias_pc = 28

    fecha_proximo_control = fecha_actual + timedelta(days=dias_pc)
    return round(nueva_dts, 2), fecha_proximo_control

with st.form("formulario_sintrom"):
    inr_actual = st.number_input("INR actual", min_value=0.0, step=0.1)
    inr_anterior = st.number_input("INR anterior", min_value=0.0, step=0.1)
    dts_previa = st.number_input("Dosis Total Semanal previa (mg)", min_value=0.0, step=0.1)
    fecha_actual = st.date_input("Fecha del control actual", value=datetime.today())
    submitted = st.form_submit_button("Calcular")

    if submitted:
        nueva_dts, fecha_pc = calcular_dts_pc(inr_actual, inr_anterior, dts_previa, fecha_actual)
        st.success(f"Nueva DTS: {nueva_dts} mg/semana")
        st.info(f"Próxima fecha de control: {fecha_pc.strftime('%Y-%m-%d')}")
