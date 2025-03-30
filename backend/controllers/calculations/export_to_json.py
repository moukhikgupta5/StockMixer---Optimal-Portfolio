import pandas as pd
import json
import numpy as np
# df = pd.read_csv('companies.csv', encoding='latin-1')

# # columns_to_remove = ["Country","Category Name",'Exchange','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12']
# columns_to_remove = ["Name","Country","Category Name",'Exchange','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12']

# # Remove the specified columns
# df = df.drop(columns=columns_to_remove)
# df.replace(np.nan, 'Not available', inplace=True)
# print(df.head())
# print(df["Ticker"].values.tolist())
# json_records = df.to_dict(orient="records")

# # Specify the output JSON file
# output_file = "../../../frontend/src/companies.json"

# # Write the list of JSON records to the output file
# with open(output_file, "w") as f:
#     json.dump(json_records, f, indent=4)
# df.to_json("companies.json", orient="records", lines=True)

with open("companies.json", "r") as compData:
    data = json.load(compData)

comp=dict()
for item in data:
    if item["Name"] not in comp:
        comp[item["Name"]] = item["Ticker"]

processed_data = [
    {"value": val, "label": key}
    for key, val in comp.items() 
]
# print(len(processed_data))
# for i in processed_data:
#     if ".NS" in i["value"]:
#         i["label"] = i["label"] + " NSE"
#     elif ".BO" in i["value"]:
#         i["label"] = i["label"] + " BSE"
with open('output.json', 'w') as file:
    json.dump(processed_data, file, indent=4)