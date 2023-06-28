import itertools

def generate_combinations(num_characters):
    characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%&*"

    with open("combinations.txt", "w") as file:
        for i in range(1, num_characters + 1):
            combinations = itertools.product(characters, repeat=i)
            for combination in combinations:
                line = ''.join(combination) + "\n"
                file.write(line)

def print_banner():
    banner = '''
                                                                                        
@@@@@@@    @@@@@@   @@@  @@@@@@@   @@@@@@@@  @@@@@@@     @@@    @@@   @@@@@@@@     @@@  
@@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@   @@@@   @@@@  @@@@@@@@@@   @@@@  
@@!  @@@  @@!  @@@  @@!  @@!  @@@  @@!       @@!  @@@  @@@!!  @@@!!  @@!   @@@@  @@@!!  
!@!  @!@  !@!  @!@  !@!  !@!  @!@  !@!       !@!  @!@    !@!    !@!  !@!  @!@!@    !@!  
@!@!!@!   @!@!@!@!  !!@  @!@  !@!  @!!!:!    @!@!!@!     @!@    @!@  @!@ @! !@!    @!@  
!!@!@!    !!!@!!!!  !!!  !@!  !!!  !!!!!:    !!@!@!      !@!    !@!  !@!!!  !!!    !@!  
!!: :!!   !!:  !!!  !!:  !!:  !!!  !!:       !!: :!!     !!:    !!:  !!:!   !!!    !!:  
:!:  !:!  :!:  !:!  :!:  :!:  !:!  :!:       :!:  !:!    :!:    :!:  :!:    !:!    :!:  
::   :::  ::   :::   ::   :::: ::   :: ::::  ::   :::    :::    :::  ::::::: ::    :::  
 :   : :   :   : :  :    :: :  :   : :: ::    :   : :     ::     ::   : : :  :      ::  
                                                                                        
'''

    print("PWGen V1.0")
    print("Made By")
    print(banner)

def main():
    print_banner()
    num_characters = int(input("Enter the maximum number of characters per combination: "))
    generate_combinations(num_characters)
    print("The combinations have been saved in the file combinations.txt.")

if __name__ == "__main__":
    main()
