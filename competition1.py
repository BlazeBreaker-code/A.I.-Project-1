import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import shapely.geometry
import descartes
import math
from matplotlib import path
from queue import PriorityQueue
import operator

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(12, 6.5)

plt.plot(183, 70, marker=".")
plt.plot(950, 432, marker=".")
plt.text(170, 70, 'S')
plt.text(955, 432, 'G')

# Points for the polygon shapes.
points1 = ([214, 1], [214, 113], [568, 113], [568, 1])
points2 = ([197, 216], [178, 332], [306, 447], [388, 335], [321, 186])
points3 = ([392, 180], [491, 180], [440, 357])
points4 = ([497, 296], [496, 438], [585, 448], [647, 383])
points5 = ([620, 76], [695, 146], [585, 237])
points6 = ([667, 204], [815, 204], [815, 435], [667, 435])
points7 = ([751, 56], [751, 139], [831, 191], [892, 138], [892, 52], [821, 15])
points8 = ([834, 405], [909, 177], [928, 395], [888, 438])

l = []
# Had to create a bunch of vertices that hover the polygon in order to use an intersect function to see possible neighbors for a given vertex.
coordsa1 = tuple([213.9, 1])
coordsa2 = tuple([213.9, 113])
coordsa3 = tuple([568.1, 113.1])
coordsa4 = tuple([568.1, 1])

coordsb1 = tuple([197, 215.9])
coordsb2 = tuple([177.9, 332])
coordsb3 = tuple([306, 447.1])
coordsb4 = tuple([388.1, 335])
coordsb5 = tuple([321, 185.9])

coordsc1 = tuple([392, 179.9])
coordsc2 = tuple([491, 179.9])
coordsc3 = tuple([440, 357.1])

coordsd1 = tuple([497, 295.9])
coordsd2 = tuple([496, 438.1])
coordsd3 = tuple([585, 448.1])
coordsd4 = tuple([647, 382.9])

coordse1 = tuple([620, 75.9])
coordse2 = tuple([695, 145.9])
coordse3 = tuple([584.9, 237])

coordsf1 = tuple([667, 203.9])
coordsf2 = tuple([815, 203.9])
coordsf3 = tuple([815, 435.1])
coordsf4 = tuple([667, 435.1])

coordsg1 = tuple([751, 55.9])
coordsg2 = tuple([750.9, 139])
coordsg3 = tuple([831, 191.1])
coordsg4 = tuple([892, 138.1])
coordsg5 = tuple([892, 51.9])
coordsg6 = tuple([821, 14.9])

coordsh1 = tuple([833.9, 405])
coordsh2 = tuple([909, 176.9])
coordsh3 = tuple([928.1, 395])
coordsh4 = tuple([888, 438.1])

coordsg = tuple([949.9, 432])

l.append(coordsa1)
l.append(coordsa2)
l.append(coordsa3)
l.append(coordsa4)

l.append(coordsb1)
l.append(coordsb2)
l.append(coordsb3)
l.append(coordsb4)
l.append(coordsb5)

l.append(coordsc1)
l.append(coordsc2)
l.append(coordsc3)

l.append(coordsd1)
l.append(coordsd2)
l.append(coordsd3)
l.append(coordsd4)

l.append(coordse1)
l.append(coordse2)
l.append(coordse3)

l.append(coordsf1)
l.append(coordsf2)
l.append(coordsf3)
l.append(coordsf4)

l.append(coordsg1)
l.append(coordsg2)
l.append(coordsg3)
l.append(coordsg4)
l.append(coordsg5)
l.append(coordsg6)

l.append(coordsh1)
l.append(coordsh2)
l.append(coordsh3)
l.append(coordsh4)

l.append(coordsg)

polygon = plt.Polygon(points1)
polygon2 = plt.Polygon(points2)
polygon3 = plt.Polygon(points3)
polygon4 = plt.Polygon(points4)
polygon5 = plt.Polygon(points5)
polygon6 = plt.Polygon(points6)
polygon7 = plt.Polygon(points7)
polygon8 = plt.Polygon(points8)

polygon1e = shapely.geometry.Polygon(points1)
polygon2e = shapely.geometry.Polygon(points2)
polygon3e = shapely.geometry.Polygon(points3)
polygon4e = shapely.geometry.Polygon(points4)
polygon5e = shapely.geometry.Polygon(points5)
polygon6e = shapely.geometry.Polygon(points6)
polygon7e = shapely.geometry.Polygon(points7)
polygon8e = shapely.geometry.Polygon(points8)

ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

ax.add_patch(polygon)
ax.add_patch(polygon2)
ax.add_patch(polygon3)
ax.add_patch(polygon4)
ax.add_patch(polygon5)
ax.add_patch(polygon6)
ax.add_patch(polygon7)
ax.add_patch(polygon8)

# Checks if there is a x element within a list.
def commonelems(x, y):
    common = 0
    if x in y:
            common = 1
    if(not common):
        return False
    else:
        return True

# A star algorithm using a priority queue and 2 lists in order to have a depth of two to find the best path.
def astar(li, start, g, l, new_list1, prev_neigh_list, prev_neigh_list2, end):
    neighbor = PriorityQueue()
    new_list2 = []
    for x in range(len(li)):
        hn = math.sqrt(((li[x][0] - 949.9) ** 2) + ((li[x][1] - 432) ** 2))
        gn = math.sqrt(((li[x][0] - start[0]) ** 2) + ((li[x][1] - start[1]) ** 2)) + g
        fn = hn + gn
        neighbor.put((fn, li[x]))
    # Takes the lowest fn vertex and uses that from the priority queue
    best_node = tuple(neighbor.get()[1])
    gn = math.sqrt(((best_node[0] - start[0]) ** 2) + ((best_node[1] - start[1]) ** 2)) + g
    # Other neighbors are then put into a list based on fn from the priority queue, this is the hold list.
    # Then checks depth 2 list to see if there is a better path within this list.
    while not neighbor.empty():
        new_list2.append(neighbor.get()[1])
    if prev_neigh_list2:
        if (commonelems(new_list1[len(new_list1) -1] ,prev_neigh_list2)):
            del new_list1[len(new_list1) - 2]
    prev_neigh_list2 = prev_neigh_list
    prev_neigh_list = new_list2
    actions(best_node, l, gn, new_list1, prev_neigh_list, prev_neigh_list2, end)

# Takes vertex and finds the possible neighbors then gives the list to the a star function
def actions(start, l, gn, new_list1, prev_neigh_list, prev_neigh_list2, end):
    if (start == end):
        new_list1.append(end)
        print(new_list1)
        verts = new_list1
        pb = path.Path(verts)
        plt.gca().add_patch(patches.PathPatch(pb, edgecolor="green", fill=None, linewidth=2.0))
        return
    new_list =[]
    for x in range(len(l)):
        if(l[x] != start):
            someline = shapely.geometry.LineString([start, l[x]])
            if (not (someline.intersects(polygon1e) or someline.intersects(polygon2e) or someline.intersects(polygon3e) or someline.intersects(polygon4e) or someline.intersects(polygon5e) or someline.intersects(polygon6e) or someline.intersects(polygon7e) or someline.intersects(polygon8e))):
                new_list.append(l[x])
    new_list1.append(start)
    astar(new_list, start, gn, l, new_list1, prev_neigh_list, prev_neigh_list2, end)

def main():
    start = tuple([183,70])
    end = tuple([949.9, 432])
    new_list1 = []
    prev_neigh_list = []
    prev_neigh_list2 = []
    actions(start, l, 0, new_list1, prev_neigh_list, prev_neigh_list2, end)
    plt.show()

if __name__ == '__main__':
    main()
