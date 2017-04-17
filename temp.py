#!/bin/python


# print all the moves here
m = 3  # input()

m_x = -1
m_y = -1
p_x = -1
p_y = -1

grid = ["---", "-m-", "p--"]


# !/bin/python
def displayPathtoPrincess(n, grid):
    for i in xrange(0, m):
        # line_str = raw_input().strip()
        line_str = grid[i]
        m_y = line_str.find("m")
        if m_y != -1:
            m_x = i
        p_y = line_str.find("p")
        if p_y != -1:
            p_x = i

    direction = "LEFT"
    if m_x > p_x:
        direction = "RIGHT"
        m_x, p_x = p_x, m_x

    for _ in xrange(m_x, p_x):
        print direction

    direction = "DOWN"
    if m_y > p_y:
        direction = "UP"
        m_y, p_y = p_y, m_y

    for _ in xrange(m_y, p_y):
        print direction


# print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
