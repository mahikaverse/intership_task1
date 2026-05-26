from pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m, start=None):

    if start is None:
        start = (m.rows, m.cols)

    open = PriorityQueue()
    open.put((h(start,(1,1)),
              h(start,(1,1)),
              start))

    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start,(1,1))

    apath = {}

    searchPath = []

    while not open.empty():

        currCell = open.get()[2]

        searchPath.append(currCell)

        if currCell == (1,1):
            break

        for d in 'ESNW':

            if m.maze_map[currCell][d] == True:

                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)

                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)

                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])

                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:

                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score

                    open.put((temp_f_score,
                              h(childCell,(1,1)),
                              childCell))

                    apath[childCell] = currCell

    fwdpath = {}

    cell = m._goal

    while cell != start:
        fwdpath[apath[cell]] = cell
        cell = apath[cell]

    return searchPath, apath, fwdpath


if __name__ == '__main__':

    m = maze(15,15)

    m.CreateMaze(theme=COLOR.dark)

    searchPath, apath, fwdpath = aStar(m)

    a = agent(m,
              footprints=True,
              color=COLOR.red,
              filled=True)

    b = agent(m,
              1,1,
              footprints=True,
              color=COLOR.blue,
              filled=True,
              goal=(m.rows,m.cols))

    c = agent(m,
              footprints=True,
              color=COLOR.green,
              filled=True)

    m.tracePath({a:searchPath}, delay=300)

    m.tracePath({b:apath}, delay=300)

    m.tracePath({c:fwdpath}, delay=300)

    textLabel(m, 'A* Search Path Length', len(searchPath))

    textLabel(m, 'A* Shortest Path Length', len(fwdpath)+1)

    m.run()