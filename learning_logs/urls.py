"""定义learning_logs的url模式"""
from django.urls import path
from . import views
app_name = "learning_logs"
urlpatterns = [
    #homepage
    path('',views.index,name='index'),
    #show all topics
    path('topics/',views.topics,name='topics'),
    #特定主题详细页面
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #add a new topic page
    path('new_topic/',views.new_topic,name='new_topic'),
    #add a new entry page
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #use to edit entry page
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry')
    

]
