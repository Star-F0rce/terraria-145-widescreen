import argparse


parser = argparse.ArgumentParser(description="Widescreen Patcher for Terraria 1.4.5.1")

parser.add_argument("file", type=str, help="Terraria.exe path")
parser.add_argument("width", type=int, help="Monitor width")
parser.add_argument("height", type=int, help="Monitor Height")
args = parser.parse_args()
width_value = args.width - 1
height_value = args.height - 1


MaxWorldViewSize = bytes.fromhex("04 20 80 07 00 00 20 B0 04")

with open(args.file, "rb") as f:
    data = bytearray(f.read())

index = data.find(MaxWorldViewSize)

if index == -1:
    raise RuntimeError("Pattern not found")
else:
    print(f"MaxWorldViewSize found")

width_hex = width_value.to_bytes(2, byteorder="little", signed=False)
height_hex = height_value.to_bytes(2, byteorder="little", signed=False)
if args.width > 1920:
    print(f"Replacing width with {width_hex.hex()}")
    data[index + 2 : index + 4] = width_hex

if args.height > 1200:
    print(f"Replacing height with {height_hex.hex()}")
    data[index + 7 : index + 9] = height_hex

with open(args.file, "wb") as f:
    f.write(data)

print("All done! Have fun with 1.4.5!")
