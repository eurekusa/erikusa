from .formulas import _cagr, _growth, _evolution_index
from ._metrics_helper import build_dataframe
def cagr(
    data=None,
    begin=None,
    final=None,
    t=None,
    fill=None
    ):
    if not isinstance(t, int):
        raise ValueError(
            "The timeframe could must be a postive int."
        )
    args={
    'x':begin,
    'y':final,
    'x_col':'begin',
    'y_col':'final',
    'data_frame':data
    }
    input_data=build_dataframe(args)
    output_data=input_data.apply(lambda row: _cagr(begin=row['begin'],final=row['final'],t=t),axis=1)
    if fill is not None:
        output_data.fillna(value=fill,inplace=True)
    return output_data
def growth(
    data=None,
    begin=None,
    final=None,
    fill=None
    ):
    args={
    'x':begin,
    'y':final,
    'x_col':'begin',
    'y_col':'final',
    'data_frame':data
    }
    input_data=build_dataframe(args)
    output_data=input_data.apply(lambda row: _growth(begin=row['begin'],final=row['final']),axis=1)
    if fill is not None:
        output_data.fillna(value=fill,inplace=True)
    return output_data
def evolution_index(
    data=None,
    brand=None,
    market=None,
    percent=True,
    fill=None
    ):
    args={
    'x':brand,
    'y':market,
    'x_col':'brand',
    'y_col':'market',
    'data_frame':data
    }
    input_data=build_dataframe(args)
    output_data=input_data.apply(lambda row: _evolution_index(brand=row['brand'],market=row['market']),axis=1)
    if fill is not None:
        output_data.fillna(value=fill,inplace=True)
    return output_data
