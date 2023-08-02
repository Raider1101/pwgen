import itertools

def generate_combinations(num_characters, use_letters=True, use_numbers=True, use_special_chars=True):
    characters = ""
    if use_letters:
        characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        characters += "0123456789"
    if use_special_chars:
        characters += "!@#$%&*"

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

    print("PWGen V1.2")
    print("Made By")
    print(banner)

def print_help():
    help_text = '''
Usage: python program.py [options]

Options:
  -h, --help            Display this help message and exit.
  -d, --default         Use default configurations.
  -c, --custom          Use custom configurations.
  -n, --number          Set the maximum number of characters per combination.
  -l, --letters         Include letters in combinations.
  -m, --numbers         Include numbers in combinations.
  -s, --special-chars   Include special characters in combinations.
'''

    print(help_text)

def prompt_configurations():
    print("Choose configurations:")
    use_letters = input("Use letters? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
    return use_letters, use_numbers, use_special_chars

def main():
    print_banner()

    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print_help()
            return
        elif sys.argv[1] == '-d' or sys.argv[1] == '--default':
            # Use default configurations
            use_letters = True
            use_numbers = True
            use_special_chars = True
        elif sys.argv[1] == '-c' or sys.argv[1] == '--custom':
            # Use custom configurations
            use_letters, use_numbers, use_special_chars = prompt_configurations()
        else:
            print("Invalid option.")
            return
    else:
        # No command-line arguments provided, prompt for configurations
        use_letters, use_numbers, use_special_chars = prompt_configurations()

    num_characters = int(input("Enter the maximum number of characters per combination: "))

    print("The wordlist is being generated! You can check the progress by opening the combinations.txt file. Thanks for using my tool!")

    generate_combinations(num_characters, use_letters, use_numbers, use_special_chars)

    print("The combinations have been saved in the file combinations.txt.")

if __name__ == "__main__":
    main()
