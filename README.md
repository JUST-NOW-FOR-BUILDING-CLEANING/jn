# Just Now Building Cleaning

## Apps

- `app/quote.html` – example instant-quote calculator. Customers pick a service, enter the floor area, bathrooms, frequency and extras, and see a price estimate with a breakdown. Prices are sample values set at the top of the script (`SERVICES`, `EXTRAS`, `DISCOUNT`, `MIN_PRICE`, `CURRENCY`).

## Supervisor

- `supervisor/` – the all-day monitoring project for the respond.io AI agent: how each conversation is judged, the instructions for the scheduled checks (every 10 minutes, hourly, nightly, morning apply) and the helper scripts they run. See `supervisor/README.md`.
