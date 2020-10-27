from math import pi

power = int(input("Enter power: "))
speed = int(input("Enter speed: "))
diameter = float(input("Enter diameter: "))
font_size = float(input("Enter font size: "))
output_text = input("Enter output text: ")
print([diameter, font_size, output_text])
in_file = open("auto_markirovka.script", "r")

turn = font_size / (pi * diameter) * 360

text = """Loop_{number} = 0
while (Loop_{number} < {length}):
  while (get_standard_digital_in(7) == False):
    sync()
  end
  while (get_standard_digital_in(7) == True):
    sync()
  end
  position[5]=position[5]- d2r ({degree})
  movej(position, a=3.490658503988659, v=2.0943951023931953)
  Loop_{number} = Loop_{number} + 1
end
position[5]=position[5]- d2r ({degree})
movej(position, a=3.490658503988659, v=2.0943951023931953)
"""

with open("C:/Users/laser/Desktop/robot.script", "w") as out_file:
    for line in in_file.readlines():
        if line.strip() == "$OUTPUT":
            out = output_text.split()
            for each in out:
                if each.isdigit() == True:
                    turn -= 0.5
                out_file.write(text.format(number = out.index(each), length = len(each), degree = round(turn, 3)))
        else:
            out_file.write(line)

with open('C:/Users/laser/Desktop/marking.lsc', 'w') as marker:
    marker.write('freq 50\nspeed {}\npower {}\n\nttfont "Times New Roman", {}, 3, 20,, 1\n\n'.format(speed, power, font_size))
    for each in output_text:
        if not each.isspace():
            marker.write('outport 1\ntext "{}"\noutport 0\ndelay 500\n\n'.format(each))
        else:
            marker.write('delay 250\n\n')

marker.close()
out_file.close()
in_file.close()