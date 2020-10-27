from math import pi
import tkinter as tk
import tkinter.messagebox

# Creating script for laser to output thr text separately by letter
def marker_script(speed, power, font_size, output_text):
  with open('C:/Users/laser/Desktop/marking.lsc', 'w') as marker:
    marker.write('freq 50\nspeed {}\npower {}\n\nttfont "Times New Roman", {}, 3, 20,, 1\nrotate -90\n\n'.format(speed, power, font_size))
    for each in output_text:
      if not each.isspace():
        marker.write('outport 1\ntext "{}"\noutport 0\ndelay 500\n\n'.format(each))
      else:
        marker.write('delay 250\n\n')

# Creating script for robot to rotate depending on the letter being marked
def robot_script(in_file, output_text, font_size, one_mm_to_rotate):
  point9 = ['W'] 
  point8 = ['Ъ', 'Ш', 'Щ', 'Ф', 'Ж']          
  point7 = ['Ю', 'Ы', 'Ц', 'О', 'Х', 'М', 'Д', 'А', 'ж', 'т', 'ф', 'ш', 'щ', 'ы', 'ю', 'A', 'M', 'V', 'X', 'Y', 'm', 'w', 'K']
  point6 = ['Г', 'С', 'а', 'м', 'ц', 'ъ', 'B', 'D', 'G', 'H', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'Z', 'a']
  point5 = ['З', 'C', 'E', 'F', 'L', 'b', 'd', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 'q', 's', 'u', 'v', 'x', 'y', 'z']
  point4 = ['з', 'с', 'G', 'c', 'f', 'r', 't', '-']
  point3 = ['g', '1']
  point2 = ['l']
  point1 = ['I', 'i', '.']
  with open("C:/Users/laser/Desktop/robot.script", "w") as out_file:
    for line in in_file.readlines():
      if line.strip() == "$OUTPUT":
        for each in output_text:
          if each in point1:
            turn = 0.6 * font_size * one_mm_to_rotate
          elif each in point2:
            turn = 0.7 * font_size * one_mm_to_rotate
          elif each in point3:
            turn = 0.8 * font_size * one_mm_to_rotate
          elif each in point4:
            turn = 0.9 * font_size * one_mm_to_rotate
          elif each in point5:
            turn = 1.0 * font_size * one_mm_to_rotate
          elif each in point6:
            turn = 1.1 * font_size * one_mm_to_rotate
          elif each in point7:
            turn = 1.2 * font_size * one_mm_to_rotate
          elif each in point8:
            turn = 1.3 * font_size * one_mm_to_rotate
          elif each in point9:
            turn = 1.4 * font_size * one_mm_to_rotate
          elif each.isupper() == True:
            turn = 1.1 * font_size * one_mm_to_rotate
          elif each.isspace() == True:
            turn = 0.7 * font_size * one_mm_to_rotate
          else:
            turn = 0.9 * font_size * one_mm_to_rotate
          if each.isspace() != True:
            out_file.write(text.format(degree = round(turn, 3)))
          else:
            out_file.write("position[5]=position[5]- d2r ({degree})\nmovej(position, a=3.490658503988659, v=2.0943951023931953)\n".format(degree = round(turn, 3)))
      else:
        out_file.write(line)

text = """while (get_standard_digital_in(7) == False):
  sync()
end
while (get_standard_digital_in(7) == True):
  sync()
end
position[5]=position[5]- d2r ({degree})
movej(position, a=3.490658503988659, v=2.0943951023931953)
"""

def main():
  root = tk.Tk()

  canvas = tk.Canvas(root, width=300, height=325, relief='raised', bg='gray85')
  canvas.pack()

  output1 = tk.Label(root, text='Мощность: ', bg='gray85')
  output1.config(font=('helvetica', 10))
  canvas.create_window(150, 25, window=output1)

  powerIn = tk.Entry(root, width=5)
  canvas.create_window(150, 50, window=powerIn)

  output2 = tk.Label(root, text='Скорость: ', bg='gray85')
  output2.config(font=('helvetica', 10))
  canvas.create_window(150, 75, window=output2)

  speedIn = tk.Entry(root, width=5)
  canvas.create_window(150, 100, window=speedIn)

  output3 = tk.Label(root, text='Диаметр: ', bg='gray85')
  output3.config(font=('helvetica', 10))
  canvas.create_window(150, 125, window=output3)

  diameterIn = tk.Entry(root, width=5)
  canvas.create_window(150, 150, window=diameterIn)

  output4 = tk.Label(root, text='Размер шрифта: ', bg='gray85')
  output4.config(font=('helvetica', 10))
  canvas.create_window(150, 175, window=output4)

  font = tk.Entry(root, width=5)
  canvas.create_window(150, 200, window=font)

  output5 = tk.Label(root, text='Надпись: ', bg='gray85')
  output5.config(font=('helvetica', 10))
  canvas.create_window(150, 225, window=output5)

  text = tk.Entry(root, width=40)
  canvas.create_window(150, 250, window=text)

  def get_values():

    power = int(powerIn.get())
    speed = int(speedIn.get())
    diameter = int(diameterIn.get())
    font_size = float(font.get())
    output_text = text.get()

    in_file = open("auto_markirovka.script", "r")

    one_mm_to_rotate = 360 / (pi * diameter)

    marker_script(speed, power, font_size, output_text)
    robot_script(in_file, output_text, font_size, one_mm_to_rotate)
    in_file.close()

    root.quit()

    tk.messagebox.showinfo('Готово', 'Файлы "marking.lsc" и "robot.script" были созданы на рабочем столе!')
  
  btn = tk.Button(text="Готово", command=get_values, width=8, font=('helvetica', 10, 'bold'), bg='lightgreen')
  canvas.create_window(100, 300, window=btn)

  quitBtn = tk.Button(text="Выход", command=root.quit, width=8, font=('helvetica', 10, 'bold'), bg='tomato')
  canvas.create_window(200, 300, window=quitBtn)

  root.mainloop()

if __name__ == "__main__":
  main()