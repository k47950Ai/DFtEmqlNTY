# 代码生成时间: 2025-09-03 04:02:15
import os
import cherrypy
def batch_rename(source_folder, destination_folder, new_extension=None):
    """批量重命名文件的函数。
    
    Args:
    source_folder (str): 源文件夹路径。
    destination_folder (str): 目标文件夹路径。
    new_extension (str, optional): 新的文件扩展名，如果为None，则保留原有扩展名。
    
    Returns:
    list: 成功重命名的文件列表。
    
    Raises:
    FileNotFoundError: 如果源文件夹不存在。
    """
    if not os.path.exists(source_folder):
        raise FileNotFoundError("源文件夹不存在。")
    
    renamed_files = []
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            if new_extension:
                name += new_extension
                new_filename = f"{name}{ext}"
            else:
                new_filename = filename
            new_path = os.path.join(destination_folder, new_filename)
            os.rename(file_path, new_path)
            renamed_files.append(filename)
    return renamed_files

def expose_rename(*args, **kwargs):
    """CherryPy暴露的重命名函数。
    
    通过CherryPy web服务接收参数，并调用batch_rename函数。
    """
    try:
        source = kwargs.get('source')
        destination = kwargs.get('destination')
        extension = kwargs.get('extension')
        result = batch_rename(source, destination, extension)
        return {"status": "success", "renamed_files": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# CherryPy服务配置
class BatchRenameTool:
    exposed = True
    def POST(self, **kwargs):
        "