# %% [markdown]
# # Módulo 54: Series de tiempo — Solución
#
# Author: Juliho Castillo Colmenares Ph.D.
#
# Enunciado para estudiantes: [m54-series-de-tiempo-guia.ipynb](m54-series-de-tiempo-guia.ipynb) · Lección: [m54-series-de-tiempo-leccion.ipynb](m54-series-de-tiempo-leccion.ipynb)
#
# ## Contexto
#
# Un fondo de inversión tiene posiciones en **IBM** y **Walmart** y quiere entender cómo se han comportado sus acciones de 2019 a 2023: si sus precios se mueven juntos, si muestran tendencia o estacionalidad, si las series son estacionarias y cuál sería un pronóstico ingenuo para el siguiente día de negociación basado en promedios móviles.
#
# ## Datos
#
# Precios diarios de `IBM` y `WMT` del 2019-01-01 al 2023-12-31, descargados de Yahoo Finance con `yfinance` (requiere internet). `Close` es el cierre ajustado (`auto_adjust=True`); las columnas tienen dos niveles (campo y ticker).
#
# ## Instrucciones
#
# 1. **Correlación entre IBM y Walmart:** precios de cierre alineados, correlación y diagrama de dispersión; correlación de los rendimientos diarios.
# 2. **Descomposición y autocorrelación:** descomposición aditiva con periodo de 252 días hábiles y correlograma con 40 rezagos.
# 3. **Prueba de estacionariedad de Dickey–Fuller** para cada precio de cierre.
# 4. **Promedio móvil de 30 días** y su gráfica junto al precio.
# 5. **Pronóstico a un día** con el último promedio móvil.
#
# *El enunciado original del curso no se conserva; estas instrucciones se reconstruyeron a partir de la solución.* El material del módulo (Buenas prácticas) confirma que la tarea asignada consistía en analizar y pronosticar con promedios móviles el precio de las acciones de IBM y Walmart.
#

# %% [markdown]
# ### Descarga de los datos

# %%
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose

# %%
# Step 1: Download historical data
start_date = "2019-01-01"
end_date = "2024-01-01"

# %%
ibm_data = yf.download("IBM", start=start_date, end=end_date)
ibm_data

# %%
walmart_data = yf.download("WMT", start=start_date, end=end_date)
walmart_data

# %% [markdown]
# ### Tarea 1. Correlación entre IBM y Walmart

# %%
# Step 2: Correlation Analysis

# Create DataFrames from the Close prices for alignment
ibm_close = ibm_data["Close"]["IBM"].to_frame()
ibm_close

# %%
walmart_close = walmart_data["Close"]["WMT"].to_frame()
walmart_close

# %%
aligned_data = ibm_close.join(walmart_close, how="inner").rename(
    columns={"IBM": "Close_IBM", "WMT": "Close_WMT"}
)
aligned_data

# %%
# Calculate the correlation between IBM and Walmart closing prices
correlation = aligned_data["Close_IBM"].corr(aligned_data["Close_WMT"])
correlation

# %%
# Plot scatter plot for visual correlation
plt.figure(figsize=(10, 5))
plt.scatter(aligned_data["Close_IBM"], aligned_data["Close_WMT"])
plt.xlabel("IBM Closing Price")
plt.ylabel("Walmart Closing Price")
plt.title(f"Correlation between IBM and Walmart Prices: {correlation:.2f}")
plt.show()

# %%
# Correlation of daily returns: two trending price series can look correlated just
# because both drift over time, so we also compare their day-to-day changes
daily_returns = aligned_data.pct_change().dropna()
returns_correlation = daily_returns["Close_IBM"].corr(daily_returns["Close_WMT"])
returns_correlation

# %% [markdown]
# ### Tarea 2. Descomposición y autocorrelación

# %%
# Step 3: Time Series Decomposition
# Decompose both time series and plot
# period=252: the index only has trading days, about 252 per year (not 365)
for stock_data, name in zip([ibm_data, walmart_data], ["IBM", "Walmart"]):
    decomposed = seasonal_decompose(stock_data["Close"], model="additive", period=252)
    decomposed.plot()
    plt.suptitle(f"{name} Stock Price Decomposition")
    plt.show()

# %%
# Plot correlograms for both IBM and Walmart stock prices
for stock_data, name in zip([ibm_data, walmart_data], ["IBM", "Walmart"]):
    plt.figure(figsize=(10, 5))
    plot_acf(stock_data["Close"].dropna(), lags=40)
    plt.title(f"{name} Autocorrelation Plot")
    plt.show()


# %% [markdown]
# ### Tarea 3. Prueba de estacionariedad de Dickey–Fuller

# %%
# Step 4: Dickey-Fuller Test for stationarity
def adf_test(series, name):
    result = adfuller(series)
    print(f"ADF Statistic for {name}: {result[0]}")
    print(f"p-value for {name}: {result[1]}")
    if result[1] < 0.05:
        print(f"The {name} series is stationary.")
    else:
        print(f"The {name} series is not stationary.")


# %%
adf_test(ibm_data["Close"], "IBM")
adf_test(walmart_data["Close"], "Walmart")

# %% [markdown]
# ### Tarea 4. Promedio móvil de 30 días

# %%
# Step 5: Moving Average Analysis
# Calculate 30-day moving average for both stocks
for stock_data, name in zip([ibm_data, walmart_data], ["IBM", "Walmart"]):
    stock_data["30_day_MA"] = stock_data["Close"].rolling(window=30).mean()

    # Plot original and moving average prices
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data["Close"], label=f"{name} Close Price")
    plt.plot(stock_data["30_day_MA"], label="30-Day Moving Average", linestyle="--")
    plt.title(f"{name} Close Price and 30-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# %% [markdown]
# ### Tarea 5. Pronóstico a un día

# %%
# Step 6: One-Day Forecast (simple projection using last moving average value)
# For simplicity, we use the last available 30-day moving average as the forecast
for stock_data, name in zip([ibm_data, walmart_data], ["IBM", "Walmart"]):
    last_moving_avg = stock_data["30_day_MA"].iloc[-1]
    print(
        f"One-day forecast for {name} based on the 30-day moving average: {last_moving_avg}"
    )

# %% [markdown]
# **Revisión posterior (2026-10):** se añadió la correlación de los rendimientos diarios, además de la de los precios, y la descomposición estacional usa `period=252` (días hábiles por año) en lugar de 365, porque la serie solo tiene días de negociación. Al re-ejecutar, yfinance devuelve precios `Close` ya ajustados (`auto_adjust`), así que las cifras difieren de la versión entregada: la correlación de precios pasa de 0.25 a 0.67 (la de rendimientos es 0.32) y la prueba ADF ya no rechaza la raíz unitaria para IBM. El PDF conserva la versión entregada.
