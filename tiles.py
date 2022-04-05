import pygame, csv, os

"""Responsible for dealing with the loading of Tiles and other Obstacles"""
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = x , y

    #Draws the Tiles on the Screen
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))  

"""Sets and takes in the tile data and information"""
class TileMap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 64
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)

        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    
    def draw_map(self,surface):
        surface.blit(self.map_surface, (0,0)) #Draws map onto the screen

    #Loads the Tiles onto the screen
    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
    
    #Reads the CSV Files responsible for loading the level stages
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter = ",")
            for row in data:
                map.append(list(row))
            
        return map
    
    #Loads the tiles via the information given within the CSV Files and appends it to a Tile list
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0,0
        for row in map:
            x = 0
            for tile in row:

                if tile == "-1":
                    pass

                if tile == "0":
                    tiles.append(Tile("S1WallCorner1.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "1":
                    tiles.append(Tile("S1wall1.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "2":
                    tiles.append(Tile("S1wall1.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "3":
                    tiles.append(Tile("S1wall2.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "4":
                    tiles.append(Tile("S1WallCorner2.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "5":
                    tiles.append(Tile("S1Door.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "8":
                    tiles.append(Tile("S1Wall3.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "12":
                    tiles.append(Tile("S1Wall3.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "16":
                    tiles.append(Tile("S1Wall3.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "20":
                    tiles.append(Tile("S1Wall3.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "24":
                    tiles.append(Tile("S1Wall4.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "28":
                    tiles.append(Tile("S1Wall4.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "32":
                    tiles.append(Tile("S1WallCorner3.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "33":
                    tiles.append(Tile("S1wall1.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "34":
                    tiles.append(Tile("S1wall1.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "35":
                    tiles.append(Tile("S1wall2.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == "36":
                    tiles.append(Tile("S1WallCorner4.png", x * self.tile_size, y * self.tile_size, self.spritesheet))
                x += 1

            y += 1
        self.map_w, self.map_h = x * self.tile_size , y * self.tile_size

        return tiles

