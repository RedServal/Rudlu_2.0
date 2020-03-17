import random

weeb = ["https://cdn.discordapp.com/attachments/470974498548613123/679830457587990799/ddd4yht-49ff3ad8-a77c-4f2e-948e-694c3620b708.png",
"https://i.kym-cdn.com/photos/images/original/001/425/696/2f8.png",
"https://pm1.narvii.com/6876/1122f5434edb48d0ca921996e70298650443b0d4r1-300-301v2_hq.jpg",
"https://pm1.narvii.com/6876/93c78a71db068cecbb24bb0c79ee4f8466563857r1-888-514v2_hq.jpg",
"https://pm1.narvii.com/6876/1c560b6471eeeaec93414dfa9021e10d813386e2r1-500-572v2_hq.jpg",
"https://pm1.narvii.com/6876/ad97393aefb9dcde88704b3b24704ac1f94c7857r1-1080-1080v2_hq.jpg",
"https://pm1.narvii.com/6876/b6908d817db53340c623d3d3ef1ffeb6e76e1af5r1-347-299v2_hq.jpg",
"https://pm1.narvii.com/6876/b539a113bd854c2e9409c2da1831dab70b22f32cr1-471-463v2_hq.jpg",
"https://pm1.narvii.com/6876/4dfc80dc53d4effd42c94aafb913049f942439b5r1-312-376v2_hq.jpg",
"https://pm1.narvii.com/6876/81479667dda8e715a1e9c0ef2c367f8cbd465977r1-400-279v2_hq.jpg",
"https://pm1.narvii.com/6876/83fc3abccda4744c4060b782846282848a4de6cer1-981-1080v2_hq.jpg"]

def choose_weeb() :
    return random.choice(weeb)


morse = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':' '}
                    