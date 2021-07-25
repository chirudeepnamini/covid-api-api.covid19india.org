from pymongo import MongoClient
import dns,os
from fastapi import FastAPI
app = FastAPI()
client =MongoClient(os.environ['MONGO_URI'])
db=client['covid_data']
@app.get("/state-data/{date}")
async def data_getter(date:str):
    coll1=db['Statedata_datewise']
    Results=list(coll1.find({"Date_YMD":date}))
    if len(Results)==0:
        return {"Error":"Data not found--check your date and its format(should be yyyy-mm-dd)"}
    Confirmed_dict={k:v for k,v in Results[0].items() if k!='_id' and k!='Date'and k!='Date_YMD' and k!='Status'}
    Recovered_dict={k:v for k,v in Results[1].items() if k!='_id' and k!='Date'and k!='Date_YMD' and k!='Status'}
    Deceased_dict={k:v for k,v in Results[1].items() if k!='_id' and k!='Date'and k!='Date_YMD' and k!='Status'}
    return({'Date':Results[0]['Date_YMD'],
    'Confirmed':Confirmed_dict,
    'Recovered':Recovered_dict,
    'Deceased':Deceased_dict})
@app.get("/total-data/{date}")
async def total_data_getter(date:str):
    coll2=db['Totaldata_datewise']
    Results=list(coll2.find({"Date_YMD":date}))
    if len(Results)==0:
        return {"Error":"Data not found--check your date and its format(should be yyyy-mm-dd)"}
    print(Results[0])
    # print(Results[0])
    return({
        'Date':Results[0]['Date'],
        'Confirmed':Results[0]['Daily Confirmed'],
        'Recovered':Results[0]['Daily Recovered'],
        'Deceased':Results[0]['Daily Deceased'],
        'Total Confirmed':Results[0]['Total Confirmed'],
        'Total Recovered':Results[0]['Total Recovered'],
        'Total Deceased':Results[0]['Total Deceased']
    })