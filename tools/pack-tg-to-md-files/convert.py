"""
This script converts an exported Telegram chat (in JSON) into Markdown files to feed them into NotebookLM
"""

import math
import json
import os
import datetime as dt
from pathlib import Path


def timestamp_to_datetime(timestamp_s) -> dt.datetime:
    return dt.datetime.fromtimestamp(timestamp_s).replace(tzinfo=None)


def split_list_into_files(string_list, total_files, directory):
    if directory and not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory)

    total_strings = len(string_list)
    if total_strings == 0:
        print("The list of texts is empty. No files will be created.")
        return

    strings_per_file = math.ceil(total_strings / total_files)

    print(f"Total strings: {total_strings}")
    print(f"Number of files to create: {total_files}")
    print(f"Strings per file (approximately): {strings_per_file}")
    print("-" * 30)

    for i in range(total_files):
        start_index = i * strings_per_file
        end_index = start_index + strings_per_file

        file_content_list = string_list[start_index:end_index]

        if not file_content_list:
            break

        file_name = f"output_{i + 1}.md"
        file_path = os.path.join(directory, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(file_content_list))

            print(
                f"Successfully created {file_path} with {len(file_content_list)} strings."
            )

        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    print("-" * 30)
    print("Processing complete.")


class Conv:
    def convert_to_markdown(self, message_data):
        if "text_entities" not in message_data:
            item = message_data.get("text", "")
            markdown_text = ""

            if isinstance(item, str):
                markdown_text += item
            elif isinstance(item, dict):
                if item.get("type") == "code":
                    markdown_text += f"`{item.get('text', '').strip()}`"
                    if "\n" in item.get("text", ""):
                        markdown_text += "\n"

            final_text = markdown_text.replace("\n`", "`\n")

            return final_text

        markdown_parts = []
        for entity in message_data["text_entities"]:
            text = entity.get("text", "")
            entity_type = entity.get("type")
            language = entity.get("language")

            if entity_type == "bold":
                markdown_parts.append(f"**{text}**")
            elif entity_type == "italic":
                markdown_parts.append(f"*{text}*")
            elif entity_type == "code":
                markdown_parts.append(f"`{text}`")
            elif entity_type == "pre":
                markdown_parts.append(f"```{language}\n{text}\n```")
            elif entity_type == "link":
                url = entity.get("text", "#")
                markdown_parts.append(f"[{text}]({url})")
            else:
                markdown_parts.append(text)

        return ("".join(markdown_parts)).strip()

    def convert_note(self, message: dict) -> str:
        note_body = []
        if message["type"] != "message":
            return ""

        final_text = self.convert_to_markdown(message)

        if len(final_text) == 0:
            return ""

        message_time = timestamp_to_datetime(int(message["date_unixtime"]))
        note_body.append(
            f"{message_time.strftime('%Y-%m-%d %H:%M:%S')}, "
            f"**{message['from']}**: {final_text}"
        )

        return "\n\n".join(note_body)


conv = Conv()

file_or_folder = Path("/Users/yehorsmoliakov/Downloads/tg-chat")
input_json = json.loads((file_or_folder / "result.json").read_text(encoding="utf-8"))
output_directory = "chunked"
num_files = 300  # maximum sources NotebookLM supports

texts = []
for msg in input_json["messages"]:
    text = conv.convert_note(msg)
    if not text:
        continue
    texts.append(text)

split_list_into_files(texts, num_files, output_directory)
