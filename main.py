from ipywidgets.embed import embed_minimal_html
from PIL import ImageFilter
import gmaps
gmaps.configure(api_key="AIzaSyCo99awBRG0JvRCoJC8M12-3EiAoLfElSM")
fig = gmaps.figure()
from PIL import Image
im = Image.open("/Users/Aakash/36.070403, 68.629560, 68.673354.png")
inputim=im.filter(ImageFilter.ModeFilter(8))
inputim.show()
pix=inputim.load()
imout = im.copy()
pixout=imout.load()
deltax=68.673354-68.629560
locations=[]
xlist=[]
ylist=[]
for i in range(0,inputim.size[0],8):   #x-axis search
    for j in range(0,inputim.size[1],8): #y-axis search
 
        if pix[i,j][1] > 140:
 
                    pixout[i,j]= (255,0,0)
                    xlist=xlist+[-j/1000*delta+36.070403]
                    ylist=ylist+[i/1000*delta+68.629560]

for k in range(0,len(xlist),5):
    locations=locations+[(xlist[k],ylist[k])]
imout.show()
marker = gmaps.marker_layer(locations)
fig.add_layer(marker)
embed_minimal_html('export3.html', views=[fig])
