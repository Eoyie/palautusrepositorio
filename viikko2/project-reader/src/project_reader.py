from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        c_dict = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(c_dict['tool']['poetry']['name'], c_dict['tool']['poetry']['description'], c_dict['tool']['poetry']['license'], c_dict['tool']['poetry']['authors'], list(c_dict['tool']['poetry']['dependencies'].keys()), list(c_dict['tool']['poetry']['group']['dev']['dependencies'].keys()))
