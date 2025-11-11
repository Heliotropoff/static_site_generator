import os
import shutil
from block_handler import markdown_to_html_node, extract_title
from pprint import pprint

def copy_static_from_source(source_dir, destination_dir):
    print(f"current working directory is: {os.getcwd()}, all paths are relative to cwd")
    print(f"working with source dir:{source_dir} and destination dir: {destination_dir}")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        print(f"{destination_dir} already existed, removing it")
    print("creating new destination directory")
    os.mkdir(destination_dir)
    print("checking source contents")
    dir_contents = os.listdir(source_dir)
    print(f"current contents: {dir_contents}")
    if dir_contents:
        for item in dir_contents:
            current_source_path = os.path.join(source_dir, item)
            if os.path.isfile(current_source_path):
                print("found files")
                dest_file_path = os.path.join(destination_dir, item)
                print(f"writing files from {current_source_path} to {dest_file_path}")
                shutil.copy(src=current_source_path,dst=dest_file_path)
            else:
                print("found folders")
                new_dest_dir = os.path.join(destination_dir, item)
                print(f"recursive call with new source folder {current_source_path}")
                copy_static_from_source(current_source_path, new_dest_dir)

    return

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(file=from_path, mode="r") as content_doc:
        md_doc_raw = content_doc.read()
    with open(file=template_path, mode="r") as template_doc:
        html_template = template_doc.read()
    content_html = markdown_to_html_node(md_doc_raw).to_html()
    title_string = extract_title(md_doc_raw)
    updated_title = html_template.replace("{{ Title }}", title_string)
    new_full_html = updated_title.replace("{{ Content }}", content_html)
    dest = os.path.dirname(dest_path)
    os.makedirs(dest, exist_ok=True)
    with open(file=dest_path,mode="w") as new_html:
        new_html.write(new_full_html)

#generate_page("./content/index.md","./template.html", "./test/index.html")





#copy_static_from_source("./test_source", "./test_dest")