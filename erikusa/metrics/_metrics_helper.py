from pandas.api.types import is_numeric_dtype
import pandas as pd

def build_dataframe(args, numerical_columns=True):
    """
    Constructs a dataframe and modifies `args` in-place.
    The argument values in `args` can be either strings corresponding to
    existing columns of a dataframe, or data arrays (lists, numpy arrays,
    pandas columns, series).
    Parameters
    ----------
    args : OrderedDict
        arguments passed to the px function and subsequently modified
    constructor : graph_object trace class
        the trace type selected for this figure
    """
    for field in args:
        if field in array_attrables and args[field] is not None:
            args[field] = (
                dict(args[field])
                if isinstance(args[field], dict)
                else list(args[field])
            )

    df_provided = args["data_frame"] is not None
    if df_provided and not isinstance(args["data_frame"], pd.DataFrame):
        args["data_frame"] = pd.DataFrame(args["data_frame"])
    df_input = args["data_frame"]
    if (isinstance(args['x'],str) and isinstance(args['y'],str)):
        if(not df_provided):
            raise ValueError(
                "Missing data parameter."
            )
        else:
            if(args['x'] in df_input.columns) and (args['y'] in df_input.columns):
                args['x']=df_input[args['x']].values
                args['y']=df_input[args['y']].values
            else:
                raise ValueError(
                    "Mentioned columns are not in the dataframe."
                )
    else:
        try:
            args['x']=list(iter(args['x']))
            args['y']=list(iter(args['y']))
        except:
            raise TypeError(
                "When data is not provided, iterable variable must be provided instead."
            )
    if numerical_columns:
        if (is_numeric_dtype(args['x']) and is_numeric_dtype(args['y'])):
            return pd.DataFrame({args['x_col']:args['x'],args['y_col']:args['y']})
        else:
            raise TypeError(
                "Both columns must be of a numerical dtype."
            )
