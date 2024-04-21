import os
from jinja2 import Template

def find_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html") and "plugin" not in root:
                html_files.append({
                    "path": os.path.join(root, file),
                    "relative_path": os.path.relpath(os.path.join(root, file), directory),
                    "basename": os.path.basename(file),
                    "linkname": root.split("/")[1]
                })
    return html_files

def create_index_html(html_files, template_path="index_template.html", output_path="index.html"):
    with open(template_path, "r") as template_file:
        template_content = template_file.read()
        template = Template(template_content)

    rendered_template = template.render(html_files=html_files)

    with open(output_path, "w") as index_file:
        index_file.write(rendered_template)

if __name__ == "__main__":
    sessions_directory = "sessions"
    html_files = find_html_files(sessions_directory)
    create_index_html(html_files)
    print("Index.html created successfully.")
