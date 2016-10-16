class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_new_project(self, Project):
        wd = self.app.wd
        self.navigation_projects_page()
        wd.find_element_by_xpath(".//*[@id='content']/div[2]/form/fieldset/input[2]").click()
        self.fill_project_properties(Project)
        wd.find_element_by_xpath(".//*[@id='manage-project-create-form']/fieldset/span/input").click()

    def navigation_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='menu-items']/li[7]/a").click()
        wd.find_element_by_xpath(".//*[@id='manage-menu']/ul/li[2]/a").click()


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

    def delete_project(self,id):
        wd = self.app.wd
        self.navigation_projects_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath(".//*[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath(".//*[@id='content']/div/form/input[4]").click()

    def select_project_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="manage_proj_edit_page.php?project_id=%s"]' % project_id).click()


