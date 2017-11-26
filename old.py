# OLD
# Onion Link Database
# Version 0.1
#
# PRE-RELEASE

import colorama
from colorama import Fore, Back, Style
import random
import argparse
import sqlite3
import time

def search(tag):
	start = time.time()
	conn = sqlite3.connect("old.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM links WHERE tag1 = ? OR tag2 = ? OR tag3 = ? ;", (tag, tag, tag))
	print(Style.BRIGHT + Fore.RED + "[!] If you happen to come across a site that contains child pornography, please notify us to remove it from OLD." + Style.RESET_ALL + "\n")
	print(Style.BRIGHT + Fore.RED + "          Results:\n")
	for row in cur.fetchall():
		if row[5] != None:
			print(Style.BRIGHT + Fore.RED + row[1])
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3] + ", " + row[4] + ", " + row[5])
		if row[5] == None and row[4] != None:
			print(Style.BRIGHT + Fore.RED + row[1])
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3] + ", " + row[4])
		if row[5] == None and row[4] == None:
			print(Style.BRIGHT + Fore.RED + row[1])
			print(Fore.BLUE + row[2])
			print(Fore.WHITE + row[3])
		print("\n")
	end = time.time()
	ElapsedTime = end - start
	print(Style.BRIGHT + Fore.RED + "[+] Results for " + tag)
	print(Style.BRIGHT + Fore.RED + "[t] Time: " + str(ElapsedTime) + "s\n")
def software():
	print(Fore.WHITE + "OLD - Onion Link Databse v0.1" + Style.RESET_ALL)
def banner0():
	print(Style.BRIGHT + Fore.BLUE + " MMMMM  MM'     MMMMM")
	print(Style.BRIGHT + Fore.BLUE + "MMM MMM MM      MM''MM" + Fore.WHITE + "  Onion Link Database")
	print(Style.BRIGHT + Fore.BLUE + "MMM MMM MM      MM  MMM" + Fore.WHITE + "  Version 0.1")
	print(Style.BRIGHT + Fore.BLUE + "MMM MMM MM      MM  MMM" + Fore.WHITE + "  By MCD - avinsatne2@gmail.com")
	print(Style.BRIGHT + Style.BRIGHT + Fore.BLUE + "MMM MMM MM.  .M MM..MM" + Fore.WHITE + "   TOR links and websites!")
	print(Style.BRIGHT + Fore.BLUE + " MMMMM  MMMMMMM MMMMM" + Fore.WHITE + "   Report bugs & not working pages.\n" + Style.RESET_ALL)
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
	print(Style.BRIGHT + Fore.RED + line5 + Fore.WHITE + "   Report bugs & not working pages.\n" + Style.RESET_ALL)
def banner2():
	print(Fore.BLUE + Style.NORMAL + " .d88b.  dY      d8888b.")
	print(Fore.BLUE + Style.BRIGHT + ".8P  Y8. 88      88  '8D" + Fore.WHITE + Style.BRIGHT + "   Onion Links Database")
	print(Fore.CYAN + "88    88 88      88   88" + Fore.WHITE + Style.BRIGHT + "  Version 0.1")
	print(Fore.CYAN + "88    88 88      88   88" + Fore.WHITE + Style.BRIGHT + "  By MCD - anivsante2@gmail.com")
	print(Fore.WHITE + Style.BRIGHT + "'8b  d8' 88      88. .8D" + Fore.WHITE + "  Report bugs & not working pages.")
	print(Fore.WHITE + " 'Y88P'  Y88888P Y8888D' \n"+ Style.RESET_ALL)
def banner3():
	print(Fore.YELLOW + "\n      OOOOOOOOO     LLLLLLLLLLL             DDDDDDDDDDDDD")
	print(Fore.YELLOW + "    OO" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "OO   L" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "L             D" + Style.BRIGHT + "::::::::::::" + Style.NORMAL + "DDD" + Style.RESET_ALL)
	print(Fore.YELLOW + "  OO" + Style.BRIGHT + ":::::::::::::" + Style.NORMAL + "OO L" + Style.BRIGHT + ":::::::::" + Style.NORMAL + "L             D" + Style.BRIGHT + ":::::::::::::::" + Style.NORMAL + "DD" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OOO" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OLL" + Style.BRIGHT + ":::::::" + Style.NORMAL + "LL             DDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "DDDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + "::::::" + Style.NORMAL + "O   O" + Style.BRIGHT + "::::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D    D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::" + Style.NORMAL + "O     O" + Style.BRIGHT + ":::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L                 D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D     D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + "::::::" + Style.NORMAL + "O   O" + Style.BRIGHT + "::::::" + Style.NORMAL +"O  L" + Style.BRIGHT + ":::::" + Style.NORMAL + "L         LLLLLL  D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D    D" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " O" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OOO" + Style.BRIGHT + ":::::::" + Style.NORMAL + "OLL" + Style.BRIGHT + ":::::::" + Style.NORMAL + "LLLLLLLLL" + Style.BRIGHT + ":::::" + Style.NORMAL + "LDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "DDDDD" + Style.BRIGHT + ":::::" + Style.NORMAL + "D" + Style.RESET_ALL)
	print(Fore.YELLOW + " OO" + Style.BRIGHT + ":::::::::::::" + Style.NORMAL +"OO L" + Style.BRIGHT + "::::::::::::::::::::::" + Style.NORMAL + "LD" + Style.BRIGHT + ":::::::::::::::" + Style.NORMAL + "DD" + Style.RESET_ALL)
	print(Fore.YELLOW + "   OO" + Style.BRIGHT + ":::::::::" + Style.NORMAL +"OO   L" + Style.BRIGHT + "::::::::::::::::::::::" + Style.NORMAL + "LD" + Style.BRIGHT + "::::::::::::" + Style.NORMAL + "DDD" + Style.RESET_ALL)
	print(Fore.YELLOW + "     OOOOOOOOO     LLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDD\n")
	print(Fore.YELLOW + "$~~~~~~~~~~~~~~~~~~~~~~$ Onion Link Database $~~~~~~~~~~~~~~~~~~~~~~$\n")
	print(Fore.YELLOW + "                             Version 0.1")
	print(Fore.YELLOW + "   By Michael Constantine Dimopoulos - MCD - anivsante2@gmail.com")
	print(Fore.YELLOW + "               Report bugs & pages that don't work.\n")
	print(Fore.YELLOW + "$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$")


def options():
	sub = "         --submit      Submit your own link!"
	print(Fore.RED + sub + Style.RESET_ALL)
	print("         --help        Display the help panel (Shown right now)")
	print("         --legals      License and legal disclaimer")
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
def Interface():
	software()
	random.choice([banner0, banner1, banner2, banner3])()
	options()
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
		search("comcommercial")
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

elif args.legals:
	InterfaceS()
	print("SECTION NOT DONE YET FOLKS")
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
	
