import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("📈 Kalyan Jewellers - Cup & Handle Pattern (1H)")

st.write("Fetching latest 1H data for KALYANKJIL.NS...")
data = yf.download("KALYANKJIL.NS", interval="1h", start="2024-05-03", end="2024-05-08")

if data.empty:
    st.error("Failed to fetch stock data. Please check symbol or network.")
else:
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])

    cup_start_time = '2024-05-05 10:15:00'
    cup_start_price = 527
    cup_bottom_time = data['Close'].idxmin()
    cup_bottom_price = data.loc[cup_bottom_time]['Close']
    breakout_time = cup_bottom_time + pd.Timedelta(hours=10)
    breakout_price = 530

    fig.add_trace(go.Scatter(x=[cup_start_time], y=[cup_start_price], mode='markers+text',
                             name="Cup Start", text=["Cup Start"], textposition="top center",
                             marker=dict(color='blue', size=10)))

    fig.add_trace(go.Scatter(x=[cup_bottom_time], y=[cup_bottom_price], mode='markers+text',
                             name="Cup Bottom", text=["Cup Bottom"], textposition="bottom center",
                             marker=dict(color='orange', size=10)))

    fig.add_hline(y=527, line_dash="dot", line_color="green", annotation_text="Resistance 527")

    fig.add_trace(go.Scatter(x=[breakout_time], y=[breakout_price], mode='markers+text',
                             name="Breakout Target", text=["Potential Breakout"], textposition="top center",
                             marker=dict(color='red', size=10)))

    fig.update_layout(title="Kalyan Jewellers (KALYANKJIL.NS) - Cup & Handle Pattern (1H)",
                      xaxis_title="Time",
                      yaxis_title="Price (INR)",
                      xaxis_rangeslider_visible=False)

    st.plotly_chart(fig, use_container_width=True)
