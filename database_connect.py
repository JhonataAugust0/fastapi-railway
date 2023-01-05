#!/usr/bin/python
import psycopg2
from sqlalchemy import create_engine

def connect_pg2_1():
  """ Connect to the PostgreSQL database server """
  print('connect_pg2_1', flush=True)
  conn = None
  try:
    
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...',flush=True)
    conn = psycopg2.connect(database="railway",
                          host="containers-us-west-126.railway.app",
                          user="postgres",
                          password="yT260YQ7LT1ULIol5jr0",
                          port="8013")
    # create a cursor
    cur = conn.cursor()
        
	# execute a statement
    print('PostgreSQL database version:',flush=True)
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version,flush=True)
       
	# close the communication with the PostgreSQL
    cur.close()
  
  except (Exception, psycopg2.DatabaseError) as error:
    print(error,flush=True)
  
  finally:
    
    if conn is not None:
      conn.close()
      print('Database connection closed.',flush=True)
      return True


def connect_pg2():
  print('connect_pg2', flush=True)
  conn = psycopg2.connect(database="railway",
                          host="containers-us-west-126.railway.app",
                          user="postgres",
                          password="yT260YQ7LT1ULIol5jr0",
                          port="8013",
                          keepalives=1,
                          keepalives_idle=30,
                          keepalives_interval=10,
                          keepalives_count=5)
  return True


def connect_al():
  print('connect_al', flush=True)
  # conexao_pg = create_engine('postgresql://postgres:YfVyRn1ly6u4NBF@213.188.198.194/postgres').connect()
  # conexao_pg = create_engine('postgresql+psycopg2://postgres:YfVyRn1ly6u4NBF@213.188.198.194:5432/postgres',
  #             pool_pre_ping=True, 
  #             pool_recycle=3600, 
  #             connect_args={
  #               "keepalives": 1,
  #               "keepalives_idle": 30,
  #               "keepalives_interval": 10,
  #               "keepalives_count": 5,
  #             }).connect()
  conexao_pg = create_engine('postgresql://postgres:yT260YQ7LT1ULIol5jr0@containers-us-west-126.railway.app:8013/railway').connect()
  return True