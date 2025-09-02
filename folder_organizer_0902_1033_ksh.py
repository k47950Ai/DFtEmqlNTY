# 代码生成时间: 2025-09-02 10:33:15
import os
import shutil
from cherrypy import expose, request, Response

"""
Folder Organizer - A CherryPy application to organize directories and files.

This application provides an HTTP interface to organize files and folders on a server.
It includes error handling and ensures that the code is easily maintainable and extendable.
"""

class FolderOrganizer(object):

    """
    A CherryPy application to organize folders and files.
    """

    def __init__(self):
        pass

    @expose
    def index(self):
        """
        The index function that serves the main page.
        """
        return "Folder Organizer Service is Running."

    @expose
    def organize(self, source_folder, target_folder, **kwargs):
        """
        Organize files from source_folder to target_folder.

        :param source_folder: The folder to be organized.
        :param target_folder: The destination folder.
        """
        if not os.path.exists(source_folder):
            return Response("Source folder does not exist.", status=404)
        if not os.path.exists(target_folder):
            return Response("Target folder does not exist.", status=404)

        try:
            for item in os.listdir(source_folder):
                source_path = os.path.join(source_folder, item)
                target_path = os.path.join(target_folder, item)
                if os.path.isfile(source_path):
                    # Move file to target folder if it doesn't exist
                    if not os.path.exists(target_path):
                        shutil.move(source_path, target_path)
                elif os.path.isdir(source_path):
                    # Recursively organize the subdirectory
                    self.organize(source_path, target_path)
        except Exception as e:
            return Response(f"An error occurred: {e}", status=500)
        return Response("Files organized successfully.", status=200)

if __name__ == '__main__':
    """
    Run the CherryPy application.
    """
    conf = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8080,
        }
    }
    folder_organizer = FolderOrganizer()
    cherrypy.quickstart(folder_organizer, config=conf)