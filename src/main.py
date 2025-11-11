from file_manager import copy_static_from_source, generate_page
import shutil
def main():

    copy_static_from_source("./static", "./public")
    generate_page(from_path="content/index.md",template_path="./template.html", dest_path="./public/index.html")


if __name__ == "__main__":
    main()
