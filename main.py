import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_is_on = True
while game_is_on:
  time.sleep(level.level_speed)
  screen.update()

  car.create_car()
  car.move_cars()

  #Detect collision with car
  for car_object in car.all_cars:
    if car_object.distance(player) < 19.5:
      print(car_object.distance(player))
      game_is_on = False
      screen.write('game over', align='center', font=('Courier', 40, 'normal'))
    
  #Detect win
  if player.has_crossed():
    player.move_start_position()
    level.increase_level()

screen.mainloop()