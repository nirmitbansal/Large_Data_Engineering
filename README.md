**🚀 Large-Scale Data Engineering Pipeline  **  
⚙️ Scalable ETL for Massive Datasets (45M+ Rows)

💡 *Designed to demonstrate real-world data engineering skills with performance, scalability, and production thinking.*

**✨ Project Highlights**

🔹Handles very large datasets (~45 million rows)  
🔹Memory-efficient chunked ingestion  
🔹Resume-safe ETL (restart without data loss)  
🔹Optimized MySQL storage strategy  
🔹Analytics-ready CSV export for BI tools

**📌 Project Overview**

This project demonstrates a production-style data engineering pipeline built using Python and MySQL, focusing on efficient ingestion, transformation, storage, and export of large-scale tabular data.

🎯 The primary goal is to show how big data can be processed reliably on limited resources using smart engineering decisions.

**🏗️ Architecture & Workflow**

📁 Raw Large Dataset (45M Rows)
⬇️
⚙️ Python Chunked ETL (Resume-Safe)
⬇️
🗄️ MySQL Staging Tables (MyISAM)
⬇️
📊 Partitioned Fact Table (InnoDB)
⬇️
📤 CSV Export → Analytics / BI

**🧠 Key Engineering Concepts Applied**

✔️ Chunk-based data ingestion to avoid memory overflow  
✔️ Progress tracking to support ETL recovery  
✔️ Null & missing value handling  
✔️ High-speed staging using MyISAM 
✔️ Analytics-optimized InnoDB fact tables  
✔️ Batched inserts for performance  
✔️ Streaming exports for large datasets 
