'''
    enums.py

    contains useful enums like sheet names

'''

from enum import Enum

pfx = "-"
blnk = "ㅤ"

# used like Sheet.OWNER.value
class Sheet(Enum):

    # basic info
    OWNER = "오너" 
    CHARACTER = "캐릭터"

    # place sheets
    DAWN = "탐색:새벽녘"
    HQ = "탐색:본부"
    

    # item types
    ITEM_ALCH = "아이템:연금"
    ITEM_MEAT = "아이템:고기"
    ITEM_VEG = "아이템:채소"
    ITEM_FOOD = "아이템:음식"


class Emote(Enum):
    GEB = "<:geb_main:1257910386355867720>" 
    YISANG = "<:yisang_main:1257920236943048806>" 
    LUDMILA = "<:ludmila_main:1257920168735019038>"
    MONTAG = "<:montag_main:1257920171394469958>" 
    YIGEUM = "<:yigeum_main:1257920172828790856>"
    BETH = "<:beth_main:1257920160782745600>"

    MING = "<:ming_main:1257920169788047515>" 
    HEATH = "<:heath_main:1257920165656662016>" 
    GAHWAN = "<:gahwan_main:1257920163827810378>" 
    FLEUR = "<:fleur_main:1257920162489827470>"
    HONGLU = "<:honglu_main:1257920167220875304>"


