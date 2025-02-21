import pathlib

import markdown


def convert_md_to_html(md_file_path):
    # Read the markdown file
    with open(md_file_path, encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title from the first # heading
    title = ""
    for line in md_content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Create Markdown converter with extensions
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'attr_list'])
    
    # Convert markdown to HTML
    html_content = md.convert(md_content)
    
    # Create HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../../style.css">
    <link rel="stylesheet" href="../style.css">
    <script defer data-domain="piebro.github.io" src="https://plausible.io/js/plausible.js"></script>
</head>
<body>
<nav>
    <a href="../../index.html" class="nav-link">Projects</a> |
    <a href="../index.html" class="nav-link">Blog Posts</a> |
    <a href="../../about.html" class="nav-link">About</a>
</nav>
{html_content}
<br>
<br>
<br>
<br>
<br>
<br>
</body>
</html>
"""
    # Write the HTML file to the same directory as the markdown file
    html_file_path = md_file_path.with_suffix('.html')
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

def process_blog_directory():
    blog_dir = pathlib.Path('blog')
    
    # Find all directories in the blog folder
    for dir_path in blog_dir.iterdir():
        if dir_path.is_dir():
            # Check if index.md exists in the directory
            md_file = dir_path / 'index.md'
            if md_file.exists():
                print(f"Converting {md_file}")
                convert_md_to_html(md_file)

if __name__ == "__main__":
    process_blog_directory()
