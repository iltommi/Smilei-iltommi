import os

def extract_first_comment(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            comment="(no comment found)"
            for line in f:
                if line.startswith("#") and len(line) > 1:
                    comment+=line[1:]
                else:
                    break  # Stop at the first non-empty, non-comment line
    except Exception as e:
        return f"(error reading file: {e})"
    return comment

def list_sorted_py_files_with_comments(directory):
    py_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                rel_path = os.path.relpath(os.path.join(root, file), directory)
                full_path = os.path.join(root, file)
                comment = extract_first_comment(full_path)
                py_files.append((rel_path, comment))

    py_files.sort(key=lambda x: x[0])  # Sort by file path

    md_lines = ["# Benchmarks list\n"]
    for path, comment in py_files:
        md_lines.append(f"- `{path}` : {comment}")

    return "\n".join(md_lines)

# Current directory
directory_path = "../benchmarks"
markdown_list = list_sorted_py_files_with_comments(directory_path)

# Save to Readme.md
with open(f"{directory_path}/Readme.md", "w", encoding='utf-8') as f:
    f.write(markdown_list)
