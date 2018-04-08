import curses

import motor_control as motor

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.refresh()


DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

key = ''

max_y, max_x = stdscr.getmaxyx()
max_y -= 2
stdscr.addstr(max_y,10,"Hit 'q' to quit")

# set up console
for i in range(max_y):
	for u in range(max_x):
		if u == 0 or u == max_x-1:
			stdscr.addstr(i, u, "#")
		elif i == 0 or i == max_y-1:
			stdscr.addstr(i, u, "#")

max_x -= 1
max_y -= 1

x = int(max_x/2)
y = int(max_y/2)


def print_car(coor_x, coor_y):
	stdscr.addstr(coor_y, coor_x, "@")

	# delete other
	if coor_y - 1 != 0:
		stdscr.addstr(coor_y-1, coor_x, " ")
	if coor_y + 1 != max_y:
		stdscr.addstr(coor_y+1, coor_x, " ")
	if coor_x - 1 != 0:
		stdscr.addstr(coor_y, coor_x-1, " ")
	if coor_x + 1 != max_x:
		stdscr.addstr(coor_y, coor_x+1, " ")


print_car(x, y)

current_direction = 0

coor = (x, y)

while key != ord('q'):
	key = stdscr.getch()
	# stdscr.addch(20,25,key)
	stdscr.refresh()
	if key == curses.KEY_UP:
		motor.go_straight()
		pass
	elif key == curses.KEY_DOWN:
		motor.stop()
	elif key == curses.KEY_LEFT:
		motor.go_left()
		current_direction -= 1
		current_direction %= 8
	elif key == curses.KEY_RIGHT:
		motor.go_right()
		current_direction += 1
		current_direction %= 8

	else:
		continue

	# coor = (coor[0] + DIRECTIONS[current_direction][0], coor[1] + DIRECTIONS[current_direction][1])
	# stdscr.addstr(max_y-1, max_x-10, str(coor))

	if coor[0] == 0:
		coor = (1, coor[1])
	elif coor[0] == max_x:
		coor = (max_x-1, coor[1])

	if coor[1] == 0:
		coor = (coor[0], 0)
	elif coor[1] == max_y:
		coor = (coor[0], max_y-1)

	curses.flushinp()
	# print_car(coor[0], coor[1])

curses.endwin()
