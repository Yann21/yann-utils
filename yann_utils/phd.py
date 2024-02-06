import pandas as pd
import subprocess
import os

def csv_to_latex_png(df, png_filename, caption):
    # 1. Convert the df to LaTeX table format
    latex_code = r"""
    \documentclass{standalone}
    \usepackage{booktabs}
    \begin{document}
    """
    latex_code += df.to_latex(index=True, escape=False, caption=caption)
    latex_code += r"\end{document}"

    with open("temp_table.tex", "w") as latex_file:
        latex_file.write(latex_code)

    # 2. Compile the LaTeX to produce a PDF
    subprocess.call(["pdflatex", "-interaction=nonstopmode", "temp_table.tex"])

    # 3. Convert the PDF to PNG
    subprocess.call(["pdftoppm", "-png", "temp_table.pdf", "temp_table"])

    # Rename to the desired png filename
    os.rename("temp_table-1.png", png_filename)

    # Clean up intermediate files
    for ext in [".tex", ".aux", ".log", ".pdf"]:
        os.remove("temp_table" + ext)