from xml.dom.minidom import parse

dom = parse('./data/config.xml')

root = dom.documentElement

tag_name = root.getElementsByTagName('platform')
for platform in tag_name:
     print(platform.firstChild.data)

log_info_list = root.getElementsByTagName('login')
for log_info in log_info_list:
    print(log_info.getAttribute('username'))
    print(log_info.getAttribute('password'))