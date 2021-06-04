from menu import MenuItem

choice = int(input("Enter a value to see a demo: \n 1. Walmart - Playstation Price"
                   "\n 2. Wikipedia - Article and All Events\n 3. Wikipedia - Python Search "
                   "\n 4. Python Events \n 5. Sign Up\n"))
menu = MenuItem()
menu.interact(choice)
