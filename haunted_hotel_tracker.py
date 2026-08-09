class HauntedHotel:
    def __init__(self):
        self.rooms = {}
        self.visited_rooms = set()
        self.sightings = []

    def add_ghost(self, room, ghost_name):
        self.rooms[room] = ghost_name

    def visit_room(self, room):
        self.visited_rooms.add(room)

        if room in self.rooms:
            ghost = self.rooms[room]
            self.sightings.append((room, ghost))

    def display(self):
        print("Ghost Rooms:")

        for room, ghost in self.rooms.items():
            if "ghost" in ghost.lower():
                print(room, ":", ghost)

        print("Visited Rooms:", self.visited_rooms)
        print("Sightings:", self.sightings)


hotel = HauntedHotel()

hotel.add_ghost(101, "Blue Ghost")
hotel.add_ghost(202, "Shadow Ghost")
hotel.add_ghost(303, "Invisible Spirit")
hotel.add_ghost(404, "Laughing Ghost")

hotel.visit_room(101)
hotel.visit_room(303)
hotel.visit_room(404)

hotel.display()
