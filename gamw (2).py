from gamelib import*
#game object
game = Game (1200,800,"Pixel Knight")
#bk object
bk = Image("darkcastle.png",game)
game.setBackground(bk)
bk.resizeTo(game.width,game.height)
play = Image("play.png",game)
play.resizeBy(40)
play.y += 200
story = Image("story.png", game)
story.resizeBy(40)
story.y += 300
hplay = Image("howtoplay.png",game)
hplay.resizeBy(-30)
hplay.y += 400
gameover = Image("gameover.png",game)
monsters = []#empty list
monsters1 = []
for index in range(20):#use a loop to add items
    monsters.append(Animation("hoon-kim-gob-boss.png",7,game,3360/7,480))
for index in range(20):#use a loop to set the positions and speed
    x = randint(999,5100)
    y = randint(400,600)
    monsters[index].moveTo(x, y)
    monsters[index].resizeBy(-70)
    monsters[index].setSpeed(3,90)
for index in range(20):#use a loop to add items
    monsters1.append(Animation("hoon-kim-troll-king (1).png",6,game,4032/6,672))
for index in range(20):#use a loop to set the positions and speed
    x = randint(999,5100)
    y = randint(400,600)
    monsters1[index].moveTo(x, y)
    monsters1[index].resizeBy(-80)
    monsters1[index].setSpeed(4,90)
knight = Animation("tumblr_inline_o3of9pprYp1r43rse_250.png",4,game,768/4,232,4)
knight1 = Animation("tumblr_inline_o3oj9t9fnc1r43rse_400.png",7,game,1960/7,188,2)
explosion = Animation("explosion1.png",22,game,1254/22,64)
explosion.resizeBy(40)
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    play.draw()
    story.draw()
    hplay.draw()
    game.drawText("PIXEL KNIGHT",520,480)
    game.drawText("PRESS PLAY TO START",520,500)
    knight.draw()
    knight.moveTo(400,500)
    monsters[index].visible = False
    if play.collidedWith(mouse) and mouse.LeftClick:
        monsters[index].visible = True
        game.over = True
    game.update(10)
game.over = False#continue the game with a new game loop
monstersPassed = 0
while not game.over and knight.health > 1:
    game.processInput()
    bk.draw()
    explosion.draw()
    game.drawText("Level 1",320,280)
    game.scrollBackground("left",1)
    for index in range(20):
        explosion.moveTo(monsters[index].x,monsters[index].y)
        if monsters[index].isOffScreen("left") and monsters[index].visible:
            monsters[index].visible = False
        if monstersPassed >= 20:
            game.over = True
    knight.draw()
    knight1.draw()
    knight1.visible = False
    explosion.visible = False
    if keys.Pressed[K_SPACE]:
        knight1.visible = True
        knight1.moveTo(500,500)
        knight.visible = False
    if knight1.visible == False:
        knight.visible = True
    game.displayScore()
    for index in range(20):
        monsters[index].move()
        if monsters[index].collidedWith(knight1):
            game.score +=1
            monsters[index].visible = False
            explosion.visible = True
    for index in range(20):
        if monsters[index].collidedWith(knight):
            knight.health -= 1
            explosion.visible = True
            monsters[index].visible = False        
        if explosion.collidedWith(knight) or explosion.collidedWith(knight1):
            explosion.visible = False
        if knight.health < 0:
            game.over = True
        if game.over == True:
            monsters[index].visible = False
    game.drawText("Lives: " + str(knight.health),knight.x - 90,knight.y + 40)
    game.update(90)
game.over = False
monsters1Passed = 0
while not game.over and knight.health > 1:
    game.processInput()
    bk.draw()
    explosion.draw()
    game.drawText("Level 2",300,280)
    game.scrollBackground("left",1)
    knight.draw()
    knight1.draw()
    knight1.visible = False
    explosion.visible = False
    for index in range(20):
        explosion.moveTo(monsters1[index].x,monsters1[index].y)
        if monsters1[index].isOffScreen("left") and monsters1[index].visible:
            monsters1[index].visible = False
        if monsters1Passed >= 20:
            game.over = True
    for index in range(20):
        monsters1[index].move()
        if monsters1[index].collidedWith(knight1):
            game.score +=1
            monsters1[index].visible = False
            explosion.visible = True
        else:
            knight.health -=1
    for index in range(20):
        if monsters1[index].collidedWith(knight):
            knight.health -= 1
            explosion.visible = True
            monsters1[index].visible = False        
        if explosion.collidedWith(knight) or explosion.collidedWith(knight1):
            explosion.visible = False
        if knight.health < 0:
            game.over = True
        if game.over == True:
            monsters1[index].visible = False
        if keys.Pressed[K_SPACE]:
            knight1.visible = True
            knight1.moveTo(500,500)
            knight.visible = False
        if knight1.visible == False:
            knight.visible = True
    game.drawText("Lives: " + str(knight.health),knight.x - 90,knight.y + 40)
gameover.draw()
game.drawText("Press ENTER to Quit",520,330)
game.update()
game.wait(K_RETURN)   
game.quit()

