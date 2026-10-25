"""Grouped summaries."""
import pandas as pd


def summarize_group(data: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Summarize sales for each group.

    purchases:          number of rows (one product on one order)
    quantity_sold:      total number of items sold
    total_sales:        total dollars of sales
    avg_sale:           average dollars per purchase
    pct_of_total_sales: this group's share of all sales, in percent

    Sorted by total_sales, highest first.
    """
    if group_col not in data.columns:
        raise ValueError(f"data must contain a '{group_col}' column")
    out = (
        data.groupby(group_col)
        .agg(
            purchases=("order_id", "size"),
            quantity_sold=("quantity_ordered", "sum"),
            total_sales=("sales", "sum"),
            avg_sale=("sales", "mean"),
        )
        .sort_values("total_sales", ascending=False)
        .reset_index()
    )
    out["pct_of_total_sales"] = (out["total_sales"] / out["total_sales"].sum()).round(3)
    return out


def summarize_numeric(data: pd.DataFrame, column: str) -> pd.Series:
    """Return the mean, median, min and max of a numeric column, rounded to 2 decimals."""
    if column not in data.columns:
        raise ValueError(f"data must contain a '{column}' column")
    return data[column].agg(["mean", "median", "min", "max"]).round(2)