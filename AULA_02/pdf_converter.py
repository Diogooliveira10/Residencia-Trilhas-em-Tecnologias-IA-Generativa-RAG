import os

os.environ["TORCH_COMPILE_DISABLE"] = "1"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from pathlib import Path


""" 
Desativa OCR e reduz o processamento de imagens: PDFs com texto nativo
(não escaneados) não precisam disso, e essa é a principal causa do
estouro de memória (std::bad_alloc) em páginas mais densas. 
"""
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False
pipeline_options.do_table_structure = True
pipeline_options.generate_page_images = False
pipeline_options.images_scale = 1.0

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

def convert_pdf(
        path_pdf: str | Path,
        path_markdown: str | Path
) -> None:

    path_pdf = Path(path_pdf)
    path_markdown = Path(path_markdown)

    path_markdown.mkdir(parents=True, exist_ok=True)

    markdown = path_markdown / f"{path_pdf.stem}.md"

    try:
        document = converter.convert(path_pdf).document
        markdown.write_text(
            document.export_to_markdown(),
            encoding="utf-8"
        )

        print(f"Converted {path_pdf.name} to {markdown}")

    except Exception as e:
        print(f"Failed to convert {path_pdf.name}: {e}")


if __name__ == "__main__":
    convert_pdf(
        "pdfs/twitter_algoritmo.pdf",   # caminho do PDF a converter
        "markdown"                      # pasta de destino do .md
    )
