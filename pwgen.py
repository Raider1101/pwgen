import itertools

def generate_combinations(num_characters):
    characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%&*"
    
    combinations = []
    for i in range(1, num_characters + 1):
        combinations.extend(itertools.product(characters, repeat=i))
    return combinations

def save_combinations(combinations):
    with open("combinations.txt", "w") as file:
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
    combinations = generate_combinations(num_characters)
    save_combinations(combinations)
    print("The combinations have been saved in the file combinations.txt.")

if __name__ == "__main__":
    main()
