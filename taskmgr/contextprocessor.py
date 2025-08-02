from taskmgr import __version__
def version(request):
    return {"version" : __version__}