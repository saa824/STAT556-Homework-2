"""Executable checks on assumptions about the cleaned data."""
import pandas as pd


def validate_orders(data: pd.DataFrame) -> None:
    """Raise AssertionError if the cleaned orders break an expected rule."""
    assert not data.isna().any().any(), "unexpected missing values"
    assert (data["quantity_ordered"] > 0).all(), "non-positive quantity"
    assert (data["price_each"] > 0).all(), "non-positive price"
    assert ((data["quantity_ordered"] * data["price_each"] - data["sales"]).abs() < 0.01).all(), "sales != quantity * price"
    assert not data.duplicated().any(), "exact duplicate rows remain"
    assert data["product"].nunique() == 19, "expected 19 products"
    assert data["city_state"].nunique() == 10, "expected 10 city/state locations"
    assert data["order_datetime"].dt.year.eq(2019).all(), "found dates outside 2019"
    assert data["hour"].between(0, 23).all(), "hour out of range"
    assert data["month"].between(1, 12).all(), "month out of range"