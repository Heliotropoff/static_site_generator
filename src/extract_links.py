import re

def extract_markdown_images(text):
    extracted_img_data = []
    img_md_pattern = r"!\[[^\]]*]\([^)]+\)"
    alt_text_pattern = r"(?<=\[)(.+)(?=\])"
    url_pattern = r"\(([^)]+)\)$" #r"https:\/\/(.+)(?=\))"
    imgs = re.findall(img_md_pattern,text)
    for img in imgs:
        alt_text = re.search(alt_text_pattern, img).group()
        img_url = re.search(url_pattern, img).group(1)
        extracted_img_data.append((alt_text, img_url))
    return extracted_img_data

def extract_markdown_links(text):
    extracted_links_data = []
    link_md_pattern = r"(?<!\!)\[[^\]]*]\([^)]+\)"
    anchor_text_pattern = r"(?<=\[)(.+)(?=\])"
    url_pattern = r"\(([^)]+)\)$"
    links = re.findall(link_md_pattern,text)
    for link in links:
        anchor_text = re.search(anchor_text_pattern, link).group()
        link_url = re.search(url_pattern, link).group(1)
        extracted_links_data.append((anchor_text, link_url))
    return extracted_links_data
