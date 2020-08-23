plateau= [  [ True , False , False , False ] ,
            [ False , True , True , False ] ]
row = 2
col = 4
def voisinsCase(arr,i,j):
   result = []

   # for column
   for c in range(1,col):
      if(arr[i][c] and c!=j):
         result.append([i,c])

   # for rows
   for r in range(1,row):
      if(arr[r][j] and r!=i):
         result.append([r,j])

   return result

print(voisinsCase(plateau,1,1))

def voisinsCases(arr,points):
   result=[]
   for point in points:
      interResult = voisinsCase(arr,point[0],point[1])
      if(len(interResult)>0):
         for res in interResult:
            result.append(res)
   return result

print(voisinsCases(plateau,[[1,1],[1,2]]))

def accessibles(arr,i,j):
   result=[]
   # use voisin case to determine possible case to attein i,j
   return result

def chemin(arr,point_1,point_2):
   
   possiblePoint_1 = accessibles(arr,point_1[0],point_1[1])
   possiblePoint_2 = accessibles(arr,point_2[0],point_2[1])

   # si l'ensemble des points possiblePoint_1 existe dans possiblePoint_2 et vise versa
   # donc l'union de ces deux groupe cree le chemins
   return True
   # sinon return False



