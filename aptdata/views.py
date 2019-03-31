"""
from django.shortcuts import render, get_object_or_404
from .models import aptinfo



def index(request):
    list=aptinfo.objects.all()
    context={'list':list}
    return render(request,'aptdata/index.html',context)

def detail(request, apt_id):
    apt=get_object_or_404(aptinfo,pk=apt_id)
    return render(request, 'aptdata/details.html',{'apt':apt})

"""
from django.views import generic
from .models import aptinfo,Emp,aptboards,aptactivity,advertiser_details,client_categoery,campaign_details,apt_deals
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login, logout, get_user_model
from django.views.generic import View
from .forms import userform,add_apt,update_emp,board_detail,board_update,activity_detail,activity_update,update_apt,advt_detail,advt_update,client_cat,userloginform
from django.http import Http404, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.mixins import UserPassesTestMixin
"""
    These are views related to Apartment details

    here need to change the view of the index page.
    as this should show the data in the following format

    Apt name - Area - Number of boards vacant

"""
#@login_required
class indexview (generic.ListView):
    template_name = 'aptdata/index.html'
    # paginate_by = 2
    queryset = aptinfo.objects.all()
    # check how to include page numbers in the tempalte here.
    # def get_queryset(self):
    #     return aptinfo.objects.all()





class detailview(generic.DetailView):
    model = aptinfo
    template_name = 'aptdata/details.html'
    def get_context_data(self, **kwargs):
        context = super(detailview, self).get_context_data(**kwargs)
        context['apt_status_list'] = aptboards.objects.filter(apt_code_id=self.kwargs.get('pk')).filter(board_status='Vacant').count()#.values_list('board_status').count()
        return context

# here we need to include the role validation with user_passes_test and check if the user has the admin role
def validate(user):

    val = emp.objects.filter(emp_name=user).values('emp_dept')
    if val == 'admin':
        return True
    else:
        return False

# @user_passes_test(validate)
class addapt(CreateView):
    model = aptinfo
    form_class = add_apt

class updateapt(UpdateView):
    model = aptinfo
    form_class = update_apt

class deleteapt(DeleteView):
    model = aptinfo
    success_url = reverse_lazy('aptinfo:index')

"""
    These are employee related views

"""

class listemp(generic.ListView):
    template_name = 'aptdata/emplist.html'
    def get_queryset(self):
        return Emp.objects.all()

class empdetail(generic.DetailView):
    model = Emp
    template_name = 'aptdata/empdetail.html'

class updateemp(UpdateView):
    model = Emp
    form_class = update_emp

class addemp(CreateView):
    model = Emp
    form_class = update_emp

"""
    These are boards related views

"""

class boardlist(generic.ListView):
    template_name = 'aptdata/boardlist.html'

    def get_queryset(self):
        return aptboards.objects.filter(apt_code_id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super(boardlist,self).get_context_data(**kwargs)
        context['variable']=aptinfo.objects.get(id=self.kwargs.get('pk'))
        context['val'] = self.kwargs.get('pk')
        return context


class addboard(CreateView):
    model = aptboards
    form_class = board_detail

    def get_form_kwargs(self):
        kwargs= super(addboard,self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

class boarddetail(generic.DetailView):
    model = aptboards
    template_name = 'aptdata/boarddetail.html'
    #form_class = board_detail

class vacantboarddetail(generic.ListView):
    model = aptboards
    template_name = 'aptdata/vacantdetail.html'

    def get_queryset(self):
        #Player.objects.values('player_type').order_by().annotate(Count('player_type'))
        return aptboards.objects.values('apt_code').filter(board_status='Vacant').annotate(Vcount=Count('apt_code'))#.select_related('apt_code_id')


    """def get_context_data(self, **kwargs):
        return super(vacantboarddetail,self).get_context_data(total_count=self.get_queryset().count(), **kwargs)

        context = super(vacantboarddetail, self).get_context_data(**kwargs)
        context['name'] = aptboards.objects.values('apt_code')
        context['vacantcount'] = aptboards.objects.filter(board_status='vacant').count()
        return context"""

class updateboard(UpdateView):
    model = aptboards
    form_class = board_update

"""
    These are activity related views
"""

class activitylist(generic.ListView):

    template_name = 'aptdata/aptactivitylist.html'

    def get_queryset(self):
        return aptactivity.objects.filter(apt_code_id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super(activitylist,self).get_context_data(**kwargs)
        context['variable']=aptinfo.objects.get(id=self.kwargs.get('pk'))
        context['val'] = self.kwargs.get('pk')
        return context

class addactivity(CreateView):
    model = aptactivity
    form_class = activity_detail

    def get_form_kwargs(self):
        kwargs= super(addactivity,self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

class updateactivity(UpdateView):
    model = aptactivity
    form_class = activity_update

class activitydetail(generic.DetailView):
    model = aptactivity
    template_name = 'aptdata/aptactivitydetail.html'

    """def get_context_data(self, **kwargs):
        context = super(activitydetail,self).get_context_data(**kwargs)
        context['variable']=aptactivity.objects.get(id=self.kwargs.get('pk'))
        context['val'] = self.kwargs.get('val')
        return context"""

    """def get_form_kwargs(self):
        kwargs= super(activitydetail,self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs"""

# From here the generic views for advertiser starts

class add_advt(generic.CreateView):
    model = advertiser_details
    form_class = advt_detail

class advt_list(generic.ListView):
    model = advertiser_details
    template_name = 'aptdata/advtlist.html'

    def get_queryset(self):
        return advertiser_details.objects.all()

class advt_updated(UpdateView):
    model = advertiser_details
    form_class = advt_update

class advtdetail(generic.DetailView):
    model = advertiser_details
    template_name = 'aptdata/advtdetails.html'

class categoery_view(generic.ListView):
    template_name = 'aptdata/categoerylist.html'

    def get_queryset(self):
        return client_categoery.objects.filter(client_name_id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super(categoery_view,self).get_context_data(**kwargs)
        context['variable']=advertiser_details.objects.get(id=self.kwargs.get('pk'))
        context['val'] = self.kwargs.get('pk')
        return context

class categoery_add(generic.CreateView):
    model = client_categoery
    form_class = client_cat


class campaign_detail(generic.ListView):
    template_name = 'aptdata/campaign_details.html'

    def get_queryset(self):
        return campaign_details.objects.filter(client_name_id = self.kwargs.get('pk'))

class campaign_add(generic.CreateView):
    model = campaign_details
    form_class = campaign_detail

# def userformview(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/aptdata')
#     else:
#         form = UserCreationForm()

#         args = {'form':form}
#         return render(request, 'aptdata/reg_form.html', args)



class userformview(View):
    form_class = userform
    template_name = 'aptdata/registration_form.html'#'aptdata/registration_form.html'

    #display empty form when the user first login
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})
    #process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #validate the user credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('aptdata:index')
        return render(request, self.template_name, {'form': form})



class userloginview(View):
    form_class = userloginform
    template_name = 'aptdata/login_form.html'#'aptdata/registration_form.html'

    #display empty form when the user first login
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})
    #process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user.set_password(password)
            #user.save()

            #validate the user credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if Emp.objects.filter(emp_name=request.user.username).values('emp_dept')[0]['emp_dept'] == 'ADMIN':
                        return redirect('aptdata:index')
                    else:
                        return redirect('aptdata:get_user_page')
                else:
                    return redirect('aptdata:incorrect')
        return render(request, self.template_name, {'form': form})

def loginpage(request):
    return HttpResponse("Seems either username or password is incorrect")

class get_user_page(generic.ListView):
    
    template_name = 'aptdata/getuserpage.html'

    def get_queryset(self, **kwargs):
        return aptactivity.objects.filter(activity_done_by = self.request.user)

    def get_context_data(self, **kwargs):
        context = super(get_user_page,self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context
        

    """def __init__(self, *args, **kwargs):
        super(get_user_page, self).__init__(**kwargs)
        self.queryset = aptactivity.objects.filter(activity_done_by=self.request.user)

    def get_queryset(self):
        return aptactivity.objects.filter(activity_done_by=user)
    
    def get_context_data(self, **kwargs):
        context = super(categoery_view,self).get_context_data(**kwargs)
        context['variable']=advertiser_details.objects.get(id=self.kwargs.get('pk'))
        context['val'] = self.kwargs.get('pk')
        return context"""

# @login_required
def user_logout(request):
    #context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    #return HttpResponse("You have succesfully logged out")
    messages.success(request, "You have been succesfully logged out!")
    return redirect('aptdata:login')

"""
            if Emp.objects.filter(emp_name=request.user.username).values('emp_dept')[0]['emp_dept'] == 'ADMIN':
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                return HttpResponse("Welcome buddy")
"""