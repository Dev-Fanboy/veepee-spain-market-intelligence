# Spain Fashion E-Commerce & Circular Economy — Market Intelligence

An end-to-end data analysis of Spain's e-commerce fashion market and circular economy landscape, built on open data from official European and Spanish government sources.

## What This Covers

**Market sizing and trends** — Spain's e-commerce market grew from €40B (2018) to €95.2B (2024). Clothing is consistently the #2-3 sector by revenue and the #1 category for cross-border exports.

**Consumer spending patterns** — 19-year household expenditure series (INE, 2006–2024) showing structural shifts in fashion budget allocation, regional spending disparities across Spain's 17 autonomous communities, and CPI dynamics.

**Circular economy opportunity** — EU textile waste collection rates by country, Spain's 17.9% collection gap vs. EU average (27.5%), secondhand fashion market growth trajectory (€0.8B → €3.8B, 2018–2025), and the impact of EU mandatory separate textile collection starting 2025.

**Forecasting models** — OLS regression with seasonal decomposition for e-commerce revenue projection, scenario analysis for clothing e-commerce (base/optimistic/conservative), and exponential growth model for secondhand market sizing through 2028.

**EU cross-country comparison** — Fashion purchasing power across 20 European countries (NIQ-GfK 2024), positioning Spain as an outlier with the highest fashion share of retail spending (14.8%) despite below-average absolute spend.

## Data Sources

| Source | Data | Format | URL |
|--------|------|--------|-----|
| **CNMC** | Quarterly e-commerce revenue, transactions, sector breakdown, cross-border flows | CSV | [data.cnmc.es](https://data.cnmc.es) / [datos.gob.es](https://datos.gob.es) |
| **INE** | Household Budget Survey — clothing expenditure by year, region, household type | CSV | [ine.es](https://www.ine.es/dyngs/INEbase/en/operacion.htm?c=Estadistica_C&cid=1254736176806) |
| **Eurostat** | Cross-country household consumption | TSV | [ec.europa.eu/eurostat](https://ec.europa.eu/eurostat) |
| **EEA** | Textile waste generation, collection rates, recycling by country (2020 baseline) | Report/annex | [eea.europa.eu](https://www.eea.europa.eu/en/analysis/publications/management-of-used-and-waste-textiles-in-europes-circular-economy) |
| **NIQ-GfK** | Fashion purchasing power per capita, 25 EU countries (2024) | Press release | NIQ-GfK Purchasing Power for Retail Product Lines 2024 |
| **Industry/Press** | Competitive landscape, company KPIs, Re-Cycle timeline | Manual compilation | Various press releases |

All figures are sourced from official open-data portals and published reports. Secondhand market estimates are derived from EEA data and industry analysis (Statista, ThredUp). See `data/DATA_DICTIONARY.json` for field-level documentation and source URLs.

## Datasets (12 total, 177 data points)

| # | File | Rows | Description |
|---|------|------|-------------|
| 1 | `cnmc_ecommerce_quarterly.csv` | 28 | Total e-commerce revenue, transactions, clothing %, YoY growth (2018 Q1–2024 Q4) |
| 2 | `cnmc_ecommerce_sectors.csv` | 24 | Top sectors by revenue share across quarters |
| 3 | `cnmc_crossborder_ecommerce.csv` | 5 | Annual cross-border flows: domestic, Spain→abroad, abroad→Spain (2020–2024) |
| 4 | `ine_household_clothing_expenditure.csv` | 19 | Avg household clothing spend and budget share (2006–2024) |
| 5 | `ine_regional_expenditure_2024.csv` | 17 | Per capita spending by autonomous community |
| 6 | `eea_textile_waste_eu.csv` | 16 | Textile waste and separate collection rates by EU country |
| 7 | `circular_fashion_spain.csv` | 8 | Spain secondhand market size, EU recycling rates (2018–2025) |
| 8 | `spain_fashion_competitors.csv` | 10 | Competitive landscape: model, presence, sustainability, avg ticket |
| 9 | `veepee_kpis.csv` | 7 | Veepee global & Spain KPIs (2018–2024) |
| 10 | `eu_fashion_purchasing_power.csv` | 21 | Fashion spend per capita and % of retail by EU country |
| 11 | `ine_cpi_clothing.csv` | 10 | CPI indices for general and clothing categories (2015–2024) |
| 12 | `circular_economy_metrics.csv` | — | Key EU circular economy indicators |

## Project Structure

```
veepee-spain-market-intelligence/
├── README.md
├── data/
│   ├── DATA_DICTIONARY.json      # Field definitions + source URLs
│   └── processed/                # 12 clean CSV datasets
│       ├── cnmc_ecommerce_quarterly.csv
│       ├── ine_household_clothing_expenditure.csv
│       ├── eea_textile_waste_eu.csv
│       └── ... (9 more)
├── src/
│   ├── build_datasets.py         # Data pipeline — generates all CSVs
│   └── dashboard.jsx             # Interactive React dashboard (Recharts)
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Forecasting Methodology

Three models, all transparent and reproducible:

**1. E-Commerce Revenue Forecast (2025–2026)**
- Method: OLS linear regression with additive seasonal decomposition
- Data: 28 quarterly observations (CNMC, 2018–2024)
- Output: Point forecasts + 95% prediction intervals
- R² ≈ 0.96 on trend component

**2. Clothing E-Commerce Scenarios**
- Method: OLS on post-COVID subset (2021+, n=16) with seasonal adjustment
- Rationale: COVID created a structural break; pre-2020 data represents a different regime
- Scenarios: Base (trend), Optimistic (+15%), Conservative (−15%)

**3. Secondhand Market Sizing**
- Method: Log-linear regression (exponential growth model)
- Data: 8 annual observations (2018–2025)
- Caveat: Exponential models overestimate long-term; projections limited to 2028

**Limitations:** These are simple parametric models suited to the available data. A production system would use SARIMA, Prophet, or gradient-boosted time series with external regressors (inflation, consumer confidence, promotional calendars).

## How to Run

```bash
# Generate datasets from source
python src/build_datasets.py

# Dashboard (React + Recharts)
# The dashboard.jsx file is a standalone React component.
# To run locally, use any React environment or paste into a React sandbox.
```

## Key Findings

1. Spain's e-commerce fashion market reached ~€5.9B in 2024, growing 12–13% YoY
2. Clothing is the #1 cross-border export category from Spain (~10% of outbound e-commerce)
3. Spain has the highest fashion share of retail spending in Europe (14.8%) on below-average budgets — a consumer profile aligned with discount flash-sale models
4. Spain's textile collection rate (17.9%) is well below the EU average (27.5%), creating a supply-side opportunity as EU mandatory collection begins in 2025
5. The secondhand fashion market is growing at ~25% CAGR, projected to reach €5–6B by 2028

## Author

**Michael Akinwumi**
Economics & Data Analysis · Python, SQL, Statistical Modelling

## License

MIT
