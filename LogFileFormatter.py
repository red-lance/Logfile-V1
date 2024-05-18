def logfileformatter(filepath): 
    with open(filepath, "r") as f, open("Formatted_LogFile.txt", "w") as g:
        data = f.readlines()[4:]
        for line in data:
            if line.strip():  
                parts = line.split()
                identifier = parts[2] + "\t"
                hex_bytes = parts[6:]
                grouped_bytes = ["".join((hex_bytes[i:i+2])[::-1])for i in range(0, len(hex_bytes), 2)]
                grouped_bytes.reverse()
                formatted_hex = " ".join(grouped_bytes)
                g.write(f"{identifier} {formatted_hex}\n")

filepath = input("Enter File name/path: ")
logfileformatter(filepath)