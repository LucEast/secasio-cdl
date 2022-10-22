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
    'coursefile', message='Please enter path of the ".md" course-file', exists=True, path_type=Path.FILE)]

answers = inquirer.prompt(questions)['coursefile']


class course:
    def __init__(self, file):
        self.file = file

    def find_md_links(self):
        inline_link_re = re.compile(
            r'\[!(\[([^\]]+)\])\(([^)]+)\)]\(([^)]+)\)')
        # links = list(inline_link_re.findall(self.file))
        # print(links)
        with open(self.file, 'r') as f:
            links = inline_link_re.findall(f.read())
            indices_to_access = [1, 3]
            accessed_lists = []
            for link in links:
                link_map = map(link.__getitem__, indices_to_access)
                accessed_lists.append(list(link_map))
                # print(accessed_list)
            return accessed_lists

    def get_content(self):
        accessed_lists = self.find_md_links()
        for accessed_list in accessed_lists:
            response = requests.get(accessed_list[1])
            open(accessed_list[0], "wb").write(response.content)


if __name__ == "__main__":
    cfile = course(answers)
    cfile.get_content()
