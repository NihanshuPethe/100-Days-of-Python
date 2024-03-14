import colorgram
list_c=colorgram.extract('img.jpg',25)
color_list=[]
for i in list_c:
    r= i.rgb.r
    g= i.rgb.g
    b= i.rgb.b
    tup=(r,g,b)
    color_list.append(tup)

print(color_list)