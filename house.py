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
#WindowPane
ctx.translate(-10,0)
ctx.save()
ctx.set_source_rgb(0,158,93)
ctx.move_to(120,300)
ctx.line_to(200,350)
ctx.line_to(200,250)
ctx.line_to(120,200)
ctx.fill()
ctx.restore()

#WindowFrame
ctx.set_line_width(4)
ctx.move_to(120,300)
ctx.line_to(200,350)
ctx.line_to(200,250)
ctx.line_to(120,200)
ctx.close_path()
ctx.move_to(160,225)
ctx.line_to(160,325)
ctx.move_to(120,250)
ctx.line_to(200,300)


#Front Windows
ctx.translate(30,0)
#Left Window
ctx.move_to(260,280)
ctx.line_to(300,270)
ctx.line_to(300,355)
ctx.line_to(260,365)
ctx.close_path()
ctx.move_to(260,325)
ctx.line_to(300,315)



#Right Window
ctx.translate(100,-25)
ctx.move_to(260,280)
ctx.line_to(300,270)
ctx.line_to(300,355)
ctx.line_to(260,365)
ctx.close_path()
ctx.move_to(260,325)
ctx.line_to(300,315)
ctx.stroke()

#DoorKnob
ctx.save()
ctx.scale(1, 2)
ctx.arc(400, 160, 4, 0, 2 * 3.14159)
ctx.restore()
ctx.fill()

surface.write_to_png("house.png")