from __future__ import division
import re
import sys

# YOUR CODE GOES HERE
'''
def main():
    ### YOUR MAIN CODE GOES HERE
    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print 'read a line:', line
    print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)
'''
class line():
    
    def __init__(self,a,b,c,d):
        self.x1 = float(a)
        self.x2 = float(c)
        self.y1 = float(b)
        self.y2=  float(d)
    def gradient(self):
        try:
            return (self.y2  - self.y1) / (self.x2 - self.x1)
        except ZeroDivisionError:
            print"Zero error occured at x1", self.x1, " x2 ",self.x2     
    def equation(self):
        self.y = self.y2 - (self.gradient()*self.x2)
        return self.y
    def print_line(self):
        print(self.x1,",",self.y1, "->",self.x2,",",self.y2)
        
def intersection(custom_line1,custom_line2,V,Intersection_Vertex):
    
    if(custom_line1.x1==custom_line2.x1 and custom_line1.x2==custom_line2.x2 and custom_line1.y1==custom_line2.y1 and custom_line1.y2==custom_line2.y2) :
        if((custom_line1.x1,custom_line1.y1) not in Intersection_Vertex.values()):
            Intersection_Vertex[len(Intersection_Vertex)] = custom_line1.x1,custom_line1.y1
        if((custom_line1.x1,custom_line1.y1) not in V.values()):
            V[len(V)+1] = (custom_line1.x1,custom_line1.y1)
        if((custom_line1.x2,custom_line1.y2) not in V.values()):
            V[len(V)+1] = (custom_line1.x2,custom_line1.y2)
        return V,Intersection_Vertex
  
    x_max_Line_1 = max(custom_line1.x1,custom_line1.x2)
    x_max_Line_2 = max(custom_line2.x1,custom_line2.x2)
    y_max_Line_1 = max(custom_line1.y1,custom_line1.y2)
    y_max_Line_2 = max(custom_line2.y1,custom_line2.y2)
    x_min_Line_1 = min(custom_line1.x1,custom_line1.x2)
    x_min_Line_2 = min(custom_line2.x1,custom_line2.x2)
    y_min_Line_1 = min(custom_line1.y1,custom_line1.y2)
    y_min_Line_2 = min(custom_line2.y1,custom_line2.y2)
    
    if(custom_line1.x1==custom_line1.x2 or custom_line2.x1==custom_line2.x2):
        if(custom_line1.x1==custom_line1.x2 and custom_line2.x1!=custom_line2.x2):
            xInt = custom_line1.x1
            L2m  = custom_line2.gradient()
            L2y1 = custom_line2.equation()
            yInt = L2m*xInt + L2y1
            if(yInt>= y_min_Line_2 and yInt <= y_max_Line_2 and yInt >= y_min_Line_1 and yInt <= y_max_Line_1):
                V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex)
        elif(custom_line1.x1!=custom_line1.x2 and custom_line2.x1==custom_line2.x2 ):
            xInt = custom_line2.x1
            L1m  = custom_line1.gradient()
            L1y1 = custom_line1.equation()
            yInt = L1m*xInt +L1y1
            if(yInt>= y_min_Line_2 and yInt <= y_max_Line_2 and yInt >= y_min_Line_1 and yInt <= y_max_Line_1):
                V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex)
        return V,Intersection_Vertex
    else:
    
        L1x = custom_line1.x1
        L1y = custom_line1.y1    
        L1m = custom_line1.gradient()
        L1y1 = custom_line1.equation()
        L2x = custom_line2.x1
        L2y = custom_line2.y1
        L2m = custom_line2.gradient()
        L2y1= custom_line2.equation()
        cht = -1
        flag_IV = 0
        if(L2m==L1m):
            if (L1y1 != L2y1):
                return V,Intersection_Vertex
            else:
                #Same gradient and partial overlapp
                global_x = sorted([custom_line1.x1, custom_line1.x2, custom_line2.x1, custom_line2.x2])
                global_y = sorted([custom_line1.y1, custom_line1.y2, custom_line2.y1, custom_line2.y2])
                int_vert = -1
                for i in range(0,len(global_x)):  
                    if (global_x[i] >= min(custom_line1.x1,custom_line1.x2) and global_x[i] <= max(custom_line1.x1,custom_line1.x2) and global_x[i] >= min(custom_line2.x1,custom_line2.x2) and global_x[i] <= max(custom_line2.x1,custom_line2.x2)):
                        if(global_y[i] >= min(custom_line1.y1,custom_line1.y2) and global_y[i] <= max(custom_line1.y1,custom_line1.y2) and global_y[i] >= min(custom_line2.y1,custom_line2.y2) and global_y[i] <= max(custom_line2.y1,custom_line2.y2)):
                           int_vert= i
                           cht  = i
                           if((global_x[i],global_y[i]) not in Intersection_Vertex.values() and flag_IV == 0):
                               flag_IV = 1
                               Intersection_Vertex[len(Intersection_Vertex)] = global_x[i],global_y[i]
                    
                if((global_x[cht],global_y[cht]) not in Intersection_Vertex.values()):
                    Intersection_Vertex[len(Intersection_Vertex)] = global_x[cht],global_y[cht]
                if(int_vert>-1):
                    for i in range(0,len(global_x)):
                        if((global_x[i],global_y[i]) not in V.values()):
                            V[len(V)+1] = global_x[i],global_y[i]
                return V,Intersection_Vertex
        
        xInt=float((L1y1-L2y1)/(L2m-L1m))
        yInt = float(L1m*xInt + L1y1)
        yTest = float(L2m*xInt + L2y1)
        
        if((yInt>y_min_Line_1) and (yInt<y_max_Line_1) and (xInt >x_min_Line_1) and (xInt<x_max_Line_1) and (yInt>y_min_Line_2) and (yInt<y_max_Line_2) and (xInt > x_min_Line_2) and (xInt < x_max_Line_2)):
            V,Intersection_Vertex = Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex) 
    return V,Intersection_Vertex

def same_street(V,I_V,TotalStreets,StreetList):
    Vlist = V.values()
    I_Vlist = I_V.values()
    edges =[]
    yes_edge = 0
    vertix_st_dict = {}
    street_V = []
    street_V =V.values()
    ks = 0
    for key in I_V:
        ks = key
        for key in V:
            yes_edge = 0
            if(V[key]!=I_V[ks]):
                for i in range(len(StreetList)):
                    flag_iv = False
                    flag_v = False
                    lab_v = []
                    v_seg = -1
                    int_seg = -1
                    k_Num = []
                    flag_Check = -2
                   
                    for k in range(len(TotalStreets[StreetList[i]])):
                        outputt = 0
                        k_set = []
                        for m in range(0,len(street_V)):
                            if(vertix_check(street_V[m],TotalStreets[StreetList[i]][k])):
                                
                                    if(len(lab_v)==0):
                                       k_set.append(tuple(list(street_V[m])))
                                    else:
                                        for ko in range(0,len(lab_v)):

                                            if((street_V[m]) not in lab_v):
                                                flag_Check=0
                                                
                                            else:
                                                flag_Check=1
                                                
                                                break
                                        if(flag_Check == 0):
                                            k_set.append(tuple(list(street_V[m])))
                                        if(flag_Check == 1):
                                            continue
                        distance = {}
                        updated_k_set = []
                        for L in range(0,len(k_set)):
                            x1 = TotalStreets[StreetList[i]][k].x1
                            y1 = TotalStreets[StreetList[i]][k].y1
                            dist_from_x_Start = (k_set[L][0]-x1)**2 + (k_set[L][1]-y1)**2
                            distance[L] = dist_from_x_Start
                        distance = sorted(distance.iteritems(), key = lambda po : po[1])
                        
                        for L in range(0,len(distance)):
                            updated_k_set.append(k_set[distance[L][0]])
                       
                        for kl in range(0,len(updated_k_set)):
                            lab_v.append(updated_k_set[kl])
                                
                        if(vertix_check(I_V[ks],TotalStreets[StreetList[i]][k])):
                            flag_iv = True
                            int_seg = k
                            
                        if(vertix_check(V[key],TotalStreets[StreetList[i]][k])):
                            flag_v = True
                            v_seg = k
       
                    if(flag_iv == True and flag_v == True):
                        yes_edge = No_Vertix_Between( V[key],I_V[ks],lab_v)
                    if(yes_edge == 1):
                        if((ks,key) not in edges and (key,ks) not in edges):
                            edges.append((ks,key))
                       
    return edges
             
def No_Vertix_Between(V1,IV1,lab_v):
    V1_Index = -1
    IV1_Index= -1
    for i in range(0,len(lab_v)):
        if(lab_v[i]==V1):
            V1_Index = i
        elif(lab_v[i]==IV1):
            IV1_Index= i
    if(V1_Index-IV1_Index==1 or V1_Index-IV1_Index == -1):
        return 1
    else:
        return 0

def vertix_check(v,custom_line1):
    x_max = max(custom_line1.x1,custom_line1.x2)
    x_min = min(custom_line1.x1,custom_line1.x2)
    y_max = max(custom_line1.y1,custom_line1.y2)
    y_min = min(custom_line1.y1,custom_line1.y2)
    Vx = 0
    Vy = 0
    Vx = v[0]
    Vy = v[1]
    result = 0
    vtest = 0

    if(custom_line1.x1 == custom_line1.x2):
        if(Vx==custom_line1.x1  and Vy>=y_min and Vy<=y_max):
            result = 1
            return result
    elif(Vx>=x_min and Vx<=x_max and Vy>=y_min and Vy<=y_max):
        m = custom_line1.gradient()
        yc = custom_line1.equation()
        Vy = float(Vy)
        Vx = float(Vx)
        m = float(m)
        yc = float(yc)
        vtest = float((m*Vx + yc))
        vtest = round(vtest,2)
        Vy = round(Vy,2)
        if(float(Vy) == float(vtest)):
            result = 1
            return result
    else:
        return result
                               
def addStreet(cart,TotalStreets,Command,StreetNames):
    Streets=[]
    i = 1
    numSeg = int(len(cart)/2 - 1)
    for k in range(0,numSeg):
        line1 = line(cart[i],cart[i+1],cart[i+2],cart[i+3])
        Streets.append(line1)
        i = i+2
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break
    streetlist = streetlist.upper()

    if(streetlist in StreetNames):
        print"Error: The street you want to add alreay exists in our database."
        return TotalStreets,StreetNames
    else:
        StreetNames.append(streetlist)
        TotalStreets.update({streetlist:Streets})
        return TotalStreets,StreetNames

def changeStreet(cart,TotalStreets,Command,StreetNames):
    Streets=[]
    i = 1
    numSeg = int(len(cart)/2 - 1)
    for k in range(0,numSeg):
        line1 = line(cart[i],cart[i+1],cart[i+2],cart[i+3])
        Streets.append(line1)
        i = i+2
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break
    
    streetlist = streetlist.upper()
    if(streetlist not in StreetNames):
        print"Error: The street you want to change doesn't exist on our database."
        return TotalStreets,StreetNames
    else:
        TotalStreets.update({streetlist:Streets})
        return TotalStreets,StreetNames

def Vertex(xInt,yInt,custom_line1,custom_line2,V,Intersection_Vertex):
    xIntt = (xInt)
    yIntt = (yInt)
    x_1_1 = (custom_line1.x1)
    x_2_1 = (custom_line1.x2)
    x_1_2 = (custom_line2.x1)
    x_2_2 = (custom_line2.x2)
    y_1_1=  (custom_line1.y1)
    y_2_1=  (custom_line1.y2)
    y_1_2 = (custom_line2.y1)
    y_2_2 = custom_line2.y2
    
    if((xIntt,yIntt) not in Intersection_Vertex.values()):
        Intersection_Vertex[len(Intersection_Vertex)] = xIntt,yIntt
    
    if((xIntt,yIntt) not in V.values()):
        V[len(V)+1] = xIntt,yIntt
        
    if((x_1_2,y_1_2) not in V.values()):
        V[len(V)+1] = x_1_2,y_1_2
        
    if((x_2_2, y_2_2) not in V.values()):
        V[len(V)+1] = x_2_2, y_2_2
        
    if((x_2_1, y_2_1) not in V.values()):
        V[len(V)+1] = x_2_1, y_2_1
        
    if((x_1_1,y_1_1) not in V.values()):
        V[len(V)+1] = x_1_1,y_1_1

    return V,Intersection_Vertex
    
def keyupdate(V,Intersection_Vertex):
    keyy = 0
    intersection_with_actual_keys = {}
    for i in range(len(Intersection_Vertex)):
        keyy= [key  for (key, value) in V.items() if value == Intersection_Vertex[i]]
        keyyy = keyy[0]
        intersection_with_actual_keys.update({keyyy: Intersection_Vertex[i]})
    return intersection_with_actual_keys
        
def exCord(Command):
    provided = []
    provided = Command
    i = 0
    flag = 0
    Cord = []
    while (i< len(provided)):
        while(provided[i]!= '(' and flag == 0):
            i = i+1
        flag = 1
        Cord.append(provided[i])
        i = i+1
    h = len(Cord)
    itr = 0
    cart = {}
    u = 0
    much = 0
    listt = []
    gg= 0
    num = 0
    values =[]
    while itr<h:
        if(Cord[itr] not in ["(",")",","," "]):
            much = much+1
            while True:
                if(Cord[itr] == ")" or Cord[itr] == ","):
                    itr = itr+1
                    break
                elif(Cord[itr] not in ["(",")",","]):
                    listt.append(Cord[itr])
                    itr = itr+1

            num = checknumbers(str(listt))  
            if num==1:
                s = [str(i) for i in listt]
                res = int("".join(s))
                cart[much] = res
                listt = []
            else:
                return ""
        else:
            itr = itr + 1
            
    if(len(cart)%2==0):
        return cart
    else:
        print "Error: One coordinate missing"
        return ""
    
def ErrorCheck(Command):
    output = 0
    k = 0
    g = 0
    flag_Input = 0
    flag_count=0
    flag_brac_check = 0
    br = 0
    error = 0
    ind = 0
    check = 0
    checkbrac = 0
    onlyletters = ""
    
    if(len(Command)==0 ):
        print"Error:Not valid input given"
        output = 1
        return output
    if(Command[0] == ' '):
        print"Error:Not valid input given as there is extra space at start"
        output = 1
        return output
    if(Command[0]=='g' and len(Command)>1):
        print"Error: Nothing should be given as input along with 'g'"
        output = 1
        return output
    if(Command[0]!='g' and len(Command)<2):
        print"Error: Invalid Input as no streetname and coordinates are given"
        output = 1
        return output
    if(Command[0]!='g'):
        if(Command[0] not in ['a','c','r','g']):
            print "Error: Invalid input command "
            output = 1
            return output
        if(Command[1] != ' '):
            print "Error: No space before Street Name "
            output = 1
            return output
            
        for i in range(len(Command)):
            if(Command[i]=='"'):
               if(Command[i]=='"' and flag_Input==1):
                   flag_count = 2
                   k = i
                   g = i+1
                   if(Command[0]!='r'):

                       
                       if(i==len(Command)-1 ):
                           print "Error: No coordinates given"
                           error = 1
                           output = 1
                           return output
                           break      
                       
                       if(Command[len(Command)-1] not in  [')',' ']):
                           print "Error: Invalid input format"
                           error = 1
                           output = 1
                           return output
                           break
                         
                       if(i==len(Command)-1 ):
                           print "Error: No coordinates given"
                           error = 1
                           output = 1
                           return output
                           break
                       if(Command[i+1]!=' '):
                           error = 1
                           print "Error: No Space after Street Name"
                           output = 1
                           return output
                           break
                       while(k<len(Command) ):
                             if(Command[k+1] ==' '):
                                 k = k+1
                             elif(Command[k+1]=='('):
                                 flag_brac_check = 1
                                 k = k+1
                                 break
                             else:
                                 print"Error: Invalid Input format"
                                 br = 1
                                 output = 1
                                 return output
                                 break
               flag_Input = 1
        if(flag_count)==0:
            print "Error: Invalid street name or no street name given "
            output = 1
            return output
        if(br == 1):
            print "Error:Invalid input format"
            output = 1
            return output

        if(flag_Input == 0):
            print "Error: Invalid Input format"
            output = 1
            return output
            
        flag_CheckLetters = 0

        for i in range(1,len(Command)):
            if(Command[i] not in ['"',' ']):
                print "Error: Invalid input before Street Name"
                output = 1
                return output  
            elif(Command[i] == '"'):
                break
        for i in range(len(Command)):    
            if(Command[i]=='"' and flag_CheckLetters==0):
                i = i+1
                while (Command[i]!='"'):
                    onlyletters += Command[i]
                    i = i+1
                flag_CheckLetters = 1
                break                        
        
        validin = 0
        if len(onlyletters) == 0:
            print "Error: No Street Name Specified"
            output = 1
            return output
        
        if all(x.isalpha() or x.isspace() for x in onlyletters):
            validin = 1
            
        else:
            print("Error: Street name should only have alphabets ")
            error = 1
            output = 1
            return output 
            
    for i in range(len(Command)):
        if(Command[i] in ['(',')']):
            if(Command[i] == ')' and flag_brac_check== 0):
                print "Error: Invalid input format"
                check = 1
                output = 1
                return output
                continue
            elif(Command[i]=='(' and checkbrac == 0):
                 checkbrac = 1
            elif(Command[i]==')' and checkbrac == 1):
                 checkbrac = 0
            else:
                print "Error: Invalid input format "
                output = 1
                check = 1
                return output
               
    if(check==1 or checkbrac==1):
        output = 1
        return output
    if(error == 1):
        output = 1
        return output
    
    return output
   
def keyupdate_For_V(V,V_Previous):
    keyy = 0
    new_V = {}
    flag_0 = 0
    kee = 0
    new_V_2 = {}
    keylist = V_Previous.keys()
    if(len(V_Previous)>0):
        key_max = max(keylist)
        L = key_max
    else:
        L = 0
    
    for key in V:
        kee = key
        for key in V_Previous:
            if(V_Previous[key]==V[kee]):
                new_V.update({key: V_Previous[key]})
                
    for key in V:
        kys = key
        for key in new_V:
            if(V[kys]==new_V[key]):
                flag_0 = 1
        if(flag_0 == 0):
            L=L+1
            new_V.update({L:V[kys]})
            
        flag_0 = 0
   
    return new_V

def removeStreet(TotalStreets,Command,StreetNames):
    provided = Command
    flag2 = 0
    streetlist=''
    p = 0
    while (p< len(provided)):
        if(provided[p] != '"' and  flag2 == 0):
            p = p+1
        else:
            flag2 = 1
            y=p
            while(y<len(provided)):
                streetlist += provided[y]
                y = y+1
                if(provided[y] =='"'):
                    streetlist += provided[y]
                    break
        if (flag2== 1):
            break
       
    streetlist = streetlist.upper()
    if(streetlist not in StreetNames):
        print"Error: The street you want to remove doesn't exist on our database."
        return TotalStreets,StreetNames
    else:
        StreetNames.remove(streetlist)
        del TotalStreets[streetlist]
        return TotalStreets,StreetNames
def showEdge(EdgeList):  
    if(len(EdgeList)<1):
        print "E = {\n}"
    else:
        print "E = { "
        for i in range(len(EdgeList)):
            if(i<len(EdgeList)-1):
               print" <"+str(EdgeList[i][0])+","+str(EdgeList[i][1])+">,"
            else:
               print" <"+str(EdgeList[i][0])+","+str(EdgeList[i][1])+">"
               
        print"}"
        
def showDic(new_V):
    dictionary_Vertix = {}
    dictionary_Vertix = dict(new_V)
    for key in dictionary_Vertix :
        x1 = dictionary_Vertix [key][0]
        y1 = dictionary_Vertix [key][1]
        x1 = round(x1,2)
        y1 = round(y1,2)
        dictionary_Vertix [key] = x1,y1
    if(len(dictionary_Vertix )<1):
        print "V = {\n}"
    else:
        print "V = { "
        for key in sorted(dictionary_Vertix) :
            print " "+str(key)+":"+" "+"("+str(dictionary_Vertix[key][0])+","+str(dictionary_Vertix[key][1])+")"
        print"}"

def run(string):  
    regex = re.compile('[@_!#$%^&*<>?/\|}{~:]') 
          
    if(regex.search(string) == None): 
        return 0  
    else: 
        print("Error:Input not accepted as it contains invlaid characters or brackets.") 
        return 1
def checknumbers(string):
    if re.search(r"[a-z]", string) == None:
        return 1
    else:
        print "Error: Invalid Coordinates"
        return 0
    
while True:
    V={}
    Intersection_Vertex = {}
    Streets = []
    TotalStreets = {}
    StreetList = []
    I_V={}
    Error_Result = 0
    V_Previous ={}
    Intersection_Vertex_Previous = {}
    new_Flag = 0
    gPress = 0
    Edges_List = []
    inputResult = 0
    errorr = 0
    while True:
        Command = raw_input("")
        inputResult = run(Command)
        if(inputResult == 1):
            continue
        Error_Result = ErrorCheck(Command)
        if(Error_Result ==1):
            continue
        elif(Error_Result ==0):
            if(Command[0] == 'a'):
                cart1= exCord(Command)
                if (len(cart1) == 0):
                    continue
                TotalStreets,StreetList = addStreet(cart1,TotalStreets,Command,StreetList)
                gPress = 0
                
            elif(Command[0] == 'c'):
                cart1= exCord(Command)
                if (len(cart1) == 0):
                    continue
                TotalStreets,StreetList = changeStreet(cart1,TotalStreets,Command,StreetList)
                gPress = 0
                
            elif(Command[0] == 'r'):
                TotalStreets,StreetList = removeStreet(TotalStreets,Command,StreetList)
                gPress = 0
                       
            elif(Command[0]=='g'):
                if(gPress == 0):
                    gPress = 1
                    V={}
                    Intersection_Vertex = {}
                    for i in range(len(StreetList)):
                        tr = i
                        while (tr<len(StreetList)-1):
                            for k in range(len(TotalStreets[StreetList[i]])):
                                for l in range(len(TotalStreets[StreetList[tr+1]])):
                                    V,Intersection_Vertex = intersection(TotalStreets[StreetList[i]][k],TotalStreets[StreetList[tr+1]][l],V,Intersection_Vertex)
                            tr = tr + 1
                    if(new_Flag == 0):
                        new_V = V
                        I_V= keyupdate(V,Intersection_Vertex)
                        showDic(new_V)
                        Edges_List = same_street(V,I_V,TotalStreets,StreetList)
                        showEdge(Edges_List)
                        
                    elif(new_Flag==1):
                        new_V = keyupdate_For_V(V,V_Previous)
                        I_V= keyupdate(new_V,Intersection_Vertex)
                        showDic(new_V)
                        Edges_List = same_street(new_V,I_V,TotalStreets,StreetList)
                        showEdge(Edges_List)   
                    new_Flag = 1
                elif(gPress == 1):
                    showDic(new_V)
                    showEdge(Edges_List)
                    gPress = 1
                    
                V_Previous = new_V
                
