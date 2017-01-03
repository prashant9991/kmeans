import random
import math
import sys

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

#num_of_clusetrs = len(sys.argv[1])
def kmeansAlgo():
    num_of_clusetrs = 3
    class DataPoint:
        def __init__(self, x, y, clusterNumber = -1):
            self.x = x
            self.y = y
            self.clusterNumber=clusterNumber

        def setX(self, x):
            self.x = x

        def getX(self):
            return self.x

        def setY(self, y):
            self.y = y

        def getY(self):
            return self.y

        def setCluster(self, clusterNumber):
            self.clusterNumber = clusterNumber

        def getCluster(self):
            return self.clusterNumber

    class Centroid:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def setX(self, x):
            self.x = x

        def getX(self):
            return self.x

        def setY(self, y):
            self.y = y

        def getY(self):
            return self.y


    data = []
    centroids = []
    lines = [line.rstrip('\n') for line in open('/Users/prashant.s/kmeans_clustering/filename')]
    no_data_points = len(lines)
    for index in range(no_data_points):
        print lines[index]
        mylist = lines[index].split(',')
        data.append(DataPoint(float(mylist[0]),float(mylist[1]),random.randint(0,num_of_clusetrs-1)))

    #for point in data:
     #   print("next point: ", point.getX(), point.getY(), point.getCluster())


    #Initialize cluster points
    for j in range(num_of_clusetrs):
        centroids.append(Centroid(data[j].getX(),data[j].getY()))


    #for centroid in centroids:
     #   print("next centroid: ", centroid.getX(), centroid.getY())

    def recalculate_centroids():
        totalX = 0
        totalY = 0
        totalInCluster = 0

        for j in range(num_of_clusetrs):
            for k in range(no_data_points):
                if(data[k].getCluster() == j):
                    totalX += data[k].getX()
                    totalY += data[k].getY()
                    totalInCluster += 1

            if(totalInCluster > 0):
                centroids[j].setX(totalX / totalInCluster)
                centroids[j].setY(totalY / totalInCluster)

        return

    # Calculate Euclidean distance.

    def update_clusters():
        isStillMoving = False

        for i in range(no_data_points):
            bestMinimum = 1000000
            currentCluster = 0

            for j in range(num_of_clusetrs):
                distance = get_distance(data[i].getX(), data[i].getY(), centroids[j].getX(), centroids[j].getY())
                if(distance < bestMinimum):
                    bestMinimum = distance
                    currentCluster = j
            oldcluster = data[i].getCluster()
            data[i].setCluster(currentCluster)

            if(data[i].getCluster() != oldcluster):
                data[i].setCluster(currentCluster)
                isStillMoving = True

        return isStillMoving


    iteration=0;
    isStillMoving = True
    while(isStillMoving):
        recalculate_centroids()
        iteration +=  1
        isStillMoving = update_clusters()

    for i in range(num_of_clusetrs):
        print("Cluster ", i, " includes:")
        for j in range(no_data_points):
            if(data[j].getCluster() == i):
                print("(", data[j].getX(), ", ", data[j].getY(), ")")
        print()

    print "No of Iteration  " , iteration
    for centroid in centroids:
        print("finally: ", centroid.getX(), centroid.getY())

    return centroids,iteration,data

if __name__=="__main__":kmeansAlgo()



