import eel
import desktop
import search

app_name = "html"
end_point = "index.html"
size = (700, 600)



def kimetsu_search(word, filename):
    search.kimetsu_search(word, filename)


desktop.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)
