import math 
import copy

posroute= []
posroute2= []
disttravel= int
dist=0
targetdist=8
roaddict = {}
roadcondition ={"flood": .2, "ice":.7 , "snow": .8}
maxquality=0

class node:
	def __init__(self,name, xcord,ycord,adj):
		self.name = name
		self.xcord = xcord
		self.ycord = ycord
		self.adj = adj
	def buildroads(self):
		global roaddict
		# roaddict[self.name] = self.name + "-" +
		for ti in self.adj:
			roadname = self.name + "-" + ti.name
			roaddict[roadname] = 1
def updateroad (node1, node2, condition):
	roaddict.update({node1.name+"-"+node2.name : condition})
	roaddict.update({node2.name+"-"+node1.name : condition})
def quality1(currentnode,previous,dist):
	result= roaddict[currentnode.name+"-"+previous.name] * dist
	return result

def disttravel(currentnode,previous,travellist):
	global maxquality
	# print(posroute2)
	travellist.append(currentnode)
	# print(currentnode.name)
	tdist = 0
	tqual=0
	for k in range(len(travellist)-1):
		dist1 = distance(travellist[k+1].xcord,travellist[k+1].ycord,travellist[k].xcord,travellist[k].ycord)
		tdist = tdist +dist1
		quality = quality1(travellist[k+1],travellist[k],dist1)
		tqual = quality + tqual
	if tdist != 0:
		tqual = tqual/tdist
	else:
		tqual = 0
	newdist = distance(currentnode.xcord,currentnode.ycord,previous.xcord,previous.ycord)
	if(currentnode.name == travellist[0].name and targetdist-.2 <= tdist <= targetdist+2):
		print(tqual)
		if maxquality == 0:
			maxquality= tqual
			posroute2.append(travellist.copy())
		elif maxquality == tqual:
			posroute2.append(travellist.copy())
		elif tqual > maxquality:
			maxquality = tqual
			posroute2.clear()
			posroute2.append(travellist.copy())
		tqual = 0
	elif(tdist < targetdist):
		for i in currentnode.adj:
			if(i.name != previous.name):
				disttravel(i, currentnode, travellist)
				if(len(travellist) >0):
					travellist.pop()


def distance(x1,y1,x2,y2):
	par = (x2-x1)
	par2 =(y2-y1)
	part = par **2
	part2 = par2**2
	fpart = part +part2
	dist2 = math.sqrt(fpart)
	return dist2


A = node("A",0,0,[])
B = node("B",0,2,[])
C = node("C",2,2,[])
D = node("D",2,0,[])
E = node("E",8,0,[])
G = node("G", 0,-2,[])
F= node("F", 2,-2,[])

A.adj.append(B)
A.adj.append(E)
A.adj.append(D)
A.adj.append(G)
B.adj.append(A)
B.adj.append(C)
C.adj.append(B)
C.adj.append(D)
D.adj.append(C)
D.adj.append(A)
D.adj.append(F)
E.adj.append(A)
G.adj.append(A)
G.adj.append(F)
F.adj.append(D)
F.adj.append(G)


A.buildroads()
B.buildroads()
C.buildroads()
D.buildroads()
E.buildroads()
F.buildroads()
G.buildroads()

updateroad(A,B,roadcondition["ice"])
disttravel(A,A,posroute)
# print(len(posroute))
print("+++++++++++++++++++++")
count =0
# print(posroute2)
# print(posroute)
for p in posroute2:
	for p2 in p:
		print(p2.name+"->",end=" ")
	print(" ")


print("###########################")
print(roaddict)
print("**********************************")
updateroad(A,B,roadcondition["ice"])
print(roaddict)
