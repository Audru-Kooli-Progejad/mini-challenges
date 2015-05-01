'''
Siin failis on ulesanded, mis on seotud tingimus lausetega. (Conditionals)

Naide tingimus lausest:

if x == 0: # x == 0 on tingimus (x vordub 0)
    # Tee midagi kui tingimus on tosi
else:
    # Tee midagi kui tingimus ei ole tosi

Veel laheb siin vaja teadmist:

and      - Saab tingimusi ehitada sidudes neid "ja"-ga.
              Tingimus on tosi ainult kui molemad tingimused on tosid.

True and True   -> True
True and False  -> False
False and False -> False
False and True  -> False

or        - Saab tingimusi ehitada sidudes neid "voi"-ga.
             Tingimus on tosi kui vahemalt yks tingimus on tosi

True or True   -> True
True or False  -> True
False or False -> False
False or True  -> True

type(x) - Saab kasutada kui tahad teada, mis tyypi on x. (str, int, list)
x % y    - Moodulo operaatoriga saab kontrollida, kas x jagub y-ga.
len(x)    - Annab x-i pikkuse.
'''


def is_ten(x):
    """Kontrollida kas x on 10
    nt. is_ten(10) -> True
    *Naite ylesanne*
    """
    if x == 10:
        return True
    else:
        return False


def bigger_than_ten(x):
    """Kontrollida kas x on suurem 10st
    nt. bigger_than_ten(0) -> False"""
    pass


def smaller_than_ten(x):
    """Kontrollida kas x on vaiksem 10st
    nt. smaller_than_ten(0) -> True"""
    pass


def return_bigger(x, y):
    """Tagastada suurem.
    nt. return_bigger(1, 0) -> 1"""
    pass


def is_positive(x):
    """Kontrollida kas arv on postiivne.
    nt. is_positive(1) -> True"""
    pass


def is_negative(x):
    """Kontrollida kas arv on negatiivne.
    nt. is_negative(-1) -> True"""
    pass
