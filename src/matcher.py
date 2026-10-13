"""Synthetic portfolio matching logic, independent of employer database schemas."""
import pandas as pd

COLUMNS = ['customer_name', 'email', 'spz', 'offense_datetime', 'amount', 'offense_type', 'file']

def match_fines_to_orders(fines: pd.DataFrame, rentals: pd.DataFrame):
    """Assign the latest preceding rental of the same vehicle, per demonstration rule."""
    matched, unmatched = [], []
    for _, fine in fines.iterrows():
        eligible = rentals.loc[
            (rentals['spz'] == fine['spz']) &
            (rentals['rentstartdatetime'] <= fine['offense_datetime'])
        ]
        if eligible.empty:
            unmatched.append(fine.to_dict())
            continue
        rental = eligible.sort_values('rentstartdatetime', ascending=False).iloc[0]
        matched.append({
            'customer_name': f"{rental['first_name']} {rental['last_name']}",
            'email': rental['email'], 'spz': fine['spz'],
            'offense_datetime': fine['offense_datetime'], 'amount': fine['amount'],
            'offense_type': fine['offense_type'], 'file': fine['file']
        })
    return pd.DataFrame(matched, columns=COLUMNS), pd.DataFrame(unmatched)
