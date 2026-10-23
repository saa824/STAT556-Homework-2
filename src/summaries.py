"""Grouped summaries."""
import pandas as pd


def summarize_group(data: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Return line count, units, revenue and mean line value per group.

    Sorted by revenue, highest first.
    """
    if group_col not in data.columns:
        raise ValueError(f"data must contain a '{group_col}' column")
    return (
        data.groupby(group_col)
        .agg(
            n_lines=("order_id", "size"),
            units=("quantity_ordered", "sum"),
            revenue=("sales", "sum"),
            mean_line_value=("sales", "mean"),
        )
        .sort_values("revenue", ascending=False)
        .reset_index()
    )