from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    markdown_line_list = markdown.split("\n")
    markdown_title = markdown_line_list[0].strip()
    if markdown_title[0] != "#":
        raise Exception("No h1 header in markdown")
    title = markdown_title.lstrip("#").lstrip()
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    source_markdown = ""
    with open(from_path, "r", encoding="utf8") as markdown_source_file:
        source_markdown = markdown_source_file.read()
        markdown_source_file.close()
    #print(source_markdown)

    template_html = ""
    with open(template_path, "r", encoding="utf8") as html_template_file:
        template_html = html_template_file.read()
        html_template_file.close()
    #print(template_html)

    html_node = markdown_to_html_node(source_markdown)
    html_result = html_node.to_html()
    #print(html_result)

    title = extract_title(source_markdown)
    #print(title)

    result_html = template_html.replace("{{ Title }}", title)
    result_html = result_html.replace("{{ Content }}", html_result)
    #print(result_html)

    with open(dest_path, "w", encoding="utf8") as out_html_file:
        out_html_file.write(result_html)
        out_html_file.close()