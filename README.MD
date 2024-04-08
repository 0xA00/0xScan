# 0xScan

A simple Python scanner designed to scan Minecraft servers using a fork of Masscan.

> :warning: **Warning:** First of all, please use this on a VPS. You really don't want to be banned from certain parts of the Internet.


## Features

- It will scan 16 IP ranges simultaneously each time
- It should have a speed of around 1k packets per second per IP range, so you can expect approximately 16k packets per second in total.
- The docker-compose includes SQLiteBrowser, allowing you to view your database at <your_domain/ip>:3000. You'll just need to click on 'Open Database' and then select 'MinecraftDB.db'

## Notes

This scanner is primarily created for amusement. If you decide to scan servers, please be aware that you do so at your own risk. Avoid conducting scans on your personal computer as you risk being banned from certain parts of the internet or having your internet access cut off by your provider. Additionally, consider developing your own scanner by leveraging tools like Masscan (or any other scanner) and either wrapping it or creating your own implementation.

## To-do list

There are a few things I want to do/improve before considering this project 'done':

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

Thanks to [LiveOverflow](https://www.youtube.com/@LiveOverflow/) who gave me the idea of making a minecraft server scanner, his series on Minecraft really helped spark the idea of making a scanner and coding Minecraft hacks for fun on the other hand.
This project was also made so I could join their server as it was the "only" way to find the server.
Sadly now there is a whitelist made out of bots so I can't join the server.\
Also Thanks to [Matdoesdev](https://matdoes.dev/) who really made me want to make a somewhat serious projet thanks to their blog, it has given me a look on what can be done with this project and some of their other projects gave me new ideas.
