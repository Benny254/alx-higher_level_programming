#!/usr/bin/python3
def pascal_triangle(n):
    """ pascal triangle class body.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    
    for _ in range(1, n):
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    
    return triangles
