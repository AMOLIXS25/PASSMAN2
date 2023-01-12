"""Module that manage the application"""

from menu import display_logo_menu, display_user_menu


def is_user_menu_choice_valid(user_menu_choice_to_valited: str) -> bool:
    """Verif if the user_menu_choice_is_valid"""
    return user_menu_choice_to_valited.strip().isdigit()


def user_menu_loop() -> None:
    """Loop for the user menu"""
    user_menu_choice: str = ""
    while not user_menu_choice == 4:
        display_user_menu()
        user_menu_choice: str = input("[*] Entrez votre choix : ")
        if is_user_menu_choice_valid(user_menu_choice):
            user_menu_choice = int(user_menu_choice)
        else:
            print("[!] Veuillez entrez un choix valide !")
        user_menu_choice_manager(user_menu_choice)


def user_menu_choice_manager(user_menu_choice: int) -> None:
    """
    The manager of the user menu
    :param: user_menu_choice The user's choice for the user menu
    """
    if user_menu_choice == 1:
        # TODO Register()
        print("register")
    elif user_menu_choice == 2:
        # TODO login()
        pass
    elif user_menu_choice == 3:
        # TODO remove_user()
        pass
    elif user_menu_choice == 4:
        # TODO quit()
        pass


def start() -> None:
    """Start the applications"""
    display_logo_menu()
    user_menu_loop()
