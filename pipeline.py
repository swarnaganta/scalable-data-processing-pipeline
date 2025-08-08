import pandas as pd
import multiprocessing as mp
import time

# Function to process each chunk of data
def process_chunk(chunk):
    # Example: filter customers with claims above 5000
    filtered = chunk[chunk['ClaimAmount'] > 5000]
    summary = filtered.groupby('Region')['ClaimAmount'].sum().reset_index()
    return summary

def main():
    start = time.time()
    
    # Read CSV in chunks for large datasets
    chunk_size = 50000
    chunks = pd.read_csv("insurance_data.csv", chunksize=chunk_size)
    
    # Use multiprocessing to handle chunks in parallel
    pool = mp.Pool(mp.cpu_count())
    results = pool.map(process_chunk, chunks)
    
    # Combine results
    final_df = pd.concat(results).groupby('Region').sum().reset_index()
    
    # Save output
    final_df.to_csv("claims_summary.csv", index=False)
    
    print("Processing completed in", round(time.time() - start, 2), "seconds")
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
