import argparse


parser = argparse.ArgumentParser(description="Widescreen Patcher for Terraria 1.4.5.1")

parser.add_argument("file", type=str, help="Terraria.exe path")
parser.add_argument("width", type=int, help="Monitor width")
parser.add_argument("height", type=int, help="Monitor Height")
args = parser.parse_args()
offset_width_loc = "0x4049D3"
offset_height_loc = "0x4049D8"
offset_width = int(offset_width_loc,16)
offset_height = int("0x4049D3",16)
width_value = args.width - 1
height_value = args.height - 1

width_hex = width_value.to_bytes(2, byteorder="little", signed=False)
height_hex = height_value.to_bytes(2, byteorder="little", signed=False)

if args.width > 1920:
    with open(args.file, "r+b") as f:
        print(f"Writing {width_hex.hex()} at {offset_width_loc}")
        f.seek(offset_width)
        f.write(width_hex)
    
if args.height > 1200:
    with open(args.file, "r+b") as f:
        print(f"Writing {height_hex.hex()} at {offset_height_loc}")
        f.seek(offset_height)
        f.write(height_hex)

print(f"All done! Have fun with 1.4.5!")
