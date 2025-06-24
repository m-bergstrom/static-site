from os import listdir, mkdir, path, remove
import shutil

from blocktype import BlockType, block_to_block_type
from md_to_blocks import block_to_heading_node, markdown_to_blocks, markdown_to_html_node

def main():
    copy_static(path.abspath("./static"), path.abspath("./public"))
    generate_pages_recursive(path.abspath("./content"), path.abspath("./template.html"), path.abspath("./public/"))

def copy_static(source: str, target :str):
    if path.exists(target):
        entries = listdir(target)
        for entry in entries:
            full_entry_path = path.join(target, entry)
            if path.isfile(full_entry_path):
                remove(full_entry_path)
            else:
                shutil.rmtree(full_entry_path)
    entries = listdir(source)
    if len(entries) > 0 and not path.exists(target):
        mkdir(target)
    for entry in entries:
        full_entry_path = path.join(source, entry)
        if path.isfile(full_entry_path):
            shutil.copy(full_entry_path, target)
        else:
            copy_static(full_entry_path, path.join(target, entry))
    
def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    try:
        header_block = next(filter(
            lambda h: h.tag == "h1", 
            map(block_to_heading_node, 
                filter(lambda block: block_to_block_type(block) == BlockType.HEADING, 
                    blocks)
                )
            )
        )
        if (not header_block.value
            and header_block.children
            and len(header_block.children) > 0):
            return next(filter(lambda b: b.value, header_block.children)).value or ""

        return header_block.value or ""
    except StopIteration:
        raise Exception("No top-level header found")
    
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    entries = listdir(dir_path_content)
    for entry in entries:
        full_entry_path = path.join(dir_path_content, entry)
        if path.isfile(full_entry_path):
            if entry.endswith(".md"):
                entry = path.splitext(entry)[0] + ".html"
                generate_page(full_entry_path, template_path, path.join(dest_dir_path, entry))
        else:
            generate_pages_recursive(full_entry_path, template_path, path.join(dest_dir_path, entry))

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, "r") as source:
        with open(template_path, "r") as template:
            source_text = source.read()
            template_text = template.read()
            content = markdown_to_html_node(source_text).to_html()
            title = extract_title(source_text)
            dest_text = template_text.replace("{{ Title }}", title).replace("{{ Content }}", content)

            if not path.exists(path.dirname(dest_path)):
                create_directory(path.dirname(dest_path))
                #mkdir(path.dirname(dest_path))
            with open(dest_path, "w") as dest:
                dest.write(dest_text)

def create_directory(dest_path: str):
    if len(dest_path) == 0:
        raise ValueError
    if not path.exists(path.dirname(dest_path)):
        try:
            create_directory(path.dirname(dest_path))
        except ValueError as ex:
            raise ValueError("{dest_path} root doesn't exist")
    mkdir(dest_path)

if __name__ == "__main__":
    main()