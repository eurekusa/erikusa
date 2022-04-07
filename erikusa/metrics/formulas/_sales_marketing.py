import numpy as np 
def _cagr(
    begin=None,
    final=None,
    t=None,
    ):
    if t<1:
        raise ValueError(
            f"The timeframe could not be {t}"
        )
    try:
        return (begin/end)**(1/t)-1
    except:
        return np.NaN

def _growth(
    begin=None,
    final=None
    ):
    try:
        return (final-begin)/begin
    except:
        return np.NaN

def _evolution_index(
    brand=None,
    market=None,
    percent=True
    ):
    try:
        if percent:
            return (brand+100)/(market+100)
        else:
            return ((brand*100)+100)/((market*100)+100)
    except:
        return np.NaN
def _irr(cashflows=None):
    return np.irr(cashflows)
