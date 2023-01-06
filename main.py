from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database_connect import connect_al, connect_pg2, connect_pg2_1
import uvicorn


app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/healthcheck")
def read_root():
  try:
    con1 = connect_pg2_1()
    con2 = connect_pg2()
    con3 = connect_al()
    return {"conn1": con1, "conn2": con2, "conn3": con3}
  except Exception as e:
    return {'status': 'Not ok', 'message': str(e)}