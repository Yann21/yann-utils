import pandas as pd
import subprocess
import os
import tempfile
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def csv_to_latex_png(df, caption="Table", index=False):
  with tempfile.TemporaryDirectory() as temp_dir:
    latex_file = os.path.join(temp_dir, "table.tex")
    pdf_file = os.path.join(temp_dir, "table.pdf")
    png_file = os.path.join(temp_dir, "table.png")
    ppm_file = os.path.join(temp_dir, "table-1.png")

    # LaTeX document
    latex_code = r"""\documentclass{standalone}
\usepackage{booktabs}
\usepackage{preview}
\PreviewEnvironment{tabular}
\begin{document}
"""
    latex_code += df.to_latex(index=index, escape=True, caption=caption)
    latex_code += r"\end{document}"

    # Write LaTeX file
    with open(latex_file, "w") as f:
      f.write(latex_code)

    # Generate PDF
    subprocess.call(
      [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory",
        temp_dir,
        latex_file,
      ],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL,
    )

    # Convert PDF to PNG
    subprocess.call(["pdftoppm", "-png", pdf_file, os.path.join(temp_dir, "table")])

    # Rename generated file
    shutil.move(ppm_file, png_file)

    # Display image inline
    img = mpimg.imread(png_file)
    plt.figure(figsize=(20, 10))
    plt.axis("off")
    plt.imshow(img)
    plt.show()
