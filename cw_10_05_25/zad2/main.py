import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


def get_connection():
       return sqlite3.connect(r"C:\Users\korne\Desktop\studia\programming_2\sales.db")


conn = get_connection()
df = pd.read_sql_query("SELECT * FROM sales", conn)


product_filter = st.selectbox("Filtry", ["All"] + df["product"].unique().tolist())
if product_filter != "All":
    df = df[df["product"] == product_filter]

st.dataframe(df)


st.header("Dodaj sprzedaz")
with st.form("add_sale_form"):
    product = st.text_input("Nazwa produktu")
    quantity = st.number_input("Ilosc", min_value=1, step=1)
    price = st.number_input("Cena", min_value=0.0, step=0.01)
    date = st.date_input("Data")
    submitted = st.form_submit_button("Add Sale")

    if submitted:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
                       (product, quantity, price, date))
        conn.commit()
        conn.close()

st.header("Sprzedaz dzienna")
conn = get_connection()
daily_sales = pd.read_sql_query(
    "SELECT date, SUM(quantity * price) AS total_sales FROM sales GROUP BY date", conn
)
fig1 = px.bar(daily_sales, x="date", y="total_sales")
st.plotly_chart(fig1)


st.header("Sprzedane produkty")
product_sales = pd.read_sql_query(
    "SELECT product, SUM(quantity) AS total_quantity FROM sales GROUP BY product", conn
)
fig2 = px.pie(product_sales, names="product", values="total_quantity")
st.plotly_chart(fig2)


conn.close()