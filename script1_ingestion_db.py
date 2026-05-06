from sqlalchemy import create_engine
import pandas as pd
import os
import logging
import time

def ingest_db(df, table_name, engine):
    '''Ingest dataframe into database'''
    df.to_sql(table_name, con= engine, if_exists= "replace", index= False, method ="multi" )

def load_data():
    '''Load the CSVs as pandas dataframe and ingest into database'''
    Stime = time.time()
    for file in os.listdir("Data"):
        if file.endswith(".csv"):
            table_name = file[:-4]
            df = pd.read_csv("Data/"+file)
            logging.info(f"Ingesting CSV: {table_name}; Shape: {df.shape}; Database: {db_name}")
            ingest_db(df, table_name, conn) # Comment this line if you just want to check
    Etime = time.time()
    logging.info(f"|----------------------Ingestion Complete----------------------|")
    logging.info(f"Time Elapsed: {round((Etime - Stime)/60,3)} min")

if __name__ == "__main__":

    # Keeps logs
    logging.basicConfig(
        filename= "Logs/ingestion_db.log",
        level= logging.DEBUG,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        filemode= "a"
    )

    # Connect to Database
    db_name = "vendoranalysis"
    engine = create_engine(f"mysql+pymysql://root:Sourin@123@localhost/{db_name}")
    conn = engine.connect()
    logging.info(f"Connected to database {db_name}")

    # Starts script
    load_data()