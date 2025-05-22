import os
import requests
import geopandas as gpd
import numpy as np


# (1) download the dataset file in the parquet file format directly from zenodo:
# (feel free to change the download location following the --output parameter)
# Create directory for data and subdirectories if not already existent
#os.makedirs("data/large_data", exist_ok=True)
#!curl https://zenodo.org/records/10473706/files/LIST_v1-2.parquet --output data/large_data/LIST_v1-2.parquet

data = "data/LIST_v1-2.parquet"

if os.path.exists(data):
    path = data

else:
    print("no data detect")
    path = None

print(path)
# data path is fixed


LIST = gpd.read_parquet(path)
LIST.shape # the number of datas in frame
df_test = LIST.head(5) # data frame
print(df_test)


# textual explorations
LIST_texts = LIST["clean_text_interpretive_word"].tolist()
df_test = LIST_texts[:10]
print(df_test)