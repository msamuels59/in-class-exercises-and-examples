# try to represent a musician with a dictionary

musician = [{
    'name': 'Andrew Bird',
    'instrument': ['violin', 'whistle'],
    'record label': 'Merge',
    'bands': []
    },
    {

    }]


#as we reach the limitations of dictionaries to represnt data we can move to classes

class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'{self.name}: {self.instrument}'


#when I create an object that's an element of a class, its called an instance
#writing name of the clas with () causes the __init__ method to be called 

snoop = Musician('Snoop Dogg', 'MC')
print(snoop)
jewel = Musician("Jewel", "guitar")
print(jewel)

class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return self.name

    @property
    def show_members(self):
        print(f'The members of {mouse_rat.name} are: ', [f'{member}' for member in mouse_rat.members])


mouse_rat = Band('Mouse Rat')

mouse_rat.members.extend([snoop,jewel])

#create a new musician instance
andy = Musician('Andy Dwierr', 'also guitar')
ron = Musician('Ron Swanson', 'smooth jazz sax')
flea = Musician('Flea from RHCP', 'bass')

#add those musicians to the list

new_members = [andy, ron, flea]

mouse_rat.members.extend(new_members)

mouse_rat.show_members

