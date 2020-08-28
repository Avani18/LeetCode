# Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

def checkStraightLine(coordinates):
        m = len(coordinates)
        if (m == 2):
            return True
        x = []
        y = []
        
        for i in range(m):
            x.append(coordinates[i][0])
            y.append(coordinates[i][1])

        #print (x, y)
        
        if (max(x) == min(x) or max(y) == min(y)):
            return True
        
        if (coordinates[0][0] - coordinates[1][0] == 0):
            return False
        slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        for i in range(2, m):
            if (coordinates[i][0] - coordinates[1][0] == 0):
                return False
            ns = (coordinates[i][1] - coordinates[1][1]) / (coordinates[i][0] - coordinates[1][0])
            if (ns == slope):
                continue
            else:
                return False
        return True
        
print (checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
