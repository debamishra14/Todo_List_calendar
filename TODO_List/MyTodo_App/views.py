from django.shortcuts import render, redirect
from .models import Status, TodoList
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.exceptions import MultipleObjectsReturned

from django.views.generic import View
import json
from django.http import HttpResponseRedirect
from MyTodo_App.mixins import SerializeMixin, HttpResponseMixin

from MyTodo_App.utils import is_json



def index(request):
    todos  = TodoList.objects.all()
    statuss = Status.objects.all()

    if request.method == 'POST':
        if 'taskAdd' in request.POST:
            try:
                title = request.POST['title']
                description = request.POST['description']
                status = request.POST['status_select']
                date = request.POST['date']
                Todo = TodoList(title=title,description=description,due_date=date, status=Status.objects.get(name = status))

                Todo.save()
                messages.success(request, 'Todo item is added Successfully.')
                return redirect('/')

            except Exception:
                messages.error(request, 'Kindly Fill all the fields.')


        if 'taskDelete' in request.POST:
            try:
                checkedlist = request.POST.getlist('checkedbox')
                for todo_id in checkedlist:
                    todo = TodoList.objects.get(id=int(todo_id))
                    todo.delete()
                    messages.success(request, 'Todos deleted Successfully!')

            except MultiValueDictKeyError:
                messages.error(request, 'Kindly select something to Delete!')


        if 'taskModify' in request.POST:
            try:
                checkedlist = request.POST.getlist('checkedbox')
                if len(checkedlist)>1:
                    messages.error(request, 'Kindly do not select multple items to Modify at same time.')
                    return redirect('/')
                else:
                    todo = TodoList.objects.get(id=int(checkedlist[0]))
                    return render(request,'modify.html',{'todo':todo, 'statuss':statuss})

            except MultiValueDictKeyError:
                messages.error(request, 'Kindly select something to Modify!')

    return render(request, 'index.html', {'todos':todos, 'statuss':statuss})


def update(request,id):
    todos  = TodoList.objects.all()
    statuss = Status.objects.all()

    todo = TodoList.objects.get(id=id)

    todo.title = request.POST['title']
    todo.description = request.POST['description']
    todo.status = Status.objects.get(name = request.POST['status_select'])
    todo.due_date = request.POST['date']
    todo.save()
    messages.success(request, 'Todo item is Updated Successfully.')

    return HttpResponseRedirect('/')



# FOR api call use
class ListViewCBV(HttpResponseMixin, SerializeMixin, View):
    def get_object_by_id(self,id):
        try:
            todo = TodoList.objects.get(id=id)
        except TodoList.DoesNotExist:
            todo = None
        return todo

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'plz send valid json data'})
            return self.render_to_HttpResponse(json_data,status=400)

        pdata = json.loads(data)
        id = pdata.get('id',None)

        if id is not None:
            todo = self.get_object_by_id(id)
            if todo is None:
                json_data = json.dumps({'msg':"No matched TODO List found with this id"})
                return self.render_to_HttpResponse(json_data, status=404)
            json_data = self.serialize([todo])
            return self.render_to_HttpResponse(json_data)

        qs = TodoList.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_HttpResponse(json_data)
