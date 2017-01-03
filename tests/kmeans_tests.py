
import nose.tools as nt  # contains testing tools like ok_, eq_, etc.
import kmeans.kmeans

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def testDistaceFromCentroids():
    initK = 10
    (centroids, iters, points) = kmeans.kmeans.kmeansAlgo()
    for i in range(len(points)):
        cluster = points[i].getCluster()
        centroid = centroids[cluster]
        internalDist = kmeans.kmeans.get_distance(centroid.getX(),centroid.getY(), points[i].getX(),points[i].getY())
        for k in range(len(centroids)):
            if k != cluster:
                centroid=centroids[k]
                #distance of point to it's own centroid should be less than all other centroids
                assert (kmeans.kmeans.get_distance(centroid.getX(),centroid.getY(), points[i].getX(),points[i].getY()) >= internalDist)


