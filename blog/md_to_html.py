import markdown


def convert_md_to_html():
    # Read the markdown file
    with open('blog/2025_02_17_generated_ablum_cover_art/index.md', encoding='utf-8') as f:
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
</body>
</html>
"""
    # Write the HTML file
    with open('blog/2025_02_17_generated_ablum_cover_art/index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

if __name__ == "__main__":
    convert_md_to_html()
