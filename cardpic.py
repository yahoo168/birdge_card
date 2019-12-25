from tkinter import *
from tkinter import PhotoImage
from functools import total_ordering

def picture_file(mycard):
    if mycard == "♠2":
        photo = PhotoImage(file='2-spades.png')
        return (photo)

    elif mycard == "♠3":
        photo = PhotoImage(file='3-spades.png')
        return (photo)
    
    elif mycard == "♠4":
        photo = PhotoImage(file='4-spades.png')
        return (photo)
    
    elif mycard == "♠5":
        photo = PhotoImage(file='5-spades.png')
        return (photo)
    
    elif mycard == "♠6":
        photo = PhotoImage(file='6-spades.png')
        return (photo)
    
    elif mycard == "♠7":
        photo = PhotoImage(file='7-spades.png')
        return (photo)
    
    elif mycard == "♠8":
        photo = PhotoImage(file='8-spades.png')
        return (photo)

    elif mycard == "♠9":
        photo = PhotoImage(file='9-spades.png')
        return (photo)
    
    elif mycard == "♠10":
        photo = PhotoImage(file='10-spades.png')
        return (photo)
    
    elif mycard == "♠J":
        photo = PhotoImage(file='11-spades.png')
        return (photo)
    
    elif mycard == "♠Q":
        photo = PhotoImage(file='12-spades.png')
        return (photo)
    
    elif mycard == "♠K":
        photo = PhotoImage(file='13-spades.png')
        return (photo)
    
    elif mycard == "♠A":
        photo = PhotoImage(file='14-spades.png')
        return (photo)
    
    # end of spades
    
    elif mycard == "♥2":
        photo = PhotoImage(file='2-hearts.png')
        return (photo)
    
    elif mycard == "♥3":
        photo = PhotoImage(file='3-hearts.png')
        return (photo)
    
    elif mycard == "♥4":
        photo = PhotoImage(file='4-hearts.png')
        return (photo)
    
    elif mycard == "♥5":
        photo = PhotoImage(file='5-hearts.png')
        return (photo)
    
    elif mycard == "♥6":
        photo = PhotoImage(file='6-hearts.png')
        return (photo)
    
    elif mycard == "♥7":
        photo = PhotoImage(file='7-hearts.png')
        return (photo)
    
    elif mycard == "♥8":
        photo = PhotoImage(file='8-hearts.png')
        return (photo)
    
    elif mycard == "♥9":
        photo = PhotoImage(file='9-hearts.png')
        return (photo)
    
    elif mycard == "♥10":
        photo = PhotoImage(file='10-hearts.png')
        return (photo)
    
    elif mycard == "♥J":
        photo = PhotoImage(file='11-hearts.png')
        return (photo)
    
    elif mycard == "♥Q":
        photo = PhotoImage(file='12-hearts.png')
        return (photo)
    
    elif mycard == "♥K":
        photo = PhotoImage(file='13-hearts.png')
        return (photo)
    
    elif mycard == "♥A":
        photo = PhotoImage(file='14-hearts.png')
        return (photo)
    # end of hearts
    
    elif mycard == "♦2":
        photo = PhotoImage(file='2-diamonds.png')
        return (photo)
    
    elif mycard == "♦3":
        photo = PhotoImage(file='3-diamonds.png')
        return (photo)
    
    elif mycard == "♦4":
        photo = PhotoImage(file='4-diamonds.png')
        return (photo)
    
    elif mycard == "♦5":
        photo = PhotoImage(file='5-diamonds.png')
        return (photo)
        
    elif mycard == "♦6":
        photo = PhotoImage(file='6-diamonds.png')
        return (photo)
    
    elif mycard == "♦7":
        photo = PhotoImage(file='7-diamonds.png')
        return (photo)
    
    elif mycard == "♦8":
        photo = PhotoImage(file='8-diamonds.png')
        return (photo)

    elif mycard == "♦9":
        photo = PhotoImage(file='9-diamonds.png')
        return (photo)
    
    elif mycard == "♦10":
        photo = PhotoImage(file='10-diamonds.png')
        return (photo)
    
    elif mycard == "♦J":
        photo = PhotoImage(file='11-diamonds.png')
        return (photo)
    
    elif mycard == "♦Q":
        photo = PhotoImage(file='12-diamonds.png')
        return (photo)
    
    elif mycard == "♦K":
        photo = PhotoImage(file='13-diamonds.png')
        return (photo)
    
    elif mycard == "♦A":
        photo = PhotoImage(file='14-diamonds.png')
        return (photo)
    # end of diamonds
    
    elif mycard == "♣2":
        photo = PhotoImage(file='2-clubs.png')
        return (photo)
    
    elif mycard == "♣3":
        photo = PhotoImage(file='3-clubs.png')
        return (photo)
    
    elif mycard == "♣4":
        photo = PhotoImage(file='4-clubs.png')
        return (photo)
    
    elif mycard == "♣5":
        photo = PhotoImage(file='5-clubs.png')
        return (photo)
    
    elif mycard == "♣6":
        photo = PhotoImage(file='6-clubs.png')
        return (photo)
    
    elif mycard == "♣7":
        photo = PhotoImage(file='7-clubs.png')
        return (photo)
    
    elif mycard == "♣8":
        photo = PhotoImage(file='8-clubs.png')
        return (photo)

    elif mycard == "♣9":
        photo = PhotoImage(file='9-clubs.png')
        return (photo)
    
    elif mycard == "♣10":
        photo = PhotoImage(file='10-clubs.png')
        return (photo)
    
    elif mycard == "♣J":
        photo = PhotoImage(file='11-clubs.png')
        return (photo)
    
    elif mycard == "♣Q":
        photo = PhotoImage(file='12-clubs.png')
        return (photo)
    
    elif mycard == "♣K":
        photo = PhotoImage(file='13-clubs.png')
        return (photo)
    
    elif mycard == "♣A":
        photo = PhotoImage(file='14-clubs.png')
        return (photo)