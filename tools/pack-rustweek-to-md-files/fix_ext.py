import os


def rename_markdown_to_md(folder_path):
    """
    Renames all files with the .markdown extension to .md in a specified folder.

    Args:
        folder_path (str): The absolute or relative path to the folder
                           containing the files to be renamed.
    """
    if not os.path.isdir(folder_path):
        print(
            f"Error: The folder '{folder_path}' does not exist or is not a directory."
        )
        print("Please check the path and try again.")
        return

    print(f"Scanning folder: {folder_path}\n")
    renamed_count = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".markdown"):
            old_file_path = os.path.join(folder_path, filename)

            base_name, _ = os.path.splitext(filename)
            new_filename = base_name + ".md"
            new_file_path = os.path.join(folder_path, new_filename)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                renamed_count += 1
            except OSError as e:
                print(f"Error renaming file {filename}: {e}")

    if renamed_count == 0:
        print("No files with the .markdown extension were found to rename.")
    else:
        print(f"\nFinished. Renamed {renamed_count} file(s).")


if __name__ == "__main__":
    target_folder = "/Users/yehorsmoliakov/Downloads/rust-learning/materials/this-week-in-rust/content"

    rename_markdown_to_md(target_folder)
