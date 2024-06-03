import os

def text2md(text, source_link):
    # Initialize variables to store extracted data
    data = []
    current_label = None
    source_text = None
    source_link = source_link
    star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'
    # Split the text by lines
    lines = text.strip().split('\n')
    md_text = []
    sidebar_text = "    * "
    
    for line in lines:
        # Check for '##' headers
        if line.startswith('# '):
            source_text = line[2:].strip()
            
        # Check for '##' headers
        if line.startswith('## '):
            current_label = line[3:].strip()
        
        # Check for '###' headers
        elif line.startswith('### '):
            current_title = line[4:].strip()
        
        # Check for links
        elif line.startswith('- 链接：'):
            current_link = line.split('链接：')[1].strip()
        
        # Check for descriptions
        elif line.startswith('- 介绍：'):
            current_description = line.split('介绍：')[1].strip()
            data.append((current_label, current_title, current_link, current_description))

    # Print the extracted data
    for entry in data:
        label, title, link, description = entry
        final_str = "| "
        if len(link) > 0:
            if link.find("github.com") != -1:
                github_item = '/'.join(link.split('/')[-2:])
                final_str += star_format.format(github_item, github_item)
                final_str += "<br> "
            final_str += "[{}]({})".format(title, link)
        final_str += " |"
        if len(description) > 0:
            final_str += "{} ".format(description)
        final_str += " |"
        if len(label) > 0:
            final_str += "{}".format(label)
        final_str += " |"
        if len(source_text) > 0:
            final_str += "[{}]({})".format(source_text, source_link)
        final_str += " |"
        md_text.append(final_str)
    if len(source_text) > 0:
        sidebar_text += "[{}]({})".format(source_text, source_link)
    return md_text, sidebar_text



def read_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def append_lines_to_file(file_path, lines):
    try:
        if isinstance(lines, str):
            lines = [lines]
        else:
            lines = lines
        # 读取输出文件中的现有内容
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_lines = set(line.strip() for line in file)
        else:
            existing_lines = set()
        
        # 过滤掉已经存在于文件中的内容
        new_lines = [line for line in lines if line not in existing_lines]
        
        # 如果没有新内容需要追加，退出
        if not new_lines:
            print("所有内容已存在，忽略追加操作。")
            return
        
        # 追加新的内容到文件
        with open(file_path, 'a', encoding='utf-8') as file:
            for line in new_lines:
                file.write(line + '\n')  # 每个元素作为一行追加，并在末尾添加换行符
        print("新内容追加成功!")
    except Exception as e:
        print(f"发生错误: {e}")



if __name__ == '__main__':
    
    new_file = "20240601-20240607.md"
    
    # Get the current working directory
    current_directory = os.getcwd()
    docs_directory = os.path.join(os.path.dirname(current_directory), "docs")
    readme = os.path.join(docs_directory, 'README.md')
    sidebar = os.path.join(docs_directory, '_sidebar.md')
    file_md = os.path.join(docs_directory, "contents", new_file[:-3], new_file)
    source_link = "contents/{}/{}".format(new_file[:-3], new_file)
    content = read_file(file_md)
    contents, sidebar_text = text2md(content, source_link)
    append_lines_to_file(readme, contents)
    append_lines_to_file(sidebar, sidebar_text)