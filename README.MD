# 0xScan

A simple Python scanner that is designed to scan Minecraft servers using a Masscan fork.

> :warning: **Warning:** First of all, please use this on a VPS, You really don't want to be banned from certain part of the Internet.


## Features

- Will scan 16 ip ranges each time in parallel
- Have a speed of around 1k packets per second per ip range so you can count around 16k packets per second
- The docker-compose have sqlitebrowser so you can see your database on <your_domain/ip>:3000, you'll just need to click on open database then select MinecraftDB.db

## Notes

This scanner is mostly made for fun. If you want to scan servers : you should do it at your own risk and don't do it on your own computer, you really don't want to be banned from parts of the internet / have your internet provider cutting off your internet access.
And also you should try to make your own scanner, by using Masscan (or any scanner) and wrap it or create your own implementation.

## To-do list

there are a few things I want to do / improve before saying that this projet is "done" :

- [ ] Improve the database (using MongoDB)
- [ ] create an API
- [ ] create another program that will check every server it found and scan them more frequently
- [ ] detect if the server have a whitelist
- [ ] same but if it is in offline mode

## Usage

I assume that you have the basics about server scanning (I recommend the [Minecraft serie made by Liveoverflow](https://www.youtube.com/watch?v=VIy_YbfAKqo) if not, they explain the basics about a simple server scanner)

First of all, you'll need to write that in your terminal 
```
iptables -A INPUT -p tcp --dport 25565 -j DROP
```
It's really important or else you'll not be able to receive any Minecraft banner from Masscan.

If done correctly you just need to launch the docker-compose, it can be easily done by writing this command in your terminal :
`docker-compose up -d --build` it will launch the docker-compose in detach mode.

If everything is working , you just need to go on your browser and type `<your_domain/ip>:3000`, then you'll just need to click on "Open Database" and click on your database (it should be MinecraftDB.db)


## Screenshots

![Image of the servers](https://i.imgur.com/jVkp4fM.png)
*Screenshot of some servers that are in the database*

![Image of the players](https://i.imgur.com/CGvCGX8.png)
*Screenshot of some players that are in the database*


## Credits

Thanks to [LiveOverflow](https://www.youtube.com/@LiveOverflow/) who gave me the idea of making a minecraft server scanner, his series on Minecraft really helped sparkling the idea of making a scanner and coding Minecraft hacks for fun on the other hand.
This project was also made so I could join their server as it was the "only" way to find the server.
Sadly there is a whitelist made out of bots so I can't join the server.\
Also Thanks to [Matdoesdev](https://matdoes.dev/) who really made me want to make a somewhat serious projet thanks to their blog, it has gave me a look on what can be done with this project and some of their other projects gave me new ideas.