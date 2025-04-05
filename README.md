# Memecoin Valuation Reference System

**Version**: 1.0  
**Author**: Norman 
**Date**: April 5, 2025  
**Repository**: [`https://github.com/EnbangWu/memecoin-analyzer`]

## Overview

This project automates the scanning of memecoins launched daily on [Pump.fun](https://pump.fun), identifies the top 3 tokens by market capitalization after 1 day and 1 week, and collects key metrics (market cap, holder count, 24-hour trading volume, and narrative). The data is stored in a local database, creating a dynamic valuation reference system for memecoin trading decisions.

### Goals
- Scan ≥90% of Pump.fun’s daily token launches with ≤6-hour delay.
- Rank top 3 tokens by market cap for 1-day and 1-week periods.
- Store metrics and narratives in a queryable database (~1M records).
- Provide basic visualizations (tables, charts) and optional growth alerts.

### Scope
- **In Scope**: Pump.fun token data, market cap, holders, volume, narratives, local database.
- **Out of Scope**: Other platforms (e.g., SunPump), automated trading, predictive analytics.

## Features

| Feature              | Description                                          | Priority     |
|----------------------|------------------------------------------------------|--------------|
| **Data Collection**  | Scan Pump.fun for new tokens daily                    | Must-Have    |
| **Top Token Ranking**| Rank top 3 tokens by market cap (1-day, 1-week)      | Must-Have    |
| **Narrative Analysis**| Tag tokens with narratives (e.g., "AI," "dog")        | Should-Have  |
| **Database**         | Store and query token data locally                   | Must-Have    |
| **Visualization**    | Display rankings/trends in tables/charts             | Should-Have  |
| **Alerts**           | Notify on rapid market cap growth (e.g., Telegram)   | Nice-to-Have |

### Example Output
```json
[
  {
    "name": "CHILLGUY",
    "address": "0x123...",
    "market_cap": 1000000,
    "holders": 500,
    "volume_24h": 200000,
    "narrative": "dog",
    "period": "1-day"
  }
]