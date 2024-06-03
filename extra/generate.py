 
project_name = 'ChatTTS webUI & API'
github_url = 'https://github.com/jianchang512/ChatTTS-ui'
introduction = '​​Omost是一个将编码能力转换为LLM图像生成能力的项目..'
label = 'LLM'
source_text = 'awesome'
source_link = 'contents/20231218-20231224/20231218-20231224.md'
star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'



final_str = "| "
if len(github_url) > 0:
    github_item = '/'.join(github_url.split('/')[-2:])
    final_str += star_format.format(github_item, github_item)
    final_str += "<br> "
    final_str += "[{}]({})".format(project_name, github_url)
final_str += " |"
if len(introduction) > 0:
    final_str += "{} ".format(introduction)
final_str += " |"
if len(label) > 0:
    final_str += "{}".format(label)
final_str += " |"
if len(source_text) > 0:
    final_str += "[{}]({})".format(source_text, source_link)
final_str += " |"
print(final_str)
