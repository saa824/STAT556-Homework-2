"""Reusable cleaning functions for the ExpressMart orders data."""
import pandas as pd


def clean_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with lowercase column names without spaces ."""
    out = data.copy()
    out.columns = out.columns.str.strip().str.lower().str.replace(" ", "_")
    return out


def add_location(data: pd.DataFrame) -> pd.DataFrame:
    """Add city, state and city_state columns parsed from purchase_address."""
    out = data.copy()
    parts = out["purchase_address"].str.split(",", expand=True)
    out["city"] = parts[1].str.strip()
    out["state"] = parts[2].str.strip().str.split().str[0]
    out["city_state"] = out["city"] + ", " + out["state"]
    return out


def drop_exact_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """Return a copy without rows that are identical in every column."""
    return data.drop_duplicates().reset_index(drop=True)


def parse_order_datetime(data: pd.DataFrame) -> pd.DataFrame:
    """Convert Excel serial dates and day-fraction times into a datetime.

    Expects 'order_date' (days since 1899-12-30) and 'time' (fraction of a day).
    Adds 'order_datetime', 'month' and 'hour', and drops the two raw columns.
    """
    out = data.copy()
    date = pd.to_datetime(out["order_date"], unit="D", origin="1899-12-30")
    seconds = (out["time"] * 86400).round().astype(int)
    out["order_datetime"] = date + pd.to_timedelta(seconds, unit="s")
    out["month"] = out["order_datetime"].dt.month
    out["hour"] = out["order_datetime"].dt.hour
    return out.drop(columns=["order_date", "time"])   


def filter_year(data, year=2019):
    """Return only the rows whose order_datetime falls in the given year."""
    return data[data["order_datetime"].dt.year == year].reset_index(drop=True) 


def clean_raw_data(raw):
    """Run the full cleaning pipeline on the raw orders table."""
    return (
        raw
        .pipe(clean_column_names)
        .pipe(parse_order_datetime)
        .pipe(filter_year)
        .pipe(add_location)
        .pipe(drop_exact_duplicates)
    )