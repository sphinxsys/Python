"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""

    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    firstnames = ('Baby Oil', 'Bad News', 'Big Burps', "Bill Beenie_Weenie", "Bob Stinkbug", 'Bowel Noises', 'Boxelder', "BudLite", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry')

    surnames = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'SugarGold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:
        first_name = random.choice(firstnames)
        surname = random.choice(surnames)

        print("\n\n")
        print("{} {}".format(first_name, surname), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Presss enter else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("Press enter to exit")

if __name__ == '__main__':
    main()
