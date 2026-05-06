# **IMP** Go to EDA.ipynb for a better understanding of this script

from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import logging
from script1_ingestion_db import ingest_db
import time

def create_vendor_summary(conn):
    '''Merge different tables and get relevant data'''
    
    vendor_sales_summary = pd.read_sql('''WITH FreightSummary AS(
                                SELECT
                                    VendorNumber,
                                    SUM(Freight) AS TotalFreightCost
                                FROM vendor_invoice
                                GROUP BY VendorNumber),
                                
                                PurchaseSummary AS(
                                SELECT
                                    p.VendorNumber,
                                    p.VendorName,
                                    p.Brand,
                                    p.Description,
                                    p.PurchasePrice,
                                    pp.Price as SellingPrice,
                                    pp.Volume,
                                    SUM(p.Quantity) AS TotalPurchaseQuantity,
                                    SUM(p.Dollars) AS  TotalPurchaseDollars
                                FROM purchases p INNER JOIN purchase_prices pp
                                ON p.Brand = pp.Brand
                                WHERE p.PurchasePrice > 0
                                GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, SellingPrice, pp.Volume),
                                
                                SalesSummary AS(
                                SELECT
                                    VendorNo,
                                    Brand,
                                    SUM(SalesQuantity) AS TotalSalesQuantity,
                                    SUM(SalesDollars) AS TotalSalesDollars,
                                    SUM(SalesPrice) AS TotalSalesPrice,
                                    SUM(ExciseTax) AS TotalExciseTax
                                FROM sales
                                GROUP BY VendorNo, Brand)
                                
                                SELECT
                                    ps.VendorNumber,
                                    ps.VendorName,
                                    ps.Brand,
                                    ps.Description,
                                    ps.PurchasePrice,
                                    ps.SellingPrice,
                                    ps.Volume,
                                    ps.TotalPurchaseQuantity,
                                    ps.TotalPurchaseDollars,
                                    ss.TotalSalesQuantity,
                                    ss.TotalSalesDollars,
                                    ss.TotalSalesPrice,
                                    ss.TotalExciseTax,
                                    fs.TotalFreightCost
                                FROM PurchaseSummary ps LEFT JOIN SalesSummary ss
                                ON ps.VendorNumber = ss.VendorNo
                                AND ps.Brand = ss.Brand
                                LEFT JOIN FreightSummary fs
                                ON ps.VendorNumber = fs.VendorNumber
                                ORDER BY ps.TotalPurchaseDollars DESC''', con= conn)
    return vendor_sales_summary

def clean_data(df):
    '''Clean data and add relevant columns'''

    # Change dtype
    df["Volume"] = df["Volume"].astype("float64")

    # Handle Null values
    df.fillna(0, inplace= True)

    # Handle extra spaces
    df["VendorName"] = df["VendorName"].str.strip()

    # Add relevant new columns
    df["GrossProfit"] = df["TotalSalesDollars"] - df["TotalPurchaseDollars"]
    df["ProfitMargin"] = round((df["GrossProfit"]/df["TotalSalesDollars"])*100,2)
    df["StockTurnover"] = round(df["TotalSalesQuantity"]/df["TotalPurchaseQuantity"],2)
    df["SalesToPurchaseRatio"] = round(df["TotalSalesDollars"]/df["TotalPurchaseDollars"],2)

    # There are some cases of divided by zero which generates np.inf which are not compatible with MySQL,
    # thus we replace those inf with nan
    df.replace([np.inf, -np.inf], np.nan, inplace= True)

    return df

if __name__ == "__main__":
    
    # Keeps logs
    logging.basicConfig(
        filename= "Logs/get_vendor_summary.log",
        level= logging.DEBUG,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        filemode= "a"
    )

    # Create connection
    db_name = "vendoranalysis"
    engine = create_engine(f"mysql+pymysql://root:Sourin@123@localhost/{db_name}")
    conn = engine.connect()
    logging.info(f"Connection established: {db_name}")

    Stime = time.time()
    logging.info("Creating Vendor Summary Table...")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning data...")
    cleaned_df = clean_data(summary_df)
    logging.info(cleaned_df.head())

    logging.info("Ingesting data into database...")
    ingest_db(cleaned_df, "vendor_sales_summary", conn)
    Etime = time.time()
    logging.info(f"|----------------------Ingestion Complete----------------------|")
    logging.info(f"Total Time Elapsed: {round((Etime - Stime)/60,3)} min")