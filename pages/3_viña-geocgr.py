import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

st.set_page_config(layout="wide", page_title="GeoCGR+UUVV Viña del Mar", page_icon=":taxi:")

@st.experimental_singleton
def load_data():
    data = pd.read_csv(
        "ViñaFinal_pts.csv", #"uber-raw-data-sep14.csv.gz",
        #nrows=100000,  # approx. 10% of data
        #names=["descripción","monto","lat","lon",],  # specify names directly since they don't change
        #skiprows=1,  # don't read header since names specified directly
        #usecols=[1,2,77,78], # descripcion,monto,lat,lon
        #usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        #parse_dates=["date/time"],  # set as datetime instead of converting after the fact
    )

    return data

def hex(data):
    return pdk.Layer(
                    "HexagonLayer",
                    data=data, get_position=["lon", "lat"],
                    radius=100, elevation_scale=4, elevation_range=[0, 1000],
                    pickable=True, extruded=True,
                )
    
def map(data, lat, lon, zoom, coms):
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={"latitude": lat, "longitude": lon,
                "zoom": zoom, "pitch": 50,
            },
            layers=[hex(data),hex(coms)],
        )
    )


# FILTER DATA FOR A SPECIFIC HOUR, CACHE
@st.experimental_memo
def filterdata(df, hour_selected):
    return df #df[df["date/time"].dt.hour == hour_selected]

@st.experimental_memo
def mpoint(lat, lon):
    return (-33, -71.6) #np.average(lat), np.average(lon))

data = load_data()
uv = pd.read_json('https://elci.sitiosur.cl/unidades_vecinales/datos-vina-del-mar.php')
coms = pd.read_json('humedales_viña.json')
#uv.coordenadas = uv.coordenadas.apply(lambda c: [tuple(t) for t in list(set(c.split(';')))])
uv.coordenadas = uv.coordenadas.apply(lambda c0: [(eval(xx)[0],eval(xx)[1]) for xx in set(c0.split(';'))])

zoom_level = 14 
midpoint = mpoint(data["lat"], data["lon"])
print('MID:', midpoint)
hour_selected = 12
st.title('Proyectos GeoCGR comuna Viña del Mar')
map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11, uv)
st.write(uv)
