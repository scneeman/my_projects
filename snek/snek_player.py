from snek_ball import snek_ball

class snek_player:

    def __init__(self, num_param):
        self.rad = 10
        self.top_x = 200
        self.top_y = 200
        self.pieces = []
        for i in range(num_param):
            if i == 0:
                temp_col = (255, 0, 0)
            else:
                temp_col = (i, i, i)
            self.pieces.append(snek_ball(self.rad, self.top_x, self.top_y + i*2*self.rad, 1, temp_col))

    def draw_player(self, screen):
        for i in range(len(self.pieces)-1, -1, -1):
            self.pieces[i].draw(screen)
    
    def move_player(self):
        for piece in self.pieces:
            piece.move()
        # other than lead piece,
        # each successive piece takes the direction of the one before
        for i in range(len(self.pieces)-1, 0, -1):
            self.pieces[i].dir = self.pieces[i-1].dir
        
    # only the lead piece changes direction immediately       
    def change_dir(self, new_dir):
        self.pieces[0].dir = new_dir
    
    def add_piece(self):
        # finding the position of the end piece
        temp_place = len(self.pieces)-1
        temp_x = self.pieces[temp_place].x
        temp_y = self.pieces[temp_place].y
        temp_dir = self.pieces[temp_place].dir
        
        # add/subtract depending on direction
        temp_x_extra = 0
        temp_y_extra = 0    
        if self.pieces[temp_place].dir == 1:
            temp_y_extra = 2*self.rad
        elif self.pieces[temp_place].dir == 2:
            temp_x_extra = -2*self.rad 
        elif self.pieces[temp_place].dir == 3:
            temp_y_extra = -2*self.rad
        elif self.pieces[temp_place].dir == 4:
            temp_x_extra = 2*self.rad
        
        # appending to the list
        if len(self.pieces)<250:
            temp_color = (len(self.pieces), len(self.pieces), len(self.pieces))
        else:
            temp_color = (250, 250, 250)
        self.pieces.append(snek_ball(self.rad, temp_x + temp_x_extra, temp_y + temp_y_extra, temp_dir, temp_color))
