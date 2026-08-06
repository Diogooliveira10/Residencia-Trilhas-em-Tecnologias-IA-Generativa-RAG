import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

METADATA_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "metadata",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "titulo": {
                    "type": ["string", "null"]
                },
                "autores": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "string"
                    }
                },
                "ano": {
                    "type": ["integer", "null"]
                },
                "resumo": {
                    "type": ["string", "null"]
                },
                "palavras_chave": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "titulo",
                "autores",
                "ano",
                "resumo",
                "palavras_chave"
            ],
            "additionalProperties": False
        }
    }
}


def extract_metadata(
        path_markdown: str | Path,
        path_json: str | Path
) -> None:

    path_markdown = Path(path_markdown)
    path_json = Path(path_json)

    path_json.mkdir(parents=True, exist_ok=True)

    output_file = path_json / f"{path_markdown.stem}.json"

    try:
        document_text = path_markdown.read_text(encoding="utf-8")

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": (
                        """
                            Você é um especialista em análise de artigos científicos.

                            Extraia do documento as seguintes informações:
                            - título
                            - autores
                            - ano de publicação
                            - resumo
                            - palavras-chave

                            Regras:
                            - Extraia apenas informações explicitamente presentes no documento.
                            - Nunca invente ou infira dados.
                            - Se um campo estiver ausente, retorne `null`.
                            - Preserve o texto original do documento.
                            - Não inclua explicações ou texto adicional.
                        """
                    )
                },
                {
                    "role": "user",
                    "content": document_text
                }
            ],
            response_format=METADATA_SCHEMA,
            temperature=0,
            max_tokens=500
        )

        metadata = json.loads(response.choices[0].message.content)

        output_file.write_text(
            json.dumps(metadata, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )

        print(f"Converted {path_markdown.name} to {output_file}")

    except Exception as e:
        print(f"Failed to extract metadata from {path_markdown.name}: {e}")


if __name__ == "__main__":
    extract_metadata(
        "markdown/twitter_algoritmo.md",   # caminho do markdown a processar
        "json"                         # pasta de destino do .json
    )
