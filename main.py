import Player                   # import the classes you want to use here
import pygame
import Item
import Customer
import sys
import random
import os

WIDTH = 1200     #game window width
HEIGHT = 600    #game window height

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# TODO: work out coordinates for middle of screen

player = Player.Player(0, 0, "Yoda")                         # create your objects
customer = Customer.Customer(1000, 500, "Chewy")

item1 = Item.Item('broc.jpeg', "broc", 200, 200)
item2 = Item.Item('broc.jpeg', "broc", 150, 200)
item3 = Item.Item('broc.jpeg', "broc", 300, 300)

running = True

def check_if_quit():                   # helper function by james just to check if they want to quit - ignore this :--)
    for event in pygame.event.get():   # handle every event since the last frame.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()              # quit the screen

def update():                        # helper function by james to update screen - ignore this :--)
    pygame.display.update()          # very important - update the screen
    screen.fill((255, 255, 255))     # fill the screen with white

# would be good to use whitebaord for this part - string concatenation
# this function is used to check values for testing purposes
def test_stuff():
    key = pygame.key.get_pressed()

    if key[pygame.K_b]:  # b - bag
       print(player.name + "'s Bag has the following in it: " + (', '.join(player.bag)))

    elif key[pygame.K_o]:  # o - order
       print("This is " + customer.name + "'s Order: " + (', '.join(customer.order)))

    #elif  what other info is nice to know?

while running:                   # while the game is running: do the following.....
    player.handle_keys()         # handle the players movement

    player.display(screen)       # draw your objects, and  tell the player what you are going to draw it on
    customer.display(screen)

    for item in Item.items.sprites(): # draw items
        item.display(screen)

    for item in Item.items.sprites(): # check if player touching items
        if player.touching(item):
            player.pick_up(item)
            item.kill()

    if player.touching(customer):   # check if player has gotten the order right
        if (set(customer.order)).issubset(set(player.bag)):
            print("done")

    test_stuff()

    update()                         # update the screen
    check_if_quit()                  # lastly we need to check they want to exit the game
