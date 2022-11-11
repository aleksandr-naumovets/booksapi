float = 1.0
integer = 2
string = 'three'
boolean = True

print(float)
print(float + integer)
print(int(float) + integer)
# print(string + integer)
print(string + str(integer))
# print(int(string) + integer)
string = '3'
print(int(string) + integer)
integer = "Hey, how come I'm not a number anymore???"
print(integer)
print(boolean)
print(boolean + float)
boolean = False
print(boolean + float)

pets = ['dog', 'cat', 'dog', 'goldfish']
faves = [x for x in pets if x == 'dog']
print(faves)
fave = next((x for x in pets if x == 'dog'), None)
print(fave)
fave = next((x for  x in pets if x == 'horse'), None)
print(fave)

dogs = {
    '1' : {'name': 'Noir', 'breed': 'Schnoodle'},
    '2' : {'name': 'Bree', 'breed': 'Mutt'},
    '3' : {'name': 'Gigi', 'breed': 'Retriever'},
    '4' : {'name': 'Duchess', 'breed': 'Terrier'},
    '5' : {'name': 'Sparky', 'breed': 'Mutt'},
}

print("\n")
for x in dogs:
    print(dogs[x]['breed'])
mydogs = [dogs[x] for x in dogs if dogs[x]['breed'] == 'Mutt']
print(mydogs)

def get_my_dogs(breed): 
    return [dogs[x] for x in dogs if dogs[x]['breed'] == breed]

mydogs = get_my_dogs('Mutt')
print(mydogs)
mydogs = get_my_dogs('Retriever')
print(mydogs)
class Pet: 
    def __init__(self, name, species, noise):
        self.name = name
        self.species = species
        self.noise = noise

    def make_noise(self):
        print("I go " + self.noise)
        

my_dog = Pet('Noir', 'dog', "Woof!")
my_cat = Pet('Princess', 'cat', "Meow!")
my_pets = [my_cat, my_dog]
print("\n")
my_cat.make_noise()
my_dog.make_noise()
print(my_dog.noise)
print(my_dog.__dict__['noise'])
print(my_cat.noise)
print(my_pets[0].noise)
