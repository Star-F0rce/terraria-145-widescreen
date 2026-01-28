import argparse


parser = argparse.ArgumentParser(description="Widescreen Patcher for Terraria")

parser.add_argument("file", type=str, help="Terraria.exe path")
parser.add_argument("width", type=int, help="Monitor width")
parser.add_argument("height", type=int, help="Monitor Height")
args = parser.parse_args()
offset_width = 4212051
offset_height = 4212056
width_value = args.width - 1
height_value = args.height - 1

width_hex = width_value.to_bytes(2, byteorder="little", signed=False)
height_hex = height_value.to_bytes(2, byteorder="little", signed=False)

if args.width > 1920:
    with open(args.file, "r+b") as f:
        print(f"Writing {width_hex.hex()} at 0x404553")
        f.seek(offset_width)
        f.write(width_hex)
    
if args.height > 1200:
    with open(args.file, "r+b") as f:
        print(f"Writing {height_hex.hex()} at 0x404558")
        f.seek(offset_height)
        f.write(height_hex)

print(f"All done! Have fun with 1.4.5!")