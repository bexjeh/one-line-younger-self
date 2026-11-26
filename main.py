import os

LINE = "Kid, return the library book you stole in year nine \u2014 the fine is pennies, but you'll still be carrying it at thirty."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
