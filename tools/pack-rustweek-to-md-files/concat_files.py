from pathlib import Path


def concatenate_md_files(source_dir: str, dest_dir: str, chunk_size: int = 10):
    """
    Scans a source directory for .md files and concatenates their content
    into new files in a destination directory.

    Args:
        source_dir (str): The path to the folder with the source .md files.
        dest_dir (str): The path to the folder where merged files will be saved.
        chunk_size (int): The number of .md files to combine into one output file.
    """
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    dest_path.mkdir(parents=True, exist_ok=True)

    if not source_path.is_dir():
        print(f"❌ Error: Source directory '{source_path}' not found.")
        return

    md_files = sorted(source_path.glob("*.md"))

    if not md_files:
        print(f"ℹ️ No .md files found in '{source_path}'.")
        return

    for i in range(0, len(md_files), chunk_size):
        chunk = md_files[i : i + chunk_size]

        output_filename = f"merged_{i // chunk_size + 1}.md"
        output_filepath = dest_path / output_filename

        print(f"Creating '{output_filepath}' from {len(chunk)} files...")
        with output_filepath.open("w", encoding="utf-8") as outfile:
            for md_file in chunk:
                content = md_file.read_text(encoding="utf-8")
                outfile.write(content)
                outfile.write("\n\n---\n\n")

    print(f"\n✅ Success! All files have been processed and saved in '{dest_path}'.")


if __name__ == "__main__":
    SOURCE_FOLDER = "/Users/yehorsmoliakov/Downloads/rust-learning/materials/this-week-in-rust/content"
    DESTINATION_FOLDER = "/Users/yehorsmoliakov/Downloads/rust-learning/materials/this-week-in-rust/content-out"
    FILES_PER_CHUNK = 10

    concatenate_md_files(SOURCE_FOLDER, DESTINATION_FOLDER, FILES_PER_CHUNK)
