from file_manager import copy_static_from_source, generate_page,generate_pages_recursive
import sys
def main(site_root_path):
    base_path = site_root_path
    copy_static_from_source("./static", "./docs")
    #generate_page(from_path="content/index.md",template_path="./template.html", dest_path="./public/index.html")
    generate_pages_recursive(dir_path_content="./content",  template_path="./template.html", dest_dir_path="./docs", basepath=base_path)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        main("/")
