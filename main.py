import pygame
import math
import random
import copy

pygame.init()
height, width = 400, 400
screen = pygame.display.set_mode((width, height))
no_move, up, up_right, right, down_right, down, down_left, left, up_left = 0, 1, 2, 3, 4, 5, 6, 7, 8
font = pygame.font.SysFont('Arial', 10)
bot_count = 500
Factor=400
frame_optimize = 3
input_l=10
layer1=20
layer2=20
output_l=4

def sigmoid(x):
    y=math.exp(x)
    return y/(y+1)

class neuron_connection:
    def __init__(self, no_of_wt):
        self.wt = []
        self.offset = None
        self.value = None
        for i in range(no_of_wt):
            self.wt.append(random.random())
        self.offset = random.random()
        self.value = 0

    def change_wt(self, wt):
        self.wt = wt

    def change_off(self, of):
        self.offset = of

    def change_val(self, val):
        self.value = val

    def print_it(self):
        print(len(self.wt))


class bot:
    def __init__(self, inp_n_size, l1_n_size, l2_n_size, op_n_size):
        self.inputLayer = []
        self.neurons_l1 = []
        self.neurons_l2 = []
        self.outputLayer = []
        self.btn_up = -1000
        self.btn_down = -1000
        self.btn_right = -1000
        self.btn_left = -1000
        self.is_active = True
        self.checkPoint = 0
        self.ex_pos = [0, 0]
        self.ex_pos2 = [0, 0]
        self.angle=0
        for i in range(inp_n_size):
            self.inputLayer.append(neuron_connection(1))
        for i in range(l1_n_size):
            self.neurons_l1.append(neuron_connection(inp_n_size))
        for i in range(l2_n_size):
            self.neurons_l2.append(neuron_connection(l1_n_size))
        for i in range(op_n_size):
            self.outputLayer.append(neuron_connection(l2_n_size))
        self.pos_x = 30
        self.pos_y = 30
        self.score = 0

    def die_if_inactive(self):
        if self.ex_pos2[0] == self.pos_x and self.ex_pos2[1] == self.pos_y:
            self.is_active = False

    def get_direction(self):
        self.btn_up = self.outputLayer[0].value
        self.btn_right = self.outputLayer[1].value
        self.btn_down = self.outputLayer[2].value
        self.btn_left = self.outputLayer[3].value
        temp_dir = (self.btn_up, self.btn_right, self.btn_down, self.btn_left)
        if self.is_active:
            pass
            #print(temp_dir)
        temp_max = max(temp_dir)
        if self.btn_up == temp_max:
            return up
        if self.btn_right == temp_max:
            return right
        if self.btn_down == temp_max:
            return down
        if self.btn_left == temp_max:
            return left
        return 0

    def move(self, direction):
        self.ex_pos2 = self.ex_pos
        self.ex_pos = (self.pos_x, self.pos_y)
        if self.is_active:
            if direction == right:
                self.pos_x += frame_optimize
            elif direction == left:
                self.pos_x -= frame_optimize
            elif direction == up:
                self.pos_y -= frame_optimize
            elif direction == down:
                self.pos_y += frame_optimize
        self.die_if_inactive()

    def find_distance(self):
        if screen.get_at((self.pos_x, self.pos_y)) == (150, 255, 150, 255):
            if self.pos_x < 199:
                self.checkPoint = 2
            elif self.pos_x > 199 and self.pos_x < 280:
                self.checkPoint = 1
            else:
                self.checkPoint = 3
        arr = []
        pos = 10
        while self.pos_y - pos > -1:  # for up
            if screen.get_at((self.pos_x +10 , self.pos_y - pos)) == (0, 0, 0, 255) or screen.get_at((self.pos_x -10 , self.pos_y - pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_y - pos > -1 or self.pos_x + pos < 401:  # for up-right
            if screen.get_at((self.pos_x + pos, self.pos_y - pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_x + pos < 401:  # for right
            if screen.get_at((self.pos_x + pos, self.pos_y+10)) == (0, 0, 0, 255) or screen.get_at((self.pos_x + pos, self.pos_y-10)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_y + pos < 401 or self.pos_x + pos < 401:  # for down-right
            if screen.get_at((self.pos_x + pos, self.pos_y + pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_y + pos < 401:  # for down
            if screen.get_at((self.pos_x+10, self.pos_y + pos)) == (0, 0, 0, 255) or screen.get_at((self.pos_x-10, self.pos_y + pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_y + pos < 401 or self.pos_x - pos > -1:  # for down-left
            if screen.get_at((self.pos_x - pos, self.pos_y + pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_x - pos > -1:  # for left
            if screen.get_at((self.pos_x - pos, self.pos_y + 10)) == (0, 0, 0, 255) or screen.get_at((self.pos_x - pos, self.pos_y + 10)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        pos = 10
        while self.pos_x - pos > -1 or self.pos_y - pos > -1:  # for up-left
            if screen.get_at((self.pos_x - pos, self.pos_y - pos)) == (0, 0, 0, 255):
                arr.append(pos)
                break
            pos += 1
        arr.append(self.get_score())
        return arr

    def input_layer(self):
        arr = self.find_distance()
        if 10 in arr:
            self.is_active = False
        for i in range(len(self.inputLayer)-1):
            self.inputLayer[i].value = sigmoid((arr[i]-10)/Factor)
        self.inputLayer[i+1].value = self.angle

    def draw_bot(self, y=0):
        if self.is_active:
            pygame.draw.rect(screen, (255, 150 - y * 150, 150 - y * 150),
                             ((self.pos_x - 10, self.pos_y - 10), (20, 20)))
            pygame.draw.rect(screen, (100, 50 - y * 50, 50 - y * 50), ((self.pos_x - 10, self.pos_y - 10), (20, 20)), 1)

    def update_layers(self):
        self.input_layer()
        for j in range(len(self.neurons_l1)):
            sum = 0
            for k in range(len(self.neurons_l1[j].wt)):
                sum += self.neurons_l1[j].wt[k] * self.inputLayer[k].value
            self.neurons_l1[j].value = sigmoid(sum + self.neurons_l1[j].offset)
        for j in range(len(self.neurons_l2)):
            sum = 0
            for k in range(len(self.neurons_l2[j].wt)):
                sum += self.neurons_l2[j].wt[k] * self.neurons_l1[k].value
            self.neurons_l2[j].value = sigmoid(sum + self.neurons_l2[j].offset)

        for j in range(len(self.outputLayer)):
            sum = 0
            for k in range(len(self.outputLayer[j].wt)):
                sum += self.outputLayer[j].wt[k] * self.neurons_l2[k].value
            self.outputLayer[j].value = sigmoid(sum + self.outputLayer[j].offset)

    def calculate_score(self):
        if self.checkPoint == 0:
            ptx = 250.5
            pty = 360.5
        elif self.checkPoint == 1:
            ptx = 180.5
            pty = 150.5
        elif self.checkPoint == 2:
            ptx = 340.5
            pty = 340.5
        else:
            ptx = -1000.5
            pty = -1000.5
        self.score = 1000 * (self.checkPoint + 1) - 2 * math.sqrt(
            math.pow(self.pos_x - ptx, 2) + math.pow(self.pos_y - pty, 2))
        self.angle=math.atan((pty-self.pos_y)/(ptx-self.pos_x))

    def get_score(self):
        self.calculate_score()
        return self.score

    def new_gen(self, bot_val, gen_no):
        self.btn_up = -1000
        self.btn_down = -1000
        self.btn_right = -1000
        self.btn_left = -1000
        self.is_active = True
        self.checkPoint = 0
        self.pos_x = 30
        self.pos_y = 30
        for j in range(len(self.inputLayer)):
            temp_wt = []
            for i in range(len(self.inputLayer[j].wt)):
                temp_wt.append(bot_val.inputLayer[j].wt[i] + (random.random() - 0.5) / gen_no)
            self.inputLayer[j].change_wt(temp_wt)
            self.inputLayer[j].change_off(bot_val.inputLayer[j].offset+(random.random()-0.5)/gen_no)
        for j in range(len(self.neurons_l1)):
            temp_wt = []
            for i in range(len(self.neurons_l1[j].wt)):
                temp_wt.append(bot_val.neurons_l1[j].wt[i] + (random.random() - 0.5) / gen_no)
            self.neurons_l1[j].change_wt(temp_wt)
            self.neurons_l1[j].change_off(bot_val.neurons_l1[j].offset + (random.random() - 0.5) / gen_no)
        for j in range(len(self.neurons_l2)):
            temp_wt = []
            for i in range(len(self.neurons_l2[j].wt)):
                temp_wt.append(bot_val.neurons_l2[j].wt[i] + (random.random() - 0.5) / gen_no)
            self.neurons_l2[j].change_wt(temp_wt)
            self.neurons_l2[j].change_off(bot_val.neurons_l2[j].offset+(random.random()-0.5)/gen_no)
        for j in range(len(self.outputLayer)):
            temp_wt = []
            for i in range(len(self.outputLayer[j].wt)):
                temp_wt.append(bot_val.outputLayer[j].wt[i] + (random.random() - 0.5) / gen_no)
            self.outputLayer[j].change_wt(temp_wt)
            self.outputLayer[j].change_off(bot_val.outputLayer[j].offset+(random.random()-0.5)/gen_no)

    def equals(self,bot):
        for i in range(len(self.neurons_l1)):
            for j in range(len(self.neurons_l1[i].wt)):
                self.neurons_l1[i].wt[j]=bot.neurons_l1[i].wt[j]
        for i in range(len(self.neurons_l2)):
            for j in range(len(self.neurons_l2[i].wt)):
                self.neurons_l2[i].wt[j]=bot.neurons_l2[i].wt[j]
        for i in range(len(self.outputLayer)):
            for j in range(len(self.outputLayer[i].wt)):
                self.outputLayer[i].wt[j]=bot.outputLayer[i].wt[j]
best_bot=bot(input_l,layer1,layer2,output_l)


def store_bot(filename="Best",bot=0):
    global best_bot
    if bot !=0:
        bot_here=bot
    else:
        bot_here=best_bot
    file1 = open(str(filename) + ".txt", "w")
    '''file1.write(str(len(best_bot.neurons_l1[0].wt))+"\n")
    file1.write(str(len(best_bot.neurons_l1))+"\n")
    file1.write(str(len(best_bot.neurons_l2))+"\n")
    file1.write(str(len(best_bot.outputLayer))+"\n")
    file1.write("change\n")'''
    for i in range(len(bot_here.inputLayer)):
        file1.write(str(bot_here.inputLayer[i].offset)+"\n")
    for i in range(len(bot_here.neurons_l1)):
        for j in range(len(bot_here.neurons_l1[0].wt)):
            file1.write(str(bot_here.neurons_l1[i].wt[j]) + "\n")
        file1.write(str(bot_here.neurons_l1[i].offset)+"\n")
    for i in range(len(bot_here.neurons_l1)):
        for j in range(len(bot_here.neurons_l2[0].wt)):
            file1.write(str(bot_here.neurons_l2[i].wt[j]) + "\n")
        file1.write(str(bot_here.neurons_l2[i].offset)+"\n")
    for i in range(len(bot_here.outputLayer)):
        for j in range(len(bot_here.outputLayer[0].wt)):
            file1.write(str(bot_here.outputLayer[i].wt[j]) + "\n")
        file1.write(str(bot_here.outputLayer[i].offset)+"\n")
    file1.close()

def count_size_file(filename):
    file1 = open(str(filename)+".txt","r")
    layer=[]
    i=0
    for data in file1:
        i+=1
        if i==4:
            break
        layer.append(int(data))
    file1.close()
    return layer


def getStored_bot(filename="Best"):
    file1 = open(str(filename) + ".txt", "r")
    #size=count_size_file(filename)
    size=[10,20,20,4]
    #for i in range(4): file1.readline()
    temp_bot = bot(size[0], size[1], size[2], size[3])
    for i in range(size[0]):
        temp_bot.inputLayer[i].offset=float(file1.readline())
    for i in range(size[1]):
        for j in range(size[0]):
            temp_bot.neurons_l1[i].wt[j]=float(file1.readline())
        temp_bot.neurons_l1[i].offset=float(file1.readline())
    for i in range(size[2]):
        for j in range(size[1]):
            temp_bot.neurons_l2[i].wt[j]=float(file1.readline())
        temp_bot.neurons_l2[i].offset = float(file1.readline())
    for i in range(size[3]):
        for j in range(size[2]):
            temp_bot.outputLayer[i].wt[j]=float(file1.readline())
        temp_bot.outputLayer[i].offset=float(file1.readline())
    file1.close()
    return temp_bot


def draw_map():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (150, 255, 150), ((201, 341), (78, 58)))
    pygame.draw.rect(screen, (150, 255, 150), ((121, 121), (78, 78)))
    pygame.draw.rect(screen, (150, 255, 150), ((341, 341), (118, 58)))
    pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (width, width)), 10)
    # pt_list = ((60, 0), (60, 340), (200, 340), (200, 260), (120, 200), (120, 120), (200, 120), (400, 260))
    pt_list = ((150, 0), (80, 200), (120, 200), (200, 340))
    pt_list = ((100,0),(120, 100), (80, 200), (120, 200), (200, 340))
    pt_list2 = ((120,120),(200,120),(200,140),(400,300))
    pt_list3 = ((0,60),(60,60), (10, 200), (10, 240), (80, 260), (160, 400),(280,400),(280,340),(200,200),(340,340),(340,400))
    pygame.draw.lines(screen, (0, 0, 0), False, pt_list, 6)
    pygame.draw.lines(screen, (0, 0, 0), False, pt_list2, 6)
    pygame.draw.lines(screen, (0, 0, 0), False, pt_list3, 6)


def are_available(bots):
    count = 0
    for bot in bots:
        if bot.is_active:
            count += 1
    return count


def get_max_index(bots):
    val = []
    for i in bots:
        val.append(i.get_score())
    max_ind_arr = []
    if len(val) > 10:
        for i in range(8):
            max_val = max(val)
            ind = val.index(max_val)
            max_ind_arr.append(i + ind)
            val.remove(max_val)
    while len(max_ind_arr) < 10:
        max_val = max(val)
        ind = val.index(max_val)
        add = True
        for j in range(i):
            if int(max_val*5) == int(bots[j].get_score()*5):
                add = False
        if 10-len(max_ind_arr)==len(val):
            add=True
        if add:
            max_ind_arr.append(i + ind)
        val.remove(max_val)
    return max_ind_arr


def replay_max_index(bots):
    val = []
    for i in bots:
        val.append(i.get_score())
    max_val = max(val)
    ind = val.index(max_val)
    bots[ind].pos_x = 30
    bots[ind].pos_y = 30
    bots[ind].is_active = True
    return ind


def ex_bot_return(bot1):
    bot2 = None
    bot2 = bot1
    return bot2


def kill_all(bots):
    for i in range(bot_count):
        bots[i].is_active = False

def get_rank_new():
    r=random.random()
    if r<0.1:return 10
    if r < 0.3: return 0
    if r < 0.45: return 1
    if r < 0.55: return 2
    if r < 0.65: return 3
    if r < 0.7: return 4
    if r < 0.75: return 5
    if r < 0.8: return 6
    if r < 0.85: return 7
    if r < 0.9: return 8
    return 9

def new_gen(bots, gen=0):
    if gen!=0:
        gen_no=3*math.pow(gen,1/3)-2
        global best_bot
        best_bot.calculate_score()
        max_index = get_max_index(bots)
        high_bot = bots[max_index[0]]
        if best_bot.score < high_bot.score:
            store_bot("Best",high_bot)
            best_bot=copy.deepcopy(high_bot)
            best_bot.calculate_score()
            print("best: ",best_bot.score," in gen: ",gen)
        store_bot("High", high_bot)
        rand_bot=bot(input_l,layer1,layer2,output_l)
        for i in range(bot_count):
            r=get_rank_new()
            if r<7:
                bots[i].new_gen(bots[max_index[r]], gen_no)
            elif r<9:
                bots[i].new_gen(bots[max_index[r]],gen)
            elif r==9:
                bots[i].new_gen(rand_bot,gen_no)
            elif r==10:
                bots[i].new_gen(best_bot,gen_no)
    else:
        best_bot=getStored_bot("Epic")
        for i in range(bot_count):
            bots[i].new_gen(best_bot,100)
    return best_bot.score

def replay():
    bot_here=getStored_bot("High")
    
    global best_bot
    global frame_optimize
    temp_frame=frame_optimize
    frame_optimize=1
    while bot_here.is_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
        draw_map()
        text = font.render("Alive: " + str(bot_alive_count) + " Gen: " + str(gen_no)+" Best val: "+str(best_score), True, (0, 0, 0))
        screen.blit(text, (150, 10))
        bot_here.update_layers()
        bot_here.draw_bot()
        bot_here.move(bot_here.get_direction())
        pygame.display.update()
        pygame.time.delay(25)
    frame_optimize=temp_frame

best_score=0
bots = []
for i in range(bot_count):
    bots.append(bot(input_l,layer1,layer2,output_l))
bots_copy=copy.deepcopy(bots)
running = True
best_bot=getStored_bot("High")
#new_gen(bots)
if bots == bots_copy:
    running=False
btn = no_move
gen_no = 0
while running:
    draw_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                replay()
            if event.key == pygame.K_RETURN:
                gen_no += 1
                new_gen(bots, gen_no)
        pos = pygame.mouse.get_pos()
    for i in range(bot_count):
        bots[i].update_layers()
        bots[i].draw_bot()
        move = bots[i].get_direction()
        # print(bots[i].get_score(), " ", dirn)
        # bots[i].pos_x, bots[i].pos_y = pos
        bots[i].move(move)
    bot_alive_count = are_available(bots)
    text = font.render("Alive: " + str(bot_alive_count) + " Gen: " + str(gen_no)+" Best val: "+str(best_score), True, (0, 0, 0))
    
    screen.blit(text, (150, 10))
    if not bot_alive_count:
        gen_no += 1
        best_score=int(new_gen(bots, gen_no))
    pygame.display.update()
