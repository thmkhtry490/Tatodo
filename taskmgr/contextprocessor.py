from taskmgr import __version__
def version(request):
    " send app version to all pages"
    return {"version" : __version__}