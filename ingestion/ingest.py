# Data ingestion script for RAG project
import pandas as pd
from pathlib import Path

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
# Get our rows from each type of file
def get_rows(path : Path):
    if path.suffix == ".csv":
        data = pd.read_csv(path, chunksize=CHUNK_SIZE, dtype=str, keep_default_na=False)
        for chunk in data:
            for index, row in chunk.iterrows():
                # build and return our row
                yield {
                    "_source": path.name,
                    "_sheet": "",
                    "_row": index,
                    **row.to_dict(),
                }

    elif path.suffix in {".xlsx", ".xls", ".xlsm"}:
        with (pd.ExcelFile(path) as file):
            for sheet_name in file.sheet_names:
                data = pd.read_excel(file, sheet_name=sheet_name, dtype=str, keep_default_na=False)
                for index, row in data.iterrows():
                    yield {
                        "_source": path.name,
                        "_sheet": sheet_name,
                        "_row": index,
                        **row.to_dict(),
                    }

# break up our text into chunks
def chunk_text(str):
    if len(str) > CHUNK_SIZE:
        yield str
        return

    i = 0
    while i < len(str):
        end = min(len(str), i + CHUNK_SIZE)
        yield str[i:end]
        i += CHUNK_SIZE-CHUNK_OVERLAP

# build readable text from our rows
def build_text(row):
    return "\n".join(
        f"{col}: {str(value).strip()}"
        for col, value in row.items()
        if not col.startswith("_") and str(value).strip()
    )

# Main
def main():
    files = sorted(Path(".").glob("**/*.csv")) + sorted(Path(".").glob("**/*.xlsx"))
    if len(files) == 0:
        print("No files found")
        return

    # container for our data
    data = []

    for path in files:
        for row in get_rows(path):
            text = build_text(row)
            for chunk_index, chunk in enumerate(chunk_text(text)):
                data.append({
                    "source": path.name,
                    "sheet": str(row["_sheet"]),
                    "row": str(row["_row"]),
                    "chunk_index": chunk_index,
                    "content": chunk
                })


    # TODO: Pass this to our vector database
    print(data)


if __name__ == "__main__":
    main()