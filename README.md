# Large-Scale Data Engineering Pipeline (Python + MySQL)

## Overview
This project demonstrates an end-to-end **data engineering pipeline** built on a very large real-world dataset (~45 million rows).  
The pipeline covers ingestion, staging, transformation, storage optimization, and export for analytics using **Python and MySQL**.

Due to local storage constraints, the pipeline promotes a **representative batch (~1 million rows)** into an analytics-ready fact table.  
The architecture is designed to scale to full data volume in production environments.

---

## Architecture

Raw Dataset (Text Files, ~45M rows)  
→ Python Chunked ETL (Resume-Safe)  
→ MySQL Staging Table (MyISAM)  
→ MySQL Fact Table (InnoDB, Partitioned)  
→ CSV Export for Analytics / BI Tools  

---

## Technologies Used

- **Python**
  - pandas
  - pymysql
  - tqdm
- **MySQL 8**
- **Git & GitHub**

---

## Dataset

- Source: Display Advertising / Click Prediction dataset (tab-separated text)
- Size: ~45 million rows (raw)
- Columns:
  - `label` (binary target)
  - `feature1` – `feature13` (numerical features)

### Exported Sample
- A **1 million row CSV export** from the final fact table is included **for reference and analytics**
- File represents **Batch 1** only
- Full dataset is excluded to keep the repository lightweight

---

## Key Engineering Features

- Chunked ingestion for large datasets
- Resume-safe ETL using progress tracking
- Handling of missing values (NaN → NULL)
- Use of **MyISAM** for high-volume staging
- Batched inserts into **InnoDB** to avoid undo log overflow
- Partitioned fact table for analytical workloads
- Streaming export to CSV (low memory usage)

---

## Database Design

### Staging Table
- Engine: `MyISAM`
- Purpose: High-throughput raw ingestion

### Fact Table
- Engine: `InnoDB`
- Partitioned by `YEAR(load_date)`
- Composite primary key for partition compatibility
- Optimized for analytics and downstream consumption
