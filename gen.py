import os
import html

def generate_links(base_dir="."):
    links = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".html") and file != "index.html":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                href = html.escape(rel_path)
                display_name = html.escape(rel_path)
                links.append(f'<li><a href="{href}">{display_name}</a></li>')
    return links

def write_index_html(links, output_file="index.html"):
    joined = '\n        '.join(links)
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML Index</title>
</head>
<body>
    <h1>Index of HTML files</h1>
    <ul>
        {joined}
    </ul>
</body>
</html>"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    links = generate_links(".")
    write_index_html(links)
    print("index.html generated successfully.")
