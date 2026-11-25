# Tasa de cambio fija para el ejemplo (1 USD = 20.00 MXN)
TASA_USD = 20.00

def mxn_a_usd(mxn):
    """Convierte Pesos Mexicanos a Dólares."""
    return mxn / TASA_USD

def usd_a_mxn(usd):
    """Convierte Dólares a Pesos Mexicanos."""
    return usd * TASA_USD

if __name__ == "__main__":
    print("--- Conversor de Divisas (MXN <-> USD) ---")
    print(f"2000 MXN a USD: ${mxn_a_usd(2000):.2f}")
    print(f"100 USD a MXN: ${usd_a_mxn(100):.2f}")
