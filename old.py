# OLD
# Onion Links Databse 
# Current Version: v0.1
# Michael C. Dimopoulos
# Thessaloniki, Greece 2017
# GNU General Public License v3.0
# Free Software Foundation

############## IMPORTS: ##############

import colorama
from colorama import Fore, Back, Style
import random
import argparse
import sqlite3
import time

#######################################

############### CODE: #################

def search(tag):
	start = time.time()
	conn = sqlite3.connect("old.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM links WHERE tag1 = ? OR tag2 = ? OR tag3 = ? ;", (tag, tag, tag))
	print(Style.BRIGHT + Fore.RED + "[!] If you happen to come across a site that contains child pornography, please notify us to remove it from OLD." + Style.RESET_ALL + "\n")
	print(Style.BRIGHT + Fore.RED + "          Results:\n")
	for row in cur.fetchall():
		if row[5] != None and row[5] != "":
			print(Style.BRIGHT + Fore.RED + row[1])
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3] + ", " + row[4] + ", " + row[5])
		if row[5] == None and row[5] != "" and row[4] != None:
			print(Style.BRIGHT + Fore.RED + row[1])
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3] + ", " + row[4])
		if row[5] == None and row[4] == None and row[5] != "" and row[4] != "":
			print(Style.BRIGHT + Fore.RED + row[1])				
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3])

		print("\n")
	end = time.time()
	ElapsedTime = end - start
	print(Style.BRIGHT + Fore.RED + "[+] Results for " + tag)
	print(Style.BRIGHT + Fore.RED + "[t] Time: " + str(ElapsedTime) + "s\n")

#This Function Prints name of the program, version, developer, time & date
def software():
	print(Fore.WHITE + "OLD - Onion Links Database v0.1 by MCD Th, Gr 2017\n" + Style.RESET_ALL)

############### BANNERS ###############
def banner0():
	print(Style.BRIGHT + Fore.BLUE +                ".MMMMM.  MMM'    \"MMMMMM.")
	print(Style.BRIGHT + Fore.BLUE +                "MM' 'MM  MM'       MM 'MM." + Fore.WHITE + "  Onion Link Database")
	print(Style.BRIGHT + Fore.BLUE +                "MM   MM  MM    .   MM  MMM" + Fore.WHITE + "  Version 0.1")
	print(Style.BRIGHT + Fore.BLUE +                "MM   MM  MM    ;   MM  MMM" + Fore.WHITE + "  By MCD - avinsatne2@gmail.com")
	print(Style.BRIGHT + Style.BRIGHT + Fore.BLUE + "MM. .MM  MM   .M   MM .MM'" + Fore.WHITE + "  Report bugs & expired links")
	print(Style.BRIGHT + Fore.BLUE +                "'MMMMM'  MMMMMMM .MMMMMM'\n" + Style.RESET_ALL)
def banner1():
	line1 = "\n    .aMMMb  dMP     dMMMMb"
	line2 = "   dMP'dMP dMP     dMP VMP"
	line3 = "  dMP dMP dMP     dMP dMP"
	line4 = " dMP.aMP dMP     dMP.aMP"
	line5 = " VMMMP' dMMMMMP dMMMMP'"
	print(Style.BRIGHT + Fore.RED + line1)
	print(Style.BRIGHT + Fore.RED + line2 + Fore.WHITE + "   Onion Links Database")
	print(Style.BRIGHT + Fore.RED + line3 + Fore.WHITE + "   Version 0.1")
	print(Style.BRIGHT + Fore.RED + line4 + Fore.WHITE + "   By MCD - anivsante2@gmail.com")
	print(Style.BRIGHT + Fore.RED + line5 + Fore.WHITE + "   Report bugs & expired links\n" + Style.RESET_ALL)
def banner2():
	print(Fore.BLUE + Style.NORMAL + " .d88b.  dY      d8888b.")
	print(Fore.BLUE + Style.BRIGHT + ".8P  Y8. 88      88  '8D" + Fore.WHITE + Style.BRIGHT + "  Onion Links Database")
	print(Fore.CYAN + "88    88 88      88   88" + Fore.WHITE + Style.BRIGHT + "  Version 0.1")
	print(Fore.CYAN + "88    88 88      88   88" + Fore.WHITE + Style.BRIGHT + "  By MCD - anivsante2@gmail.com")
	print(Fore.WHITE + Style.BRIGHT + "'8b  d8' 88      88. .8D" + Fore.WHITE + " Report bugs & expired links")
	print(Fore.WHITE + " 'Y88P'  Y88888P Y8888D' \n"+ Style.RESET_ALL)
def banner3():
	print(Fore.YELLOW + "\n       OOOOOOOOO     LLLLLLLLLLL             DDDDDDDDDDDDD")
	print(Fore.YELLOW + "     OO" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "OO   L" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "L             D" + Style.BRIGHT + "::::::::::::" + Style.NORMAL + "DDD" + Style.RESET_ALL)
	print(Fore.YELLOW + "   OO" + Style.BRIGHT + ":::::::::::::" + Style.NORMAL + "OO L" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "L             D" + Style.BRIGHT + ":::::::::::::::" + Style.NORMAL + "DD" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OOO" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OLL" + Style.BRIGHT + ":::::::" + Style.NORMAL + "LL             DDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "DDDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + "::::::" + Style.NORMAL + "O   O" + Style.BRIGHT + "::::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D    D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + "::::::" + Style.NORMAL + "O   O" + Style.BRIGHT + "::::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L         LLLLLL  D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D    D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  O" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OOO" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OLL" + Style.BRIGHT + ":::::::" + Style.NORMAL + "LLLLLLLLL" + Style.BRIGHT + ":::::" + Style.NORMAL + "LDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "DDDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + "  OO" + Style.BRIGHT + ":::::::::::::" + Style.NORMAL +"OO L" + Style.BRIGHT + "::::::::::::::::::::::" + Style.NORMAL + "LD" + Style.BRIGHT + ":::::::::::::::" + Style.NORMAL + "DD" + Style.RESET_ALL)
	print(Fore.YELLOW + "    OO" + Style.BRIGHT + ":::::::::" + Style.NORMAL +"OO   L" + Style.BRIGHT + "::::::::::::::::::::::" + Style.NORMAL + "LD" + Style.BRIGHT + "::::::::::::" + Style.NORMAL + "DDD" + Style.RESET_ALL)
	print(Fore.YELLOW + "     OOOOOOOOO     LLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDD\n")
	print(Fore.YELLOW + "$~~~~~~~~~~~~~~~~~~~~~~$ Onion Link Database $~~~~~~~~~~~~~~~~~~~~~~$\n")
	print(Fore.YELLOW + "                             Version 0.1")
	print(Fore.YELLOW + "   By Michael Constantine Dimopoulos - MCD - anivsante2@gmail.com")
	print(Fore.YELLOW + "                   Report bugs & expired links.\n")
	print(Fore.YELLOW + "$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$")
#######################################

#This Function Prints the options;
def options():
	sub = "         --submit      Submit your own link!"
	print(Fore.RED + sub + Style.RESET_ALL)
	print("         --help        Display the help panel (Shown right now)")
	print("         --legals      license and legal disclaimer")
	print("         --service     Site that helps the TOR community") 
	print("         --repository  List of TOR links & websites")
	print("         --store       Store & market (mostly illegal)")
	print("         --weapons     Weapon store and information")
	print("         --adult       Porn (Only legal / CP free)")
	print("         --drugs       Drugs & illegal substances")
	print("         --torrents    Torrents & piracy")
	print("         --world       International & non-english")
	print("         --political   Political pages")
	print("         --commercial  Commercial pages (bitcoin)")
	print("         --hosting     Hosting services")
	print("         --mail        E-mail & chatting services")
	print("         --forums      Forums, chans & boards")
	print("         --chat        Chatrooms")
	print("         --blogs       Blogs & personal pages")
	print("         --books       E-books & essays")
	print("         --hack        Hacking & security")
	print("         --image       Images, icons & photos")
	print("         --audio       Music tracks, streamings & radio")
	print("         --video       Clips & videos\n")
	print("Usage: python old.py [TAG]")
#Interface without arguments
def Interface():
	software()
	random.choice([banner0, banner1, banner2, banner3])()
	options()
#Interface with arguments
def InterfaceS():
	software()
	random.choice([banner0, banner1, banner2, banner3])()
#Argument parsing 
parser = argparse.ArgumentParser()
parser.add_argument("--submit", help="Submit your own link!", action="store_true")
parser.add_argument("--legals", help="License and legal disclaimer", action="store_true")
parser.add_argument("--service", help="Site that helps the TOR community", action="store_true")
parser.add_argument("--repository", help="List of TOR links & websites", action="store_true")
parser.add_argument("--store", help="Store & market (mostly illegal)", action="store_true")
parser.add_argument("--weapons", help="Weapon store and information", action="store_true")
parser.add_argument("--adult", help="Porn & illegal porn", action="store_true")
parser.add_argument("--drugs", help="Drugs & illegal substances", action="store_true")
parser.add_argument("--torrents", help="Torrents & piracy", action="store_true")
parser.add_argument("--world", help="International & non-english", action="store_true")
parser.add_argument("--political", help="Political pages", action="store_true")
parser.add_argument("--commercial", help="Commercial pages (bitcoin)", action="store_true")
parser.add_argument("--hosting", help="Hosting services", action="store_true")
parser.add_argument("--mail", help="E-mail & chatting services", action="store_true")
parser.add_argument("--forums", help="Forums, chans & boards", action="store_true")
parser.add_argument("--chat", help="Chatrooms", action="store_true")
parser.add_argument("--blogs", help="Blogs & personal pages", action="store_true")
parser.add_argument("--books", help="E-books & essays", action="store_true")
parser.add_argument("--hack", help="Hacking & security", action="store_true")
parser.add_argument("--image", help="Images, icons & photos", action="store_true")
parser.add_argument("--audio", help="Music tracks, streamings & radio", action="store_true")
parser.add_argument("--video", help="Clips & videos", action="store_true")

args = parser.parse_args()

if args.service or args.repository or args.store or args.weapons or args.adult or args.drugs or args.torrents or args.world or args.political or args.commercial or args.hosting or args.mail or args.forums or args.chat or args.blogs or args.books or args.hack or args.image or args.audio or args.video:
	# Search with a tag:
	InterfaceS()
	if args.service:
		search("service")
	elif args.repository:
		search("repository")
	elif args.store:
		search("store")
	elif args.weapons:
		search("weapons")
	elif args.adult:
		search("adult")
	elif args.drugs:
		search("drugs")
	elif args.torrents:
		search("torrents")
	elif args.world:
		search("world")
	elif args.political:
		search("political")
	elif args.commercial:
		search("commercial")
	elif args.hosting:                              # Tried to avoid such a mess
		search("hosting")                  # Unfrotunately it will stay with us for a while
	elif args.mail:                                 # At least in python if / elif / else takes swtich/case 's role as well
		search("mail")
	elif args.forums:
		search("forums")
	elif args.chat:
		search("chat")
	elif args.blogs:
		search("blogs")
	elif args.books:
		search("books")
	elif args.hack:
		search("hack")
	elif args.image:
		search("image")
	elif args.audio:
		search("audio")
	elif args.video:
		search("video")
# Legals Option
elif args.legals:
	InterfaceS()
	print(Style.RESET_ALL + "\n\nLisence:\n")
	print("OLD (Onion Links Databse) is free software and can be modified/re-distributed")
	print("under the terms of the GNU GPL 3.0 (GNU General Public License 0.3) as published")
	print("by the Free Software Foundation;\n")
	print(Fore.RED + Style.BRIGHT + "\n\n[!] Legal Disclaimer[!]\n")
	print(Fore.RED + Style.BRIGHT + "Some TOR services could be used for malicious purposes. We do not want")
	print(Fore.RED + Style.BRIGHT + "to encourage such behaviour by promoting these websites. OLD is just a")
	print(Fore.RED + Style.BRIGHT + "repository / terminal search engine. The developer has no responsibility")
	print(Fore.RED + Style.BRIGHT + "for any unauthorized use of the websites listed in our database.\n\n" + Style.RESET_ALL)
# Submit Option
elif args.submit:
	banner1()
	print("To submit a link you need to send an E-Mail to: anivsante2@gmail.com.")
	print("The name of the E-Mail has to be 'OLD link' or else it will be ignored;")
	print("Inside the E-Mail you will have to include:\n")
	print("    I)     The name of the website;")
	print("    II)    The .onion link to the website;")
	print("    III)   The First and required tag (one of the options)")
	print("    IV)    The two optional tags (OPTIONAL)\n")
else:
	Interface()
	
