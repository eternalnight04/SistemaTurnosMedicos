from PIL import Image
import sys
img_path = r"c:\Users\nachi\SistemaTurnosMedicos\diagramas\01-diagrama-clases\06-clases-diagrama-final.png"
img = Image.open(img_path)
print('size:', img.size)

out_dir = r"c:\Users\nachi\SistemaTurnosMedicos\diagramas\01-diagrama-clases\capturas-pilares"
import os
os.makedirs(out_dir, exist_ok=True)

boxes = {
	# tighter crops: (left, top, right, bottom)
	# Turno only
	'poo-encapsulamiento-ejemplo-1.png': (680, 380, 1280, 820),
	# UsuarioDelSistema only
	'poo-encapsulamiento-ejemplo-2.png': (600, 140, 1240, 420),
	# Herencia: Paciente, Medico, Secretaria + UsuarioDelSistema (wide)
	'poo-herencia-ejemplo-1.png': (10, 20, 1450, 320),
	# Herencia ejemplo 2: UsuarioDelSistema only (show base for future subclasses)
	'poo-herencia-ejemplo-2.png': (640, 60, 940, 260),
	# Polimorfismo ejemplo 1: Paciente, UsuarioDelSistema, Medico
	'poo-polimorfismo-ejemplo-1.png': (10, 20, 1000, 360),
	# Polimorfismo ejemplo 2: Secretaria + UsuarioDelSistema
	'poo-polimorfismo-ejemplo-2.png': (760, 40, 1320, 320),
	# Agenda only
	'poo-abstraccion-ejemplo-1.png': (1500, 240, 1890, 520),
	# Turno only (abstraccion ejemplo 2)
	'poo-abstraccion-ejemplo-2.png': (680, 380, 1280, 820),
}

for name, box in boxes.items():
	crop = img.crop(box)
	out_path = os.path.join(out_dir, name)
	crop.save(out_path)
	print('saved', out_path)
