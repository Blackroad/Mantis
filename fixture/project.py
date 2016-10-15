from Model.projectmodel import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_new_project(self, Project):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='menu-items']/li[7]/a").click()
        wd.find_element_by_xpath(".//*[@id='manage-menu']/ul/li[2]/a").click()
        wd.find_element_by_xpath("manage_proj_create_page_token").click()
        self.fill_project_properties(Project)
        wd.find.element_by_xpath(".//*[@id='manage-project-create-form']/fieldset/span/input").click()

    def fill_project_properties(self, Project):
        wd = self.app.wd
        self.change_field_value("name", Project.name)
        self.change_field_value("description", Project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)