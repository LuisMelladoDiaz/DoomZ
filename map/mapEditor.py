import tkinter as tk
from tkinter import ttk

import csv


class MapEditor:
    def __init__(self, master):
        self.sectors = []
        self.walls = []
        self.current_sector = []
        self.sector_number = 0
        self.sector_origin = 0
        self.prev_point = None

        self.current_color = tk.StringVar()
        self.current_color.set("black")

        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=600, bg='white')
        self.canvas.pack(side=tk.LEFT)

        # SIDE BAR
        self.sidebar = tk.Frame(master, width=200, bg='lightgray')
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        # sector number
        self.sector_number_var = tk.StringVar()
        self.sector_number_var.set("Sector number: 1")
        self.sector_number_label = tk.Label(self.sidebar, textvariable=self.sector_number_var)
        self.sector_number_label.pack(pady=(10, 5))

        # color selection
        tk.Label(self.sidebar, text="Wall color:").pack(pady=(5, 0))
        self.color_picker = ttk.Combobox(self.sidebar, values=["black", "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta"], state="readonly", textvariable=self.current_color)
        self.color_picker.current(0)
        self.color_picker.pack(pady=(0, 5))

        # sector height
        tk.Label(self.sidebar, text="Altura del Sector:").pack(pady=(5, 0))
        self.sector_height_entry = tk.Entry(self.sidebar)
        self.sector_height_entry.insert(0, "40")
        self.sector_height_entry.pack(pady=(0, 5))


        # save button
        tk.Button(self.sidebar, text="Guardar", command=self.save).pack(side=tk.BOTTOM, pady=(5, 10))  # Espacio abajo

        self.draw_grid()
        self.canvas.bind('<Button-1>', self.add_wall)

    def draw_grid(self):
        for i in range(0, 600, 20):
            self.canvas.create_line(i, 0, i, 600, fill='lightgray', dash=(2, 2))
        for i in range(0, 600, 20):
            self.canvas.create_line(0, i, 600, i, fill='lightgray', dash=(2, 2))

    def add_wall(self, event):
        x, y = event.x, event.y
        grid_x = round(x / 20) * 20
        grid_y = round(y / 20) * 20

        # DRAW LINE
        if self.prev_point:
            x1, y1 = self.prev_point
            self.canvas.create_line(x1, y1, grid_x, grid_y, fill=self.current_color.get())
            self.current_sector.append([x1, y1, grid_x, grid_y, self.current_color.get()])

        # CLOSE SECTOR
        if (grid_x, grid_y) == self.sector_origin:
            self.sectors.append(self.current_sector)
            self.sector_number += 1
            self.prev_point = None
            self.current_sector = []
            self.sector_number_var.set("Sector number: " + str(self.sector_number))  # Actualizar la etiqueta

        # DRAW POINT
        if (grid_x, grid_y) != self.sector_origin:
            self.canvas.create_rectangle(grid_x-5, grid_y-5, grid_x+5, grid_y+5, fill=self.current_color.get())  # Mostrar el punto actual
            self.prev_point = (grid_x, grid_y)

        if (len(self.current_sector) == 0):
            self.sector_origin = (grid_x, grid_y)
            print("Sector:", self.sector_number, "; Origin:", self.sector_origin)

    def save(self):
        filename = f'map/maps_data/map1'
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.sectors)
            print(self.sectors)


def main():
    root = tk.Tk()
    root.title("Map Editor")
    app = MapEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()