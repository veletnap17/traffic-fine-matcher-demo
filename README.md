# Traffic Fine Matcher — Public Demo

A **standalone, synthetic portfolio demonstration** of matching vehicle-related fine records to rentals. It showcases Python/pandas, time-window logic, data joins, and test-driven development without publishing any internal database tables, proprietary SQL, customer records, or real fine documents.

## Business problem

A fine includes a vehicle registration and an incident timestamp. To support review of responsibility, an analyst needs to identify the most recent rental of that same vehicle that **started at or before** the incident. The example intentionally retains this business matching rule even when that rental already ended. The result is a candidate for review, **not a legal determination of responsibility**.

## Run the demonstration

```bash
python -m pip install -r requirements.txt
python -m src.demo
python -m unittest discover -s tests -v
```

The demo reads `demo/fines.csv` and `demo/rentals.csv` and writes `output/matched.csv` and `output/unmatched.csv`. Both input files are entirely invented. No network/API/DB access or credentials are necessary.

## Processing flow

```text
Synthetic fine records + synthetic rental records
                    |
           Python matching rule
                    |
         matched.csv / unmatched.csv
```

## Relation to the original workflow

The original private automation combines PDF text extraction, AI-assisted field parsing, rental lookup and spreadsheet outputs. This deliberately **limited public reconstruction** demonstrates the matching and output portion with neutral data and without copying private integrations or company schema details. It does not claim to process PDFs or call AI/database services.

## Next improvements

Add additional edge-case tests, timezone validation, and a clearly documented review/override process before using such a matcher on sensitive real-world data.
