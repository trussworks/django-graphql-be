from os import path

def root_dir() -> str:
    """
    Returns the invoke root directory (aka the project root)
    so that tasks can use it and be directory agnostic 
    """
    return path.dirname(path.dirname(__file__))

def server_path() -> str:
    """
    Returns the server path
    so that tasks can use it and be directory agnostic 
    """
    return path.join(root_dir(), 'server/')

def tasks_path() -> str:
    """
    Returns the tasks path
    so that tasks can use it and be directory agnostic 
    """
    return path.join(root_dir(), 'tasks/')