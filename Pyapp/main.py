import random
import os
import json
from threading import Thread
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import subprocess
import sqlite3


dbConn = None


def store_server(ipAll):

        text=''
        version=''
        online = -1
        favicon= ''
        status = ipAll['ports'][0]
        statusmc = json.loads(status['service']['banner'])
        if 'description' in statusmc:
            text = str(statusmc['description'])

        if 'version' in statusmc:
            version = str(statusmc['version']['name'])
        
        if 'favicon' in statusmc:
            favicon = statusmc['favicon']


        if 'players' in statusmc:
            online = statusmc['players']['online']
            if 'sample' in statusmc['players']:
                for player in statusmc['players']['sample']:
                    ptab = (
                            player['id'],
                            player['name'],
                            ipAll['ip']
                            )
                    add_player(ptab)
                    print(ptab)

        server = (
                ipAll['ip'],
                status['port'],
                version,
                text,
                online,
                favicon,
                status['service']['banner']
                )
        add_server(server)
        print(server)

        #print(f"Server {ipAll['ip']} is stored")

def add_server(server):
    global dbConn
    sql = ''' INSERT INTO server(ip,port,version,text,online,favicon,raw)
                VALUES(?,?,?,?,?,?,?) '''
    cur = dbConn.cursor()
    cur.execute(sql, server)
    dbConn.commit()


def add_player(player):
    global dbConn
    sql = ''' INSERT INTO player(uuid,name,server)
                VALUES(?,?,?) '''
    cur = dbConn.cursor()
    cur.execute(sql, player)
    dbConn.commit()


def create_connection(dbfile):
    global dbConn
    try:
        dbConn = sqlite3.connect(dbfile,check_same_thread = False)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    


def set_tables(dbfile):
    global dbConn
    sql_create_server_table = """ CREATE TABLE IF NOT EXISTS server (
                                        ip text PRIMARY KEY,
                                        port integer NOT NULL,
                                        version text,
                                        text text,
                                        online integer,
                                        favicon text,
                                        raw text
                                        ); """
    sql_create_player_table = """ CREATE TABLE IF NOT EXISTS player (
                                        id integer PRIMARY KEY,
                                        uuid text NOT NULL,
                                        name text NOT NULL,
                                        server text NOT NULL
                                        ); """
    c = dbConn.cursor()
    c.execute(sql_create_server_table)
    c.execute(sql_create_player_table)
    dbConn.commit()

def scan(iprange,nbstart):
    # Create a new scanner
    for ip in iprange:
        try:

            print(f"{ip} scanning")
            result = subprocess.Popen([f'masscan -oJ - {ip} --banners -p25565 --wait 3 --rate=500 --adapter-port 25565','&'],stdout=subprocess.PIPE,shell=True)
            stdout = result.communicate()[0]
            #print(stdout)
            if stdout != b'':
               # print(stdout)
                resultados = json.loads(stdout)
               # print(resultados)
                for ips in resultados:
                    PortIps = ips['ports']
                    if 'service' in PortIps[0] and PortIps[0]['service']['name']=='minecraft':
                        #print(f"{PortIps[0]['service']}")
                        store_server(ips)
                       #print(f"{PortIps[0]['service']['banner'][0]['description']}")
                       #print(f"{PortIps[0]['service']['banner'][0]['version']}")






            #masscan -oJ - {ip} --banners -p25565 --wait 3 --rate=1000 --adapter-port 25565


            #if not empty ,trim the result by 34 characters on the left

            #if len(result) > 0:
               # result = result[0].split("\n")
                #now we have an array of string, now for each string , we will trim 34 characters of the left
               # for i in range(len(result)):
                   # result[i]=result[i][34:]
                    #remove the \n at the end of the string
                   # result[i]=result[i][:-1]
                    #replace the space by nothing
                   # result[i]=result[i].replace(" ","")


               # result.pop()
                #print(f"{ip} scanning is done")
                #print(result)
               # for ip in result:
                   # print(f"{ip}:25565")
                   # get_server_info.send_with_options(args=(ip), delay=5000)

            #else:
             #   print(f"{ip} scanning is done")
              #  print("No server found")



            #print(f"{ip} scanning is done")

            #print(result)



            #scanner = masscan.PortScanner()
            #print(f"Scanning {ip}")
            #scanner.scan(ip, ports='25565', arguments='--rate=1000')
            #print(f"Scanning {ip} with thread number {nbstart} is done")
            #result=json.loads(scanner.scan_result)
            #print(result)

            #if not empty
           # for ip in result:
           #    host=result[ip]
             #   print(f"{ip}:25565")
                    #get_server_info.send_with_options(args=(ip,MongoClient), delay=5000)

        except Exception as e:
            print(f"{ip} failed to scan : {e}")

    print(f"Scanning thread number {nbstart} is done")
    print(f"----------------")
    print(f"|{nbstart}|254|")
    print(f"----------------")







async def main():

    create_connection("./sqlitebrowser/MinecraftDB.db")
    set_tables("./sqlitebrowser/MinecraftDB.db")

    IPa = list(range(1,0xff))
    IPb = list(range(1,0xff))

    random.shuffle(IPa)
    random.shuffle(IPb)
    rangeIP = []

    for A in IPa:
        for B in IPb:
           rangeIP.append(f"{A}.{B}.0.0/16")


    random.shuffle(rangeIP)


    #divide the rangeIP into 254
    rangeIP = [rangeIP[i:i + 254] for i in range(0, len(rangeIP), 254)]


    with ThreadPoolExecutor(max_workers=16) as executor:
        for i in range(len(rangeIP)):

            executor.submit(scan, rangeIP[i],i)


if __name__ == "__main__":
   asyncio.run(main())
   #example for me :
   # myclient = pymongo.MongoClient('mongodb://mongodb:27017')
   # mydb = myclient["MinecraftServer"]

       #create a collection
   # mycol = mydb["server"]
   # mydict = {"name": "John", "address": "Highway 37"}
   # x = mycol.insert_one(mydict)
   # print(x.inserted_id) 
