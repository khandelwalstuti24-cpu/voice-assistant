import os
import pyttsx3

ORDER_TEXT = "I would like to order two burgers, one fries, and one coke, please."

folder = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(folder, "Order.wav")

engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.save_to_file(ORDER_TEXT, out_path)
engine.runAndWait()

print("Saved:", out_path)