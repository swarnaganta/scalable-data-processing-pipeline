# Scalable Data Processing Pipeline

A high-performance Python-based pipeline to process and analyze large CSV datasets.  
Optimized with **multiprocessing** for parallel execution and **Pandas** for efficient data manipulation.

## Features
- Processes datasets with over 1M+ records
- Parallel processing for faster execution
- Chunk-based reading to save memory
- Generates summary analytics by region

## Tech Stack
- Python
- Pandas
- Multiprocessing

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scalable-data-processing-pipeline.git
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python pipeline.py
   ```

## Sample Output
`claims_summary.csv` showing total claim amounts per region.

## Example Dataset
The `insurance_data.csv` file contains:
```
CustomerID,Region,ClaimAmount,PolicyType
1,North,6000,Health
2,South,4500,Auto
...
```
