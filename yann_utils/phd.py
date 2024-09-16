#%%
import pandas as pd
import subprocess
import os


def csv_to_latex_png(df, png_filename, caption):
  # 1. Convert the df to LaTeX table format
  latex_code = r"""\documentclass{standalone}
\usepackage{booktabs}
\usepackage{preview}
\PreviewEnvironment{tabular}
\begin{document}
"""
  latex_code += df.to_latex(index=True, escape=True, caption=caption)
  latex_code += r"\end{document}"

  with open("out/temp_table.tex", "w") as latex_file:
    latex_file.write(latex_code)

  subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory=out", "temp_table.tex"])
  subprocess.call(["pdftoppm", "-png", "out/temp_table.pdf", "temp_table"])
  os.rename("temp_table-1.png", "latex_table.png")


#%%
df = pd.read_clipboard()
csv_to_latex_png(df, "latex_table.png", "Reset algorithm")

#%%
df