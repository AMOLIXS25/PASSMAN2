"""Module that manage all print menu of the application"""


def display_logo_menu() -> None:
    """Method that display menu's logo"""
    print("""
============================================================
           __  __  ____  _____         _____ _____ 
     /\   |  \/  |/ __ \|  __ \ /\    / ____/ ____|
    /  \  | \  / | |  | | |__) /  \  | (___| (___  
   / /\ \ | |\/| | |  | |  ___/ /\ \  \___ \\___ \ 
  / ____ \| |  | | |__| | |  / ____ \ ____) |___) |
 /_/    \_\_|  |_|\____/|_| /_/    \_\_____/_____/      
=============================================================                                    
    """)


def display_user_menu() -> None:
    """Method that display user menu(first menu)"""
    print("1.S'enregistrer")
    print("2.Se Connecter")
    print("3.Supprimer son compte")
    print("4.Quitter l'application")
