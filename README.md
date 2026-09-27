# Just Now Building Cleaning

## Apps

- `app/quote.html` – example instant-quote calculator. Customers pick a service, enter the floor area, bathrooms, frequency and extras, and see a price estimate with a breakdown. Prices are sample values set at the top of the script (`SERVICES`, `EXTRAS`, `DISCOUNT`, `MIN_PRICE`, `CURRENCY`).

## Supervisor

- `supervisor/` – the all-day supervisor for the respond.io AI agent: the owner's standing orders, how each conversation is judged, the scheduled runs (every 10 minutes, nightly, escalation) and the helper scripts they use. See `supervisor/README.md`.
