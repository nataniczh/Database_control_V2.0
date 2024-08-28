from src.queries import SyncORM

def help_command():
    """Display help information."""
    print("Dostupné příkazy:")
    print("/help - Zobrazení této nápovědy")
    print("/prop_contr - Kontrola zvolené průřezové charakteristiky.")
    print("/values_contr - Kontrola hodnot různých vlastností.")
    print("/exit - Ukončení programu")



  
def main():
    #tuta logika programmy
    print("Welcome to the program!\
        \nTento skript je určen pro komplexní kontrolu různých údajů\
        \nzaznamenaných teamem D do net_genia\
        \n(bohužel umí pouze kontrolovat smykové plochy průřezů a porovnávat je s referenčním vzorcem).")
    
    while True:
        user_input = input("Zadejte příkaz (pro dostupné příkazy zadejte /help): ")
        
        if user_input == "/help":
            help_command()
    
                
        elif user_input == "/prop_contr":
            SyncORM.properties_control()
            pass
        
        elif user_input == "/values_contr":
            SyncORM.values_control()
            pass
        
        elif user_input == "/exit":
            print("Exiting program...")
            break
        
        else:
            print("Neplatný příkaz. Zadejte /help pro dostupné příkazy.")


if __name__ == "__main__":
    main()