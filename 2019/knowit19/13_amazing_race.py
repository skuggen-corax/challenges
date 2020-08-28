"""
Arthur har følgande strategi:

    Roboten prioriterar alltid ubesøkte rom før besøkte.
    Roboten prioriterar ubesøkte rom i denne rekkefølga: nedover, høgre, venstre, oppover.
    Om det er ingen ubesøkte rom å gå til, går roboten tilbake til forrige rom.

Isaac programerar sin identisk, bortsett frå at roboten hans prioriterar å besøke nye rom i rekkefølga høgre, nedover, venstre, oppover

Eit enkelt rom i labyrinten har følgande eigenskapar:

    x - x-posisjon i labyrinten
    y - y-posisjon i labyrinten
    top - true om romet er stengt av ein vegg i retning oppover. false om det er passasje til tilstøytande rom.
    left - true om romet er stengt av ein vegg i retning venstre. false om det er passasje til tilstøytande rom.
    bottom - true om romet er stengt av ein vegg i retning nedover. false om det er passasje til tilstøytande rom.
    right - true om romet er stengt av ein vegg i retning høgre. false om det er passasje til tilstøytande rom.

Kor mange færre rom besøkte vinnarroboten? Gjentekne besøk til eit rom som er besøkt før skal ikkje tellast.
"""
import json

def search(maze, robot):
    steps = -1
    visited = set()
    queue = [start]

    while True:
        current = queue.pop()
        
        if current not in visited:
            visited.add(current)
            steps += 1
        else:
            continue

        if steps % 10000 == 0:
            print('step: ', steps, ' searching: ', current)

        if current == goal:
            return steps

        x = current[0]
        y = current[1]
        for keys in reversed(robot):
            if not maze[y][x][keys]:
                next_room = (x + directions[keys][0], y + directions[keys][1])
                if next_room not in visited:
                    queue.append(next_room)


with open('data/MAZE.TXT') as f:
    maze = json.load(f)


start = (0,0)
goal = (499, 499)

# earch order
arthur = ['bottom', 'right', 'left', 'top']
isaac = ['right', 'bottom', 'left', 'top']

directions = {'top': (0, -1), 'bottom': (0, 1), 'left': (-1, 0), 'right': (1, 0)}

isaac_steps = search(maze, isaac)
arthur_steps = search(maze, arthur)
diff = arthur_steps - isaac_steps


print('isaac: ', isaac_steps, ' arthur: ', arthur_steps, ' difference: ', abs(diff))