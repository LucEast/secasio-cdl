import os
import re
import requests

try:
    import inquirer
    from inquirer import Path
    from inquirer import errors
except:
    print("Install requirements with 'pip3 install -r requirements'")

questions = [inquirer.Path(
    'coursefile', message='Please enter path of the course-file', exists=True, path_type=Path.FILE),
    inquirer.Path('dest_path', message="Where do you want to save the content?", exists=True, path_type=Path.DIRECTORY)]

answers = inquirer.prompt(questions)
input_file = answers['coursefile']
output_dir = answers['dest_path']


class course:
    def __init__(self, file):
        self.file = file

    def find_md_links(self):
        # inline_link_re = re.compile(
        #     r'\[!(\[([^\]]+)\])\(([^)]+)\)]\(([^)]+)\)')
        inline_link_re = re.compile(
            r'((https?):((//secasio.de)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)')
        # links = list(inline_link_re.findall(self.file))
        # print(links)
        with open(self.file, 'r') as f:
            links = inline_link_re.findall(f.read())
            accessed_lists = []
            for link in links:
                accessed_lists.append(link[0])
                # print(link[0])
            return(accessed_lists)

    def get_content(self):
        accessed_lists = self.find_md_links()
        for accessed_list in accessed_lists:
            complete_name = os.path.join(output_dir, accessed_list[0])
            response = requests.get(accessed_list[1])
            open(complete_name, "wb").write(response.content)


if __name__ == "__main__":
    cfile = course(input_file)
    cfile.get_content()
