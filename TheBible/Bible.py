import tkinter as tk

# Utworzenie głównego okna aplikacji

w1, h1 = 1920, 1080
w0 = 3840

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title('The Bible')
second_screen = tk.Toplevel(root)
# second_screen.geometry("1920x1080+1920+0")

#second_screen.attributes("-fullscreen", True)
# second_screen.geometry("+{}+{}".format(screen_width, 0))


root.geometry("1400x200")
biblia = {'Dzieje Apostolskie': {'chapters': 28, 'verses': {1: 27, 10: 49, 11: 31, 12: 26, 13: 53, 14: 29, 15: 42, 16: 41, 17: 35, 18: 29, 19: 42, 2: 48, 20: 39, 21: 41, 22: 31, 23: 36, 24: 28, 25: 28, 26: 33, 27: 45, 28: 31, 3: 27, 4: 38, 5: 43, 6: 16, 7: 61, 8: 41, 9: 44}}, 'Ew. Jana': {'chapters': 21, 'verses': {1: 52, 10: 43, 11: 58, 12: 51, 13: 39, 14: 32, 15: 28, 16: 34, 17: 27, 18: 41, 19: 43, 2: 26, 20: 32, 21: 25, 3: 37, 4: 55, 5: 48, 6: 72, 7: 54, 8: 60, 9: 42}}, 'Ew. Marka': {'chapters': 16, 'verses': {1: 46, 10: 53, 11: 34, 12: 45, 13: 38, 14: 73, 15: 48, 16: 20, 2: 29, 3: 36, 4: 42, 5: 44, 6: 57, 7: 38, 8: 39, 9: 51}}, 'Ew. Mateusza': {'chapters': 28, 'verses': {1: 26, 10: 43, 11: 31, 12: 51, 13: 59, 14: 37, 15: 40, 16: 29, 17: 28, 18: 36, 19: 31, 2: 24, 20: 35, 21: 47, 22: 47, 23: 40, 24: 52, 25: 47, 26: 76, 27: 67, 28: 20, 3: 18, 4: 26, 5: 49, 6: 35, 7: 30, 8: 35, 9: 39}}, 'Ew. Łukasza': {'chapters': 24, 'verses': {1: 81, 10: 43, 11: 55, 12: 60, 13: 36, 14: 36, 15: 33, 16: 32, 17: 38, 18: 44, 19: 49, 2: 53, 20: 48, 21: 39, 22: 72, 23: 57, 24: 53, 3: 39, 4: 45, 5: 40, 6: 50, 7: 51, 8: 57, 9: 63}}, 'I Ks. Kronik': {'chapters': 29, 'verses': {1: 55, 10: 15, 11: 48, 12: 41, 13: 15, 14: 18, 15: 30, 16: 44, 17: 28, 18: 18, 19: 20, 2: 56, 20: 9, 21: 31, 22: 20, 23: 33, 24: 32, 25: 32, 26: 33, 27: 35, 28: 22, 29: 30, 3: 25, 4: 44, 5: 27, 6: 82, 7: 41, 8: 41, 9: 45}}, 'I Ks. Królewska': {'chapters': 22, 'verses': {1: 54, 10: 30, 11: 44, 12: 34, 13: 35, 14: 32, 15: 35, 16: 35, 17: 25, 18: 47, 19: 22, 2: 47, 20: 44, 21: 30, 22: 53, 3: 29, 4: 35, 5: 19, 6: 39, 7: 52, 8: 67, 9: 29}}, 'I Ks. Samuela': {'chapters': 31, 'verses': {1: 29, 10: 28, 11: 16, 12: 26, 13: 24, 14: 53, 15: 36, 16: 24, 17: 59, 18: 31, 19: 25, 2: 37, 20: 43, 21: 16, 22: 24, 23: 30, 24: 23, 25: 45, 26: 26, 27: 13, 28: 26, 29: 12, 3: 22, 30: 32, 31: 13, 4: 23, 5: 13, 6: 22, 7: 18, 8: 23, 9: 28}}, 'I List do Koryntian': {'chapters': 16, 'verses': {1: 32, 10: 34, 11: 35, 12: 32, 13: 14, 14: 41, 15: 59, 16: 24, 2: 17, 3: 24, 4: 22, 5: 14, 6: 21, 7: 41, 8: 14, 9: 28}}, 'I List do Tesaloniczan': {'chapters': 5, 'verses': {1: 11, 2: 21, 3: 14, 4: 19, 5: 28}}, 'I List do Tymoteusza': {'chapters': 6, 'verses': {1: 21, 2: 16, 3: 17, 4: 17, 5: 26, 6: 21}}, 'I List Jana': {'chapters': 5, 'verses': {1: 11, 2: 30, 3: 25, 4: 22, 5: 21}}, 'I List Piotra': {'chapters': 5, 'verses': {1: 26, 2: 26, 3: 23, 4: 20, 5: 14}}, 'II Ks. Kronik': {'chapters': 36, 'verses': {1: 18, 10: 20, 11: 24, 12: 17, 13: 23, 14: 16, 15: 20, 16: 15, 17: 20, 18: 35, 19: 12, 2: 19, 20: 38, 21: 21, 22: 13, 23: 22, 24: 28, 25: 29, 26: 24, 27: 10, 28: 28, 29: 37, 3: 18, 30: 28, 31: 22, 32: 34, 33: 26, 34: 34, 35: 28, 36: 23, 4: 23, 5: 15, 6: 43, 7: 23, 8: 19, 9: 32}}, 'II Ks. Królewska': {'chapters': 25, 'verses': {1: 19, 10: 37, 11: 22, 12: 22, 13: 26, 14: 30, 15: 39, 16: 21, 17: 42, 18: 38, 19: 38, 2: 26, 20: 22, 21: 27, 22: 21, 23: 38, 24: 21, 25: 30, 3: 28, 4: 45, 5: 28, 6: 34, 7: 21, 8: 30, 9: 38}}, 'II Ks. Samuela': {'chapters': 24, 'verses': {1: 28, 10: 20, 11: 28, 12: 32, 13: 40, 14: 34, 15: 38, 16: 24, 17: 30, 18: 34, 19: 44, 2: 33, 20: 27, 21: 23, 22: 52, 23: 40, 24: 25, 3: 40, 4: 13, 5: 26, 6: 24, 7: 30, 8: 19, 9: 14}}, 'II List do Koryntian': {'chapters': 13, 'verses': {1: 25, 10: 19, 11: 34, 12: 22, 13: 14, 2: 18, 3: 19, 4: 19, 5: 22, 6: 19, 7: 17, 8: 25, 9: 16}}, 'II List do Tesaloniczan': {'chapters': 3, 'verses': {1: 13, 2: 18, 3: 18}}, 'II List do Tymoteusza': {'chapters': 4, 'verses': {1: 19, 2: 27, 3: 18, 4: 22}}, 'II List Jana': {'chapters': 1, 'verses': {1: 13}}, 'II List Piotra': {'chapters': 3, 'verses': {1: 22, 2: 23, 3: 18}}, 'III List Jana': {'chapters': 1, 'verses': {1: 14}}, 'Ks. Abdiasza': {'chapters': 1, 'verses': {1: 21}}, 'Ks. Aggeusza': {'chapters': 2, 'verses': {1: 16, 2: 23}}, 'Ks. Amosa': {'chapters': 9, 'verses': {1: 16, 2: 17, 3: 16, 4: 14, 5: 28, 6: 15, 7: 18, 8: 15, 9: 15}}, 'Ks. Daniela': {'chapters': 12, 'verses': {1: 22, 10: 22, 11: 46, 12: 13, 2: 50, 3: 31, 4: 38, 5: 32, 6: 29, 7: 29, 8: 28, 9: 28}}, 'Ks. Estery': {'chapters': 10, 'verses': {1: 23, 10: 3, 2: 24, 3: 16, 4: 18, 5: 15, 6: 15, 7: 11, 8: 18, 9: 33}}, 'Ks. Ezdrasza': {'chapters': 10, 'verses': {1: 12, 10: 44, 2: 71, 3: 14, 4: 25, 5: 18, 6: 23, 7: 29, 8: 37, 9: 16}}, 'Ks. Ezechiela': {'chapters': 48, 'verses': {1: 29, 10: 23, 11: 26, 12: 29, 13: 24, 14: 24, 15: 9, 16: 64, 17: 25, 18: 33, 19: 15, 2: 11, 20: 50, 21: 33, 22: 32, 23: 50, 24: 28, 25: 18, 26: 22, 27: 37, 28: 27, 29: 22, 3: 28, 30: 27, 31: 19, 32: 33, 33: 34, 34: 32, 35: 16, 36: 39, 37: 29, 38: 24, 39: 30, 4: 18, 40: 50, 41: 27, 42: 21, 43: 28, 44: 32, 45: 26, 46: 25, 47: 24, 48: 35, 5: 18, 6: 15, 7: 28, 8: 19, 9: 12}}, 'Ks. Habakuka': {'chapters': 3, 'verses': {1: 18, 2: 21, 3: 19}}, 'Ks. Hioba': {'chapters': 42, 'verses': {1: 23, 10: 23, 11: 21, 12: 26, 13: 29, 14: 23, 15: 36, 16: 23, 17: 17, 18: 22, 19: 30, 2: 14, 20: 30, 21: 35, 22: 31, 23: 18, 24: 26, 25: 7, 26: 15, 27: 24, 28: 29, 29: 26, 3: 27, 30: 32, 31: 41, 32: 23, 33: 34, 34: 38, 35: 17, 36: 34, 37: 25, 38: 42, 39: 31, 4: 22, 40: 25, 41: 35, 42: 17, 5: 28, 6: 31, 7: 22, 8: 23, 9: 36}}, 'Ks. Izajasza': {'chapters': 66, 'verses': {1: 32, 10: 35, 11: 17, 12: 7, 13: 23, 14: 33, 15: 10, 16: 15, 17: 15, 18: 8, 19: 26, 2: 23, 20: 7, 21: 18, 22: 26, 23: 19, 24: 24, 25: 13, 26: 22, 27: 14, 28: 30, 29: 25, 3: 27, 30: 34, 31: 10, 32: 21, 33: 25, 34: 18, 35: 11, 36: 23, 37: 39, 38: 23, 39: 9, 4: 7, 40: 32, 41: 30, 42: 26, 43: 29, 44: 29, 45: 26, 46: 14, 47: 16, 48: 23, 49: 27, 5: 31, 50: 12, 51: 24, 52: 16, 53: 13, 54: 18, 55: 14, 56: 13, 57: 22, 58: 15, 59: 22, 6: 14, 60: 23, 61: 12, 62: 13, 63: 20, 64: 13, 65: 26, 66: 24, 7: 26, 8: 23, 9: 22}}, 'Ks. Jeremiasza': {'chapters': 52, 'verses': {1: 20, 10: 26, 11: 24, 12: 18, 13: 28, 14: 23, 15: 22, 16: 22, 17: 28, 18: 24, 19: 16, 2: 38, 20: 19, 21: 15, 22: 31, 23: 41, 24: 11, 25: 39, 26: 25, 27: 23, 28: 18, 29: 33, 3: 26, 30: 25, 31: 41, 32: 45, 33: 27, 34: 23, 35: 20, 36: 33, 37: 22, 38: 29, 39: 19, 4: 32, 40: 17, 41: 19, 42: 23, 43: 14, 44: 31, 45: 6, 46: 29, 47: 8, 48: 48, 49: 40, 5: 32, 50: 47, 51: 65, 52: 34, 6: 31, 7: 35, 8: 23, 9: 27}}, 'Ks. Joela': {'chapters': 3, 'verses': {1: 21, 2: 33, 3: 21}}, 'Ks. Jonasza': {'chapters': 4, 'verses': {1: 18, 2: 11, 3: 11, 4: 11}}, 'Ks. Jozuego': {'chapters': 24, 'verses': {1: 19, 10: 44, 11: 24, 12: 25, 13: 34, 14: 16, 15: 64, 16: 11, 17: 19, 18: 29, 19: 52, 2: 25, 20: 10, 21: 46, 22: 35, 23: 17, 24: 33, 3: 18, 4: 25, 5: 16, 6: 28, 7: 27, 8: 36, 9: 28}}, 'Ks. Kapłańska': {'chapters': 27, 'verses': {1: 18, 10: 21, 11: 48, 12: 9, 13: 60, 14: 58, 15: 34, 16: 35, 17: 17, 18: 31, 19: 38, 2: 17, 20: 28, 21: 25, 22: 34, 23: 45, 24: 24, 25: 56, 26: 47, 27: 34, 3: 18, 4: 36, 5: 20, 6: 31, 7: 39, 8: 37, 9: 25}}, 'Ks. Kaznodziei': {'chapters': 12, 'verses': {1: 19, 10: 21, 11: 11, 12: 14, 2: 27, 3: 23, 4: 17, 5: 21, 6: 13, 7: 30, 8: 18, 9: 19}}, 'Ks. Liczb': {'chapters': 36, 'verses': {1: 55, 10: 37, 11: 36, 12: 17, 13: 34, 14: 46, 15: 42, 16: 51, 17: 14, 18: 33, 19: 23, 2: 35, 20: 30, 21: 36, 22: 42, 23: 31, 24: 26, 25: 19, 26: 66, 27: 24, 28: 32, 29: 41, 3: 52, 30: 17, 31: 55, 32: 43, 33: 57, 34: 30, 35: 35, 36: 13, 4: 50, 5: 32, 6: 28, 7: 90, 8: 27, 9: 24}}, 'Ks. Malachiasza': {'chapters': 4, 'verses': {1: 15, 2: 18, 3: 19, 4: 6}}, 'Ks. Micheasza': {'chapters': 7, 'verses': {1: 17, 2: 14, 3: 13, 4: 14, 5: 16, 6: 17, 7: 20}}, 'Ks. Nahuma': {'chapters': 3, 'verses': {1: 16, 2: 14, 3: 19}}, 'Ks. Nehemiasza': {'chapters': 13, 'verses': {1: 12, 10: 40, 11: 37, 12: 48, 13: 31, 2: 21, 3: 33, 4: 24, 5: 20, 6: 20, 7: 74, 8: 19, 9: 39}}, 'Ks. Ozeasza': {'chapters': 14, 'verses': {1: 12, 10: 16, 11: 13, 12: 15, 13: 17, 14: 9, 2: 24, 3: 6, 4: 20, 5: 16, 6: 12, 7: 17, 8: 15, 9: 18}}, 'Ks. Powt. Prawa': {'chapters': 34, 'verses': {1: 47, 10: 23, 11: 33, 12: 33, 13: 19, 14: 30, 15: 24, 16: 23, 17: 21, 18: 23, 19: 22, 2: 38, 20: 21, 21: 24, 22: 31, 23: 26, 24: 23, 25: 20, 26: 20, 27: 27, 28: 69, 29: 30, 3: 30, 30: 21, 31: 31, 32: 53, 33: 30, 34: 12, 4: 50, 5: 34, 6: 26, 7: 27, 8: 21, 9: 30}}, 'Ks. Przysłów': {'chapters': 31, 'verses': {1: 34, 10: 33, 11: 32, 12: 29, 13: 26, 14: 36, 15: 34, 16: 34, 17: 29, 18: 25, 19: 30, 2: 23, 20: 31, 21: 32, 22: 30, 23: 36, 24: 35, 25: 29, 26: 29, 27: 28, 28: 29, 29: 28, 3: 36, 30: 34, 31: 31, 4: 28, 5: 24, 6: 36, 7: 28, 8: 37, 9: 19}}, 'Ks. Psalmów': {'chapters': 150, 'verses': {1: 7, 10: 19, 100: 6, 101: 9, 102: 29, 103: 23, 104: 36, 105: 46, 106: 49, 107: 44, 108: 14, 109: 32, 11: 8, 110: 8, 111: 11, 112: 11, 113: 10, 114: 9, 115: 19, 116: 20, 117: 3, 118: 30, 119: 177, 12: 9, 120: 8, 121: 9, 122: 10, 123: 5, 124: 9, 125: 6, 126: 7, 127: 6, 128: 7, 129: 9, 13: 7, 130: 9, 131: 4, 132: 19, 133: 4, 134: 4, 135: 22, 136: 27, 137: 10, 138: 9, 139: 25, 14: 8, 140: 14, 141: 11, 142: 8, 143: 13, 144: 16, 145: 22, 146: 11, 147: 21, 148: 15, 149: 10, 15: 6, 150: 6, 16: 12, 17: 16, 18: 51, 19: 15, 2: 13, 20: 10, 21: 14, 22: 32, 23: 7, 24: 11, 25: 23, 26: 13, 27: 15, 28: 10, 29: 12, 3: 9, 30: 13, 31: 25, 32: 12, 33: 23, 34: 23, 35: 29, 36: 13, 37: 41, 38: 23, 39: 14, 4: 9, 40: 18, 41: 14, 42: 12, 43: 6, 44: 27, 45: 18, 46: 12, 47: 10, 48: 15, 49: 21, 5: 13, 50: 24, 51: 20, 52: 10, 53: 7, 54: 8, 55: 24, 56: 14, 57: 12, 58: 12, 59: 18, 6: 11, 60: 13, 61: 9, 62: 13, 63: 12, 64: 11, 65: 14, 66: 21, 67: 8, 68: 36, 69: 37, 7: 18, 70: 6, 71: 25, 72: 21, 73: 29, 74: 24, 75: 11, 76: 13, 77: 21, 78: 73, 79: 14, 8: 10, 80: 20, 81: 17, 82: 9, 83: 19, 84: 13, 85: 14, 86: 18, 87: 8, 88: 19, 89: 53, 9: 21, 90: 18, 91: 17, 92: 16, 93: 6, 94: 24, 95: 12, 96: 14, 97: 13, 98: 10, 99: 10}}, 'Ks. Rodzaju': {'chapters': 50, 'verses': {1: 34, 10: 33, 11: 33, 12: 21, 13: 19, 14: 25, 15: 22, 16: 17, 17: 28, 18: 34, 19: 39, 2: 26, 20: 19, 21: 35, 22: 25, 23: 21, 24: 68, 25: 35, 26: 36, 27: 47, 28: 23, 29: 36, 3: 25, 30: 44, 31: 56, 32: 33, 33: 21, 34: 32, 35: 30, 36: 44, 37: 37, 38: 31, 39: 24, 4: 27, 40: 24, 41: 58, 42: 39, 43: 35, 44: 35, 45: 29, 46: 35, 47: 32, 48: 23, 49: 34, 5: 33, 50: 26, 6: 23, 7: 25, 8: 23, 9: 30}}, 'Ks. Rut': {'chapters': 4, 'verses': {1: 23, 2: 24, 3: 19, 4: 22}}, 'Ks. Sofoniasza': {'chapters': 3, 'verses': {1: 19, 2: 16, 3: 20}}, 'Ks. Sędziów': {'chapters': 21, 'verses': {1: 37, 10: 19, 11: 41, 12: 16, 13: 26, 14: 21, 15: 21, 16: 32, 17: 14, 18: 32, 19: 31, 2: 24, 20: 49, 21: 25, 3: 32, 4: 25, 5: 32, 6: 41, 7: 26, 8: 36, 9: 58}}, 'Ks. Wyjścia': {'chapters': 40, 'verses': {1: 23, 10: 30, 11: 11, 12: 52, 13: 23, 14: 32, 15: 28, 16: 37, 17: 17, 18: 28, 19: 26, 2: 26, 20: 27, 21: 37, 22: 32, 23: 34, 24: 19, 25: 41, 26: 38, 27: 22, 28: 44, 29: 47, 3: 23, 30: 39, 31: 19, 32: 36, 33: 24, 34: 36, 35: 36, 36: 39, 37: 30, 38: 32, 39: 44, 4: 32, 40: 38, 5: 24, 6: 31, 7: 26, 8: 33, 9: 36}}, 'Ks. Zachariasza': {'chapters': 14, 'verses': {1: 22, 10: 13, 11: 18, 12: 15, 13: 10, 14: 21, 2: 14, 3: 11, 4: 15, 5: 12, 6: 16, 7: 15, 8: 24, 9: 18}}, 'Lamentacje': {'chapters': 5, 'verses': {1: 23, 2: 23, 3: 67, 4: 23, 5: 22}}, 'List do Efezjan': {'chapters': 6, 'verses': {1: 24, 2: 23, 3: 22, 4: 33, 5: 34, 6: 24}}, 'List do Filemona': {'chapters': 1, 'verses': {1: 25}}, 'List do Filipian': {'chapters': 4, 'verses': {1: 31, 2: 31, 3: 22, 4: 23}}, 'List do Galatów': {'chapters': 6, 'verses': {1: 25, 2: 22, 3: 30, 4: 32, 5: 27, 6: 18}}, 'List do Hebrajczyków': {'chapters': 13, 'verses': {1: 15, 10: 40, 11: 41, 12: 30, 13: 25, 2: 19, 3: 20, 4: 17, 5: 15, 6: 21, 7: 29, 8: 14, 9: 29}}, 'List do Kolosan': {'chapters': 4, 'verses': {1: 30, 2: 24, 3: 26, 4: 18}}, 'List do Rzymian': {'chapters': 16, 'verses': {1: 33, 10: 22, 11: 37, 12: 22, 13: 15, 14: 24, 15: 34, 16: 27, 2: 30, 3: 32, 4: 26, 5: 22, 6: 24, 7: 26, 8: 40, 9: 34}}, 'List do Tytusa': {'chapters': 3, 'verses': {1: 17, 2: 16, 3: 15}}, 'List Jakuba': {'chapters': 5, 'verses': {1: 28, 2: 27, 3: 19, 4: 18, 5: 20}}, 'List Judy': {'chapters': 1, 'verses': {1: 25}}, 'Objawiene Jana': {'chapters': 22, 'verses': {1: 21, 10: 12, 11: 20, 12: 18, 13: 19, 14: 21, 15: 9, 16: 22, 17: 19, 18: 25, 19: 22, 2: 30, 20: 16, 21: 28, 22: 22, 3: 23, 4: 12, 5: 15, 6: 18, 7: 18, 8: 14, 9: 22}}, 'Pieśń nad Pieśniami': {'chapters': 8, 'verses': {1: 18, 2: 18, 3: 12, 4: 17, 5: 17, 6: 14, 7: 14, 8: 14}}}
ksiegi = [
    "Ks. Rodzaju",
    "Ks. Wyjścia",
    "Ks. Kapłańska",
    "Ks. Liczb",
    "Ks. Powt. Prawa",
    "Ks. Jozuego",
    "Ks. Sędziów",
    "Ks. Rut",
    "I Ks. Samuela",
    "II Ks. Samuela",
    "I Ks. Królewska",
    "II Ks. Królewska",
    "I Ks. Kronik",
    "II Ks. Kronik",
    "Ks. Ezdrasza",
    "Ks. Nehemiasza",
    "Ks. Estery",
    "Ks. Hioba",
    "Ks. Psalmów",
    "Ks. Przysłów",
    "Ks. Kaznodziei",
    "Pieśń nad Pieśniami",
    "Ks. Izajasza",
    "Ks. Jeremiasza",
    "Lamentacje",
    "Ks. Ezechiela",
    "Ks. Daniela",
    "Ks. Ozeasza",
    "Ks. Joela",
    "Ks. Amosa",
    "Ks. Abdiasza",
    "Ks. Jonasza",
    "Ks. Micheasza",
    "Ks. Nahuma",
    "Ks. Habakuka",
    "Ks. Sofoniasza",
    "Ks. Aggeusza",
    "Ks. Zachariasza",
    "Ks. Malachiasza",
    "Ew. Mateusza",
    "Ew. Marka",
    "Ew. Łukasza",
    "Ew. Jana",
    "Dzieje Apostolskie",
    "List do Rzymian",
    "I List do Koryntian",
    "II List do Koryntian",
    "List do Galatów",
    "List do Efezjan",
    "List do Filipian",
    "List do Kolosan",
    "I List do Tesaloniczan",
    "II List do Tesaloniczan",
    "I List do Tymoteusza",
    "II List do Tymoteusza",
    "List do Tytusa",
    "List do Filemona",
    "List do Hebrajczyków",
    "List Jakuba",
    "I List Piotra",
    "II List Piotra",
    "I List Jana",
    "II List Jana",
    "III List Jana",
    "List Judy",
    "Księga Objawienia",
]
tlumaczenia = {
    "Ks. Rodzaju": "Genesis",
    "Ks. Wyjścia": "Exodus",
    "Ks. Kapłańska": "Leviticus",
    "Ks. Liczb": "Numbers",
    "Ks. Powt. Prawa": "Deuteronomy",
    "Ks. Jozuego": "Joshua",
    "Ks. Sędziów": "Judges",
    "Ks. Rut": "Ruth",
    "I Ks. Samuela": "1 Samuel",
    "II Ks. Samuela": "2 Samuel",
    "I Ks. Królewska": "1 Kings",
    "II Ks. Królewska": "2 Kings",
    "I Ks. Kronik": "1 Chronicles",
    "II Ks. Kronik": "2 Chronicles",
    "Ks. Ezdrasza": "Ezra",
    "Ks. Nehemiasza": "Nehemiah",
    "Ks. Estery": "Esther",
    "Ks. Hioba": "Job",
    "Ks. Psalmów": "Psalms",
    "Ks. Przysłów": "Proverbs",
    "Ks. Kaznodziei": "Ecclesiastes",
    "Pieśń nad Pieśniami": "Song of Songs",
    "Ks. Izajasza": "Isaiah",
    "Ks. Jeremiasza": "Jeremiah",
    "Lamentacje": "Lamentations",
    "Ks. Ezechiela": "Ezekiel",
    "Ks. Daniela": "Daniel",
    "Ks. Ozeasza": "Hosea",
    "Ks. Joela": "Joel",
    "Ks. Amosa": "Amos",
    "Ks. Abdiasza": "Obadiah",
    "Ks. Jonasza": "Jonah",
    "Ks. Micheasza": "Micah",
    "Ks. Nahuma": "Nahum",
    "Ks. Habakuka": "Habakkuk",
    "Ks. Sofoniasza": "Zephaniah",
    "Ks. Aggeusza": "Haggai",
    "Ks. Zachariasza": "Zechariah",
    "Ks. Malachiasza": "Malachi",
    "Ew. Mateusza": "Matthew",
    "Ew. Marka": "Mark",
    "Ew. Łukasza": "Luke",
    "Ew.Jana": "John",
    "Dzieje Apostolskie": "Acts",
    "List do Rzymian": "Romans",
    "I List do Koryntian": "1 Corinthians",
    "II List do Koryntian": "2 Corinthians",
    "List do Galatów": "Galatians",
    "List do Efezjan": "Ephesians",
    "List do Filipian": "Philippians",
    "List do Kolosan": "Colossians",
    "I List do Tesaloniczan": "1 Thessalonians",
    "II List do Tesaloniczan": "2 Thessalonians",
    "I List do Tymoteusza": "1 Timothy",
    "II List do Tymoteusza": "2 Timothy",
    "List do Tytusa": "Titus",
    "List do Filemona": "Philemon",
    "List do Hebrajczyków": "Hebrews",
    "List Jakuba": "James",
    "I List Piotra": "1 Peter",
    "II List Piotra": "2 Peter",
    "I List Jana": "1 John",
    "IIList Jana": "2 John",
    "III List Jana": "3 John",
    "List Judy": "Jude",
    "Księga Objawienia": "Revelation"
}

wybrana_ksiega = tk.StringVar(root)
wybrana_ksiega.set(ksiegi[0])


rozdzialy = []
for i in range(biblia[wybrana_ksiega.get()]['chapters']): rozdzialy.append(i +1)
wybrany_rozdzial = tk.StringVar(root)
wybrany_rozdzial.set(rozdzialy[0])

wersety = []
wybrany_werset = tk.StringVar(root)
for i in range(biblia[wybrana_ksiega.get()]['verses'][int(wybrany_rozdzial.get())]): wersety.append(i +1)
wybrany_werset.set(wersety[0])

T_ksiega = tk.Label(root, text="Księga")
T_rozdzial = tk.Label(root, text="Rozdział")
T_werset = tk.Label(root, text="Werset")

def Fragment(ksiega , rozdzial, werset):
    z = ""
    if (int(werset) >= 1 or int(werset) < int(biblia[ksiega]['verses'][int(rozdzial)]) ):
        sciezka_do_pliku = "biblia_podzielona/" + ksiega +" "+ rozdzial + ".txt"

        with open(sciezka_do_pliku, 'r',encoding='windows-1250' ) as plik:
            for linia in plik:
         
       
                if linia.startswith(f'<v n="{werset}">'):
                    return linia[len(f'<v n="{werset}">')+1:].strip().rstrip('</v> </c> <b>')
        return z
    
def FragmentUK(ksiega , rozdzial, werset):
    z = ""
    if (int(werset) >= 1 or int(werset) < int(biblia[ksiega]['verses'][int(rozdzial)]) ):
        sciezka_do_pliku = "biblia_podzielona_UK/" + tlumaczenia[ksiega] +" "+ rozdzial + ".txt"

        with open(sciezka_do_pliku, 'r', encoding='UTF-8') as plik:
            for linia in plik:
                    if linia.startswith(f'{werset}.'):
                        return linia[len(f'{werset}.')+1:].strip()
        return z
    
def FragmentEN(ksiega , rozdzial, werset):
    z = ""
    if (int(werset) >= 1 or int(werset) < int(biblia[ksiega]['verses'][int(rozdzial)]) ):
        sciezka_do_pliku = "biblia_podzielona_EN/" + tlumaczenia[ksiega] +" "+ rozdzial + ".txt"

        with open(sciezka_do_pliku, 'r', encoding='UTF-8') as plik:
            for linia in plik:
         
       
                if linia.startswith(f'{werset}.'):
                    return linia[len(f'{werset}.')+1:].strip() 
        return z

def UpFra(event = None):
    podglad.configure(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()) )
    poprzedni.configure(text=f'{int(wybrany_werset.get())-1}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), int(wybrany_werset.get())-1) )
    nastepny.configure(text=f'{int(wybrany_werset.get())-1}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), int(wybrany_werset.get())+1) )
    
    
def UpWer(event = None):
    wersety=[]
    for i in range(biblia[wybrana_ksiega.get()]['verses'][int(wybrany_rozdzial.get())]): wersety.append(i +1)
    dropdown3['menu'].delete(0, 'end')
    for werset in wersety:
        dropdown3['menu'].add_command(label=werset, command=lambda opt=werset: [wybrany_werset.set(opt), UpFra()]) 
    wybrany_werset.set(wersety[0])
  
   
    UpFra()
    
    
def UpRoz(event = None):
    
    rozdzialy=[]
    for i in range(biblia[wybrana_ksiega.get()]['chapters']): rozdzialy.append(i +1)
    dropdown2['menu'].delete(0, 'end')
    
    for rozdzial in rozdzialy:
        dropdown2['menu'].add_command(label=rozdzial, command=lambda opt=rozdzial: [wybrany_rozdzial.set(opt), UpWer()])
    wybrany_rozdzial.set(rozdzialy[0])
    UpWer()



def nextW():
    if int(wybrany_werset.get()) < int(biblia[wybrana_ksiega.get()]['verses'][int(wybrany_rozdzial.get())]):
        wybrany_werset.set(int(wybrany_werset.get())+1)
        UpFra()
        show()
    else:
        if int(wybrany_rozdzial.get()) < biblia[wybrana_ksiega.get()]['chapters']:
            wybrany_rozdzial.set(int(wybrany_rozdzial.get())+1)
            wybrany_werset.set(1)
            UpWer()
            show()
        
def prevW():
    if int(wybrany_werset.get()) >1:
        wybrany_werset.set(int(wybrany_werset.get())-1)
        UpFra()
        show()
    else:
        if int(wybrany_rozdzial.get()) > 1:
           wybrany_rozdzial.set(int(wybrany_rozdzial.get())-1)
           UpWer()
           wybrany_werset.set(int(biblia[wybrana_ksiega.get()]['verses'][int(wybrany_rozdzial.get())]))
           
           show()
           
        

# def Ang():
#     if angielski.get() == 1:
#         ang=False
#     else:
#         ang=True
    
    
# def Uk():
#     if ukrainski:
#         ukr=False
#     else:
#         ukr=True
    



def Lewo(event):
    prevW()
def Prawo(event):
    nextW()
          
def BlindPrzycisk(event):
    blind()
def blind(event = None):
    label.config(text="")
def show(event =  None):
    # if angielski and not ukrainski:
    #     label.config(text="")
    #     label.config(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())+ 
    #             f'\n\n{wybrany_werset.get()}. ' + FragmentEN(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()) , 
    #              font=("Arial", 36), fg="white", bg="black")
    # elif ukrainski and not angielski :
    #     label.config(text="")
    #     label.config(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())+ 
    #             f'\n\n{wybrany_werset.get()}. ' + FragmentUK(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()) , 
    #              font=("Arial", 36), fg="white", bg="black")
    # elif ukrainski and  angielski :
    #     label.config(text="")
    #     label.config(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())+ 
    #             f'\n\n{wybrany_werset.get()}. ' + FragmentUK(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())+
    #             f'\n\n{wybrany_werset.get()}. ' + FragmentEN(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()), 
    #              font=("Arial", 36), fg="white", bg="black")
    # else:
    #     label.config(text="")
    #     label.config(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()),
    #              font=("Arial", 36), fg="white", bg="black")
    label.config(text="", wraplength=second_screen.winfo_width())
    label.config(text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())+ 
            f'\n\n{wybrany_werset.get()}. ' + FragmentUK(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())
             +f'\n\n{wybrany_werset.get()}. ' + FragmentEN(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get())
             + f'\n\n{wybrana_ksiega.get()} {wybrany_rozdzial.get()}.{wybrany_werset.get()}'
              ,font=("Arial",28), fg="white", bg="black")


root.bind("<Left>",Lewo)
root.bind("<Right>",Prawo)

second_screen.bind("<Left>",Lewo)
second_screen.bind("<Right>",Prawo)



label = tk.Label(second_screen, text=" ")
label.pack(expand=True,  fill=tk.BOTH)
dropdown = tk.OptionMenu(root, wybrana_ksiega, *ksiegi, command=UpRoz)
dropdown2 = tk.OptionMenu(root, wybrany_rozdzial, *rozdzialy, command=UpWer)
dropdown3 = tk.OptionMenu(root, wybrany_werset, *wersety, command=UpFra)

root.bind("<Key-b>",BlindPrzycisk)
second_screen.bind("<Key-b>",BlindPrzycisk)

angielski = tk.IntVar()
ukrainski = tk.IntVar()

# checkbox2 = tk.Checkbutton(root, text="Angielski",variable=angielski, onvalue=1, offvalue=0, command=Ang)
# checkbox3 = tk.Checkbutton(root, text="Ukraiński",variable=ukrainski, onvalue=1, offvalue=0,command=Uk)

nextButton = tk.Button(root, text='>',command=nextW)
prevButton = tk.Button(root, text='<', command=prevW)

blindButton = tk.Button(root, text = 'blind',command= blind)
showButton = tk.Button(root, text = 'show', command=show)

T_ksiega.grid(row=0, column=0,sticky='nsew')
T_rozdzial.grid(row=0, column=1,sticky='nsew')
T_werset.grid(row=0, column=2,sticky='nsew')

dropdown.grid(row=1, column=0,sticky='nsew')
dropdown2.grid(row=1, column=1,sticky='nsew')
dropdown3.grid(row=1, column=2,sticky='nsew')


# checkbox2.grid(row=2, column=1,sticky='s')
# checkbox3.grid(row=2, column=2,sticky='s')

prevButton.grid(row=3, column=0,sticky='sw',padx = 30)
nextButton.grid(row=3, column=2,sticky='se',padx = 30)
blindButton.grid(row=3, column=0,sticky='e',padx = 30)
showButton.grid(row=3, column=1,sticky='se',padx = 30)

x = int(wybrany_werset.get()) - 1
y = int(wybrany_werset.get()) + 1

poprzedni = tk.Label(root, text=f'{x}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), x ))
nastepny  = tk.Label(root, text=f'{y}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), y ))
podglad = tk.Label(root, text=f'{wybrany_werset.get()}. ' + Fragment(wybrana_ksiega.get(), wybrany_rozdzial.get(), wybrany_werset.get()) )
poprzedni.grid(row= 4, column =0, columnspan=3 )
podglad.grid(row= 5, column =0, columnspan=3 )
nastepny.grid(row= 6, column =0, columnspan=3 )

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)



        
# Uruchomienie głównej pętli programu
root.mainloop()

