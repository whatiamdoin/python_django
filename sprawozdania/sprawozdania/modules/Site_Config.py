import os


class Site_Config():
    def __init__(self):
        script_path = os.path.abspath( __file__ )
        self.allowed_extensions = ('.pdf', '.docx', '.doc')
        self.html_location = script_path.replace('sprawozdania\modules\Site_Config.py', 'sprawozdania\\templates\index.html')
        self.html_after_save_location = script_path.replace('sprawozdania\modules\Site_Config.py', 'sprawozdania\\templates\saved.html')

        #Destination can be configured by placing path to folder or defaults it's project root folder named "sprawozdania"
        files_destination = ""
        if(len(files_destination) > 0):
            self.files_destination_final = files_destination
        else:
            self.files_destination_final = script_path.replace('sprawozdania\modules\Site_Config.py', 'sprawozdania\\pliki_sprawozdania\\')

    def get_allowed_extensions(self):
        return self.allowed_extensions

    def get_html_location(self):
        return self.html_location

    def get_html_after_save_location(self):
        return self.html_after_save_location

    def get_files_destination_final(self):
        return self.files_destination_final
