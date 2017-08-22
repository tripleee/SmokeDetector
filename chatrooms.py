# -*- coding: utf-8 -*-
from datetime import datetime

from ChatExchange.chatexchange import client, rooms

from helpers import log

    
class Room (rooms.Room):
    
    site_wrappers = {}
    rooms = {}
    smokey_ids = {}

    experimental_reasons = [  # Don't widely report these
        "potentially bad keyword in answer",
        "potentially bad keyword in body",
        "potentially bad keyword in title",
        "potentially bad keyword in username"]
    
    def __init__(self, room_id, name, site, smokey_id=None, main_room=False,
        watcher=False, stdwatcher=False, sites=[],
            excluded_sites=[], excluded_reasons=None, privileged_users=[]):
        self.room_id = str(room_id)
        self.room_name = name
        self.site = site
        if site not in site_wrappers:
            site_wrappers[site] = client.Client(site)
        if smokey_id:
            self.smokey_id = int(smokey_id)
            if smokey_ids[site] != self.smokey_id:
                log('warn', 'Replacing old {0} smokey ID {1} with {2}'.format(
                    site, smokey_ids[site], self.smokey_id))
                smokey_ids[site] = self.smokey_id
        elif not smokey_ids[site]:
            raise KeyError('No smokey ID for site {0}'.format(site))
        self.main_room = main_room
        self.watcher = watcher
        self.stdwatcher = stdwatcher
        self.blocked_time = 0
        self.sites = sites[:]
        self.excluded_sites = exluded_sites[:]
        self.excluded_reasons = experimental_reasons[:]
        if excluded_reasons is not None:
            self.excluded_reasons += excluded_reasons
        self.privileged_users = privileged_users[:]
        self.code_privileged_users = []
        self.users_chatting = []
        self.latest_messages = []
        rooms[self.room_id] = self


def global_init (no_chat=False, charcoal_only=False):
    if no_chat:
        return Room.rooms

    Room(11540, "Charcoal HQ", "stackexchange.com", smokey_id=120914,
        main_room=True,
        privileged_users=[
            "117490",   # Normal Human
            "66258",    # Andy
            "31768",    # ManishEarth
            "103081",   # hichris123
            "73046",    # Undo
            "88521",    # ProgramFOX
            "59776",    # Doorknob
            "31465",    # Seth
            "88577",    # Santa Claus
            "34124",    # Andrew Leach
            "54229",    # apnorton
            "20459",    # S.L. Barth
            "32436",    # tchrist
            "30477",    # Brock Adams
            "58529",    # ferrybig
            "145208",   # Robert Longson
            "178825",   # Ms Yvette
            "171800",   # JAL
            "64978",    # PeterJ
            "125141",   # Jeffrey Bosboom
            "54902",    # bummi
            "135450",   # M.A.R.
            "145604",   # Quill
            "60548",    # rene
            "121401",   # michaelpri
            "116218",   # JamesENL
            "82927",    # Braiam
            "11606",    # bwDraco
            "19761",    # Ilmari Karonen
            "108271",   # Andrew T.
            "171054",   # Magisch
            "190011",   # Petter Friberg
            "165661",   # Tunaki
            "145086",   # Wai Ha Lee
            "137665",   # ByteCommander
            "147884",   # wythagoras
            "186395",   # Åna
            "181293",   # Ashish Ahuja
            "163686",   # Gothdo
            "145827",   # angussidney
            "244748",   # Supreme Leader SnokeDetector (angussidney's sock)
            "121520",   # ArtOfCode
            "244382",   # Lt. A. Code (ArtOfCode's sock to test things with)
            "137388",   # QPaysTaxes
            "212311",   # Ryan Bemrose
            "172397",   # Kyll
            "224538",   # FrankerZ
            "61202",    # OldSkool
            "56166",    # Jan Dvorak
            "133966",   # DavidPostill
            "22839",    # djsmiley2k
            "97389",    # Kaz Wolfe
            "144962",   # DJMcMayhem
            "139423",   # NobodyNada
            "62118",    # tripleee
            "130558",   # Registered User
            "128113",   # arda
            "164318",   # Glorfindel
            "175347",   # Floern
            "180274",   # Alexander O'Mara
            "158742",   # Rob
            "207356",   # 4castle
            "133031",   # Mithrandir
            "215671",   # Locutus of Borg (Mithrandir's Sock)
            "169713",   # Mego
            "126657",   # Cerbrus
            "10145",    # Thomas Ward
            "161943",   # J F
            "195967",   # CaffeineAddiction
            "5363",     # Stijn
            "248139",   # FelixSFD
            "156721",   # D-side
            "167070",   # quartata
            "172450",   # Hovercraft Full Of Eels
            "56200",    # Eric Leschinski
            "211021",   # Henders
            "255290",   # Gypsy Spellweaver
            "64521",    # CalvT
            "165474",   # Hyper Neutrino
            "281362",   # Hyper Neutrino v2
            "169252",   # Cai
            "155243",   # Nisse Engström
            "69330",    # Sconibulus
            "164187",   # Okx
            "202619",   # John Militer
            "262693"    # suraj
            ])

    if charcoal_only:
        return Room.rooms
        
    Room(41570, "SOCVR", "stackexchange.com", smokey_id=3735529,
        sites=["stackoverflow.com"],
        privileged_users=[
            "1849664",  # Undo
            "2581872",  # hichris123
            "1198729",  # Manishearth
            "3717023",  # Normal Human aka 1999
            "2619912",  # ProgramFOX
            "578411",   # rene
            "1043380",  # gunr2171
            "2246344",  # Sam
            "2756409",  # TylerH
            "1768232",  # durron597
            "359284",   # Kevin Brown
            "258400",   # easwee
            "3622940",  # Unihedron
            "3204551",  # Deduplicator
            "4342498",  # NathanOliver
            "4639281",  # Tiny Giant
            "3093387",  # josilber
            "1652962",  # cimmanon
            "1677912",  # Mogsdad
            "656243",   # Lynn Crumbling
            "3933332",  # Rizier123
            "2422013",  # cybermonkey
            "3478852",  # Nisse Engström
            "2302862",  # Siguza
            "1324",     # Paul Roub
            "1743880",  # Tunaki
            "1663001",  # DavidG
            "2415822",  # JAL
            "4174897",  # Kyll
            "5299236",  # Kevin Guan
            "4050842",  # Thaillie
            "1816093",  # Drew
            "874188",   # Triplee
            "880772",   # approxiblue
            "1835379",  # Cerbrus
            "3956566",  # JamesENL
            "2357233",  # Ms Yvette
            "3155639",  # AlexanderOMara
            "462627",   # Praveen Kumar
            "4490559",  # intboolstring
            "1364007",  # Wai Ha Lee
            "1699210",  # bummi
            "563532",   # Rob
            "5389107",  # Magisch
            "4099593",  # bhargav-rao
            "1542723",  # Ferrybig
            "2025923",  # Tushar
            "5292302",  # Petter Friberg
            "792066",   # Braiam
            "5666987",  # Ian
            "3160466",  # ArtOfCode
            "4688119",  # Ashish Ahuja
            "3476191",  # Nobody Nada
            "2227743",  # Eric D
            "821878",   # Ryan Bemrose
            "1413395",  # Panta Rei
            "4875631",  # FrankerZ
            "2958086",  # Compass
            "499214",   # JanDvorak
            "5647260",  # Andrew L.
            "559745",   # Floern
            "5743988",  # 4castle
            "4622463",  # angussidney
            "603346",   # Thomas Ward
            "3002139",  # Baum mit Augen
            "1863564",  # QPaysTaxes
            "4687348",  # FelixSFD
            "4751173",  # Glorfindel
            "2233391",  # henders
            "4805174",  # kayess
            "2370483",  # Machavity
            "1873567",  # CalvT
            "4826457",  # suraj
            ])

    Room(89, "Tavern on Meta", "meta.stackexchange.com", smokey_id=266345,
        excluded=sites=["stackoverflow.com"],
        excluded_reasons=[
            "all-caps body",
            "all-caps answer",
            "repeating characters in body",
            "repeating characters in title",
            "repeating characters in answer",
            "few unique characters in body",
            "few unique characters in answer",
            "title has only one unique char",
            "phone number detected in title",
            "offensive body detected",
            "no whitespace in body",
            "no whitespace in answer",
            ],
            privileged_users=[
                "315433",   # Normal Human
                "244519",   # CRABOLO
                "244382",   # TGMCians
                "194047",   # Jan Dvorak
                "158100",   # rene
                "178438",   # Manishearth
                "237685",   # hichris123
                "215468",   # Undo
                "229438",   # ProgramFOX
                "180276",   # Doorknob
                "161974",   # Lynn Crumbling
                "186281",   # Andy
                "266094",   # Unihedro
                "245167",   # Infinite Recursion
                "230261",   # Jason C
                "213575",   # Braiam
                "241919",   # Andrew T.
                "203389",   # backwards-Seth
                "202832",   # Mooseman
                "160017",   # bwDraco
                "201151",   # bummi
                "188558",   # Frank
                "229166",   # Santa Claus
                "159034",   # Kevin Brown
                "203972",   # PeterJ
                "188673",   # Alexis King
                "258672",   # AstroCB
                "227577",   # Sam
                "255735",   # cybermonkey
                "279182",   # Ixrec
                "271104",   # James
                "220428",   # Qantas 94 Heavy
                "153355",   # tchrist
                "238426",   # Ed Cottrell
                "166899",   # Second Rikudo
                "287999",   # ASCIIThenANSI
                "208518",   # JNat
                "284141",   # michaelpri
                "260312",   # vaultah
                "244062",   # SouravGhosh
                "152859",   # Shadow Wizard
                "201314",   # apnorton
                "280934",   # M.A.Ramezani
                "200235",   # durron597
                "148310",   # Awesome Poodles / Brock Adams
                "168333",   # S.L. Barth
                "257207",   # Unikitty
                "244282",   # DroidDev
                "163250",   # Cupcake
                "298265",   # BoomsPlus
                "253560",   # josilber
                "244254",   # misterManSam
                "188189",   # Robert Longson
                "174699",   # Ilmari Karonen
                "202362",   # chmod 666 telkitty
                "289717",   # Quill
                "237813",   # bjb568
                "311345",   # Simon Klaver
                "171881",   # rekire
                "260388",   # Pandya
                "310756",   # Ms Yvette
                "262399",   # Jeffrey Bosboom
                "242209",   # JAL
                "280883",   # ByteCommander
                "302251",   # kos
                "262823",   # ArtOfCode
                "215067",   # Ferrybig
                "308386",   # Magisch
                "285368",   # angussidney
                "158829",   # Thomas Ward
                "294691",   # Mithrandir
                "203553",   # CalvT
                "289971",   # Hyper Neutrino
                ])

    Room(111347, "SOBotics", "stackoverflow.com", stdwatcher=True,
        privileged_users=[
            "3160466",  # ArtOfCode
            "1849664",  # Undo
            "3002139",  # Baum mit Augen
            "3476191",  # Nobody Nada
            "5292302",  # Petter Friberg
            "4688119",  # Ashish Ahuja
            "4099593",  # Bhargav Rao
            "1743880",  # Tunaki
            "559745",   # Floern
            "4687348",  # FelixSFD
            "6375113",  # Bugs
            "4622463",  # angussidney
            "158742",   # Rob
            "4050842",  # Thaillie
            ])

    # If you change these sites, please also update the wiki at
    # https://github.com/Charcoal-SE/SmokeDetector/wiki/Chat-Rooms

    se="stackexchange.com"
    Room(8089, "mempool", se, sites=["bitcoin.stackexchange.com"])
    Room(1964, "(private room)", se, sites=["bricks.stackexchange.com"])
    Room(38932, "The Studio", se, sites=["crafts.stackexchange.com"])
    Room(95, "English Language & Usage", se, sites=["english.stackexchange.com"])
    Room(24938, "Language Overflow", se, sites=["ell.stackexchange.com"])
    Room(34620, "Whisper", se, sites=["ethereum.stackexchange.com"])
    Room(56223, "The Spam Blot", se, sites=["graphicdesign.stackexchange.com"])
    Room(47869, "Charcoal SmokeDetector Reports", se, sites=["magento.stackexchange.com"])
    Room(2165, "C.R.U.D.E.", se, sites=["math.stackexchange.com"])
    Room(468, "V'dibarta Bam", se, sites=["judaism.stackexchange.com"])
    Room(35068, "Smoke Detector", se, sites=["money.stackexchange.com"],
        excluded_reasons=["All-caps title", "All-caps body", "All-caps answer"])
    Room(40705, "Movies & TV Moderation & Maintenance", se, sites=["movies.stackexchange.com"])
    Room(388, "Parenting", se, sites=["parenting.stackexchange.com"])
    Room(11, "RPG General Chat", se, sites=["rpg.stackexchange.com"])
    # Stack Overflow: SOCVR listed above
    Room(201, "Ask Ubuntu General Room", se, watcher=True, sites=["askubuntu.com"],
        excluded_reasons=[
            "All-caps title",   # these should be in uppercased form
            "All-caps body",
            "All-caps answer",
            "Phone number detected",
            "Repeating characters in title",
            "Repeating characters in body",
            "Repeating characters in answer",
            "Link at end of answer"
        ])
    Room(22462, "Ru.SO General Room", se, sites=["ru.stackoverflow.com"])
    Room(59281, "SFF community cleanup room", sites=["scifi.stackexchange.com"])

    return Room.rooms
