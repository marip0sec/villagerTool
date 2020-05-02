DEBUG = True
VERBOSE = True

#COLUMN NAMES
NAME = "Name"
PERSONALITY = "Personality"
SPECIES = "Species"
STAR_SIGN = "Star Sign"

VILLAGERS_DATA_SOURCE = "villagers.csv"
COMPATIBILITY_DATA_SOURCE = "compatibilityMatrix.csv"

#COMPATIBILITY SYMBOLS
CLUB = 'c'
DIAMOND = 'd'
CROSS = 'x'
HEART = 'h'

#PERSONALITIES
NORMAL = 0
LAZY = 1
PEPPY = 2
JOCK = 3
SNOOTY = 4
CRANKY = 5
SMUG = 6
SISTERLY = 7

NORMAL_STRING = "Normal"
LAZY_STRING = "Lazy"
PEPPY_STRING = "Peppy"
JOCK_STRING = "Jock"
SNOOTY_STRING = "Snooty"
CRANKY_STRING = "Cranky"
SMUG_STRING = "Smug"
SISTERLY_STRING = "Sisterly"

PERSONALITY_DICTIONARY = {    
    NORMAL_STRING : NORMAL,
    LAZY_STRING : LAZY,
    PEPPY_STRING : PEPPY,
    JOCK_STRING : JOCK,
    SNOOTY_STRING : SNOOTY,
    CRANKY_STRING : CRANKY,
    SMUG_STRING : SMUG,
    SISTERLY_STRING : SISTERLY
}

#SPECIES
BEAR = 2
CUB = 3
BULL = 5
COW = 7
CAT = 11
TIGER = 13
DOG = 17
WOLF = 19
GOAT = 23
SHEEP = 29
KANGAROO = 31
KOALA = 37
DEER = 41
HORSE = 43
HAMSTER = 47
SQUIRREL = 53
MOUSE = 59
GORILLA = 61
MONKEY = 67

BEAR_STRING = "Bear"
CUB_STRING = "Cub"
BULL_STRING = "Bull"
COW_STRING = "Cow"
CAT_STRING = "Cat"
TIGER_STRING = "Tiger"
DOG_STRING = "Dog"
WOLF_STRING = "Wolf"
GOAT_STRING = "Goat"
SHEEP_STRING = "Sheep"
KANGAROO_STRING = "Kangaroo"
KOALA_STRING = "Koala"
DEER_STRING = "Deer"
HORSE_STRING = "Horse"
HAMSTER_STRING = "Hamster"
SQUIRREL_STRING = "Squirrel"
MOUSE_STRING = "Mouse"
GORILLA_STRING = "Gorilla"
MONKEY_STRING = "Monkey"

SPECIES_DICTIONARY= {    
    BEAR_STRING : BEAR,
    CUB_STRING : CUB,
    BULL_STRING : BULL,
    COW_STRING : COW,
    CAT_STRING : CAT,
    TIGER_STRING : TIGER,
    DOG_STRING : DOG,
    WOLF_STRING : WOLF,
    GOAT_STRING : GOAT,
    SHEEP_STRING : SHEEP,
    KANGAROO_STRING : KANGAROO,
    KOALA_STRING : KOALA,
    DEER_STRING : DEER,
    HORSE_STRING : HORSE,
    HAMSTER_STRING : HAMSTER,
    SQUIRREL_STRING : SQUIRREL,
    MOUSE_STRING : MOUSE,
    GORILLA_STRING : GORILLA,
    MONKEY_STRING : MONKEY
}

RELEVANT_SPECIES = SPECIES_DICTIONARY.keys()

#SIGN GROUPS
GROUP_1 = 2
GROUP_2 = 3
GROUP_3 = 5
GROUP_4 = 7

ARIES_STRING = "Aries"
LEO_STRING = "Leo"
SAGITTARIUS_STRING = "Sagittarius"
TAURUS_STRING = "Taurus"
VIRGO_STRING = "Virgo"
CAPRICORN_STRING = "Capricorn"
GEMINI_STRING = "Gemini"
LIBRA_STRING = "Libra"
AQUARIUS_STRING = "Aquarius"
CANCER_STRING = "Cancer"
SCORPIO_STRING = "Scorpio"
PISCES_STRING = "Pisces"

SIGN_DICTIONARY = {     
    ARIES_STRING : GROUP_1,
    LEO_STRING : GROUP_1,
    SAGITTARIUS_STRING : GROUP_1,
    TAURUS_STRING : GROUP_2,
    VIRGO_STRING : GROUP_2,
    CAPRICORN_STRING : GROUP_2,
    GEMINI_STRING : GROUP_3,
    LIBRA_STRING : GROUP_3,
    AQUARIUS_STRING : GROUP_3,
    CANCER_STRING : GROUP_4,
    SCORPIO_STRING : GROUP_4,
    PISCES_STRING : GROUP_4    
}
