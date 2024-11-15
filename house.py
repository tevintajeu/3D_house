
import math

import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

ctx.translate(0,50)
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(4)
ctx.move_to(80,200)
ctx.line_to(80,350)
ctx.line_to(230,450)

#Door Start
ctx.line_to(480,370)
ctx.line_to(480,250)
ctx.line_to(540,235)
ctx.line_to(540,360)

ctx.move_to(480,365)
ctx.line_to(530,350)
ctx.line_to(540,360)

ctx.move_to(530,350)
ctx.line_to(530,235)

#Door End
ctx.move_to(540,360)
ctx.line_to(570,350)

#Roof Start
ctx.line_to(570,180)
ctx.line_to(240,260)
ctx.line_to(150,100)
ctx.line_to(70,210)
ctx.line_to(60,200)
ctx.line_to(150,80)
ctx.line_to(500,0)
ctx.line_to(595,160)
#Roof End

ctx.move_to(570,180)
ctx.line_to(590,175)
ctx.line_to(595,160)
ctx.stroke()

ctx.set_line_width(2)
ctx.move_to(230,450)
ctx.line_to(230,240)

ctx.move_to(155,80)
ctx.line_to(245,245)
ctx.line_to(595,160)
ctx.stroke()

#Window in Shade
ctx.translate(-10,0)
ctx.move_to(120,300)
ctx.line_to(200,350)
ctx.line_to(200,250)
ctx.line_to(120,200)
ctx.close_path()

#Front Windows
ctx.translate(30,0)
#Left Window
ctx.move_to(260,280)
ctx.line_to(320,265)
ctx.line_to(320,355)
ctx.line_to(260,370)
ctx.close_path()

#Right Window
ctx.translate(100,-25)
ctx.move_to(260,280)
ctx.line_to(320,265)
ctx.line_to(320,355)
ctx.line_to(260,370)
ctx.close_path()
ctx.stroke()



ctx.move_to(165,210)#1
ctx.line_to(165,155)#4
ctx.stroke()

# window
ctx.move_to(173,155)#4
ctx.line_to(230,143)#6
ctx.line_to(230,183)#6
ctx.line_to(173,198)#1
ctx.line_to(173,155)#4

ctx.move_to(173 +4,155+4)#4
ctx.line_to(230 - 4,143 + 6)#6
ctx.line_to(230 -4,183 - 4)#6
ctx.line_to(173 + 4,198 - 6)#1
ctx.line_to(173 + 4,155 + 4)#4

ctx.move_to(177,156)
ctx.line_to(177, 176)
ctx.stroke()



# roof

ctx.move_to(165,210)#1
ctx.line_to(135,160)#2
ctx.line_to(123,160)#3
ctx.line_to(160,160)#4
ctx.line_to(200,120)#5
ctx.line_to(250,150)#6
ctx.line_to(254,145)#7
ctx.line_to(200,113)#8
ctx.line_to(165,113)#9
ctx.line_to(123,160)#3

ctx.move_to(165,210)#1
ctx.line_to(240,187)#6
ctx.line_to(240,143)#6
ctx.set_line_width(4)












ctx.stroke()

surface.write_to_png("house.png")
