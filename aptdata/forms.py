from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import aptinfo,Emp,aptboards,aptactivity,advertiser_details,client_categoery,campaign_details,apt_deals\
        , UserProfile
from django.forms import ModelForm
import datetime
from django.forms.widgets import Select
from dateutil.relativedelta import relativedelta

class DateInput(forms.DateTimeInput):

    input_type = 'date'

class TimeInput(forms.DateTimeInput):

    input_type = 'time'

class userform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','email','password']

def result():
    list=Emp.objects.values_list('id','emp_name')
    return list

"""
aggrement_sign_date = models.DateField(default='', null=True, blank=True)
    aggrement_start_date = models.DateField(default='', null=True, blank=True)
    aggrement_end_date """
class add_apt(ModelForm):
    required_css_class = 'required'
    def __init__(self, *args, **kwargs):
        super(add_apt, self).__init__(*args, **kwargs)
        self.fields['record_owner'] = forms.ChoiceField(choices=result())


    class Meta:
        model = aptinfo
        fields = [
                'aptname','area','address','landmark','apt_pic','record_owner','sales_remainder_date','sales_remainder_time',
                'apt_status','no_of_flats','no_of_blocks','total_board_count','primary_contact','primary_contact_number',
                'secondary_contact','secondary_contact_number','watchman_name','watchman_contact','distance_from_mainroad_in_km',
                'aggrement_sign_date','aggrement_start_date','aggrement_end_date','bank_name', 'bank_account_name',
                'account_number', 'ifsc_code', 'cost_of_A2','cost_of_A3','cost_of_2X4','cost_of_3X6',
                'owner_flats','rented_flats','total_male_count',
                'total_female_count','male_5_15_years','male_16_26_years','male_27_50_years','male_above_50_years','female_5_15_years',
                'female_16_26_years','female_27_50_years','female_above_50_years','families_with_cars','num_of_families_participate_activity',
                'people_into_industry_count','male_software','male_civil','male_business','male_telecom','male_construction','male_sales',
                'male_education','male_manufacturing','male_media','male_household','female_software','female_civil','female_business',
                'female_telecom','female_construction','female_sales','female_education','female_manufacturing','female_media',
                'female_household','avg_maintenance_cost_per_house',
        ]
        widgets = {
            'sales_remainder_date': DateInput(),
            'sales_remainder_time': TimeInput(),
            'aggrement_sign_date' : DateInput(),
            'aggrement_start_date' : DateInput(),
            'aggrement_end_date' : DateInput(),
        }

class update_apt(ModelForm):
    def __init__(self, *args, **kwargs):
        super(update_apt, self).__init__(*args, **kwargs)
        self.fields['record_owner'] = forms.ChoiceField(choices=result())


    class Meta:
        model = aptinfo
        fields = [
                'record_owner','sales_remainder_date','sales_remainder_time',
                'apt_status','no_of_flats','no_of_blocks','total_board_count',
                'secondary_contact','secondary_contact_number','watchman_name','watchman_contact','distance_from_mainroad_in_km',
                'aggrement_sign_date','aggrement_start_date','aggrement_end_date','bank_name', 'bank_account_name',
                'account_number', 'ifsc_code', 'cost_of_A2','cost_of_A3','cost_of_2X4','cost_of_3X6',
                'owner_flats','rented_flats','total_male_count',
                'total_female_count','male_5_15_years','male_16_26_years','male_27_50_years','male_above_50_years','female_5_15_years',
                'female_16_26_years','female_27_50_years','female_above_50_years','families_with_cars','num_of_families_participate_activity',
                'people_into_industry_count','male_software','male_civil','male_business','male_telecom','male_construction','male_sales',
                'male_education','male_manufacturing','male_media','male_household','female_software','female_civil','female_business',
                'female_telecom','female_construction','female_sales','female_education','female_manufacturing','female_media',
                'female_household','avg_maintenance_cost_per_house',
        ]
        widgets = {
            'sales_remainder_date': DateInput(),
            'sales_remainder_time': TimeInput(),
            'aggrement_sign_date' : DateInput(),
            'aggrement_start_date' : DateInput(),
            'aggrement_end_date' : DateInput(),
        }


class update_emp(ModelForm):

    def __init__(self,*args, **kwargs):
        super(update_emp, self).__init__(empty_permitted=False,*args, **kwargs)
        #pdate_emp.empty_permitted = False

    class Meta:

        model = Emp
        fields = [
            'emp_name','emp_type','emp_join_date','emp_pic','emp_dept','emp_blood_group','emp_designation','emp_dob',
        ]
        widgets = {
            'emp_join_date':DateInput(),
            'emp_dob':DateInput(),
        }

    def clean_emp_dob(self):

        data = self.cleaned_data['emp_dob']

        if relativedelta(datetime.date.today(), data).years < 21:
            raise ValidationError("Your are not more than 21 years of age.")

        return data

    def clean_emp_join_date(self):

        data = self.cleaned_data['emp_join_date']

        if data > datetime.date.today():
            raise ValidationError("Employee joining date cannot be in future.")

        return data




class board_detail(ModelForm):

    def __init__(self, pk=None,*args, **kwargs):
        super(board_detail, self).__init__(*args, **kwargs)
        self.fields['apt_code'].queryset = aptinfo.objects.filter(pk=pk)

    class Meta:

        model = aptboards
        fields = [
            'apt_code','board_location','block_name','board_type','board_size','board_status','board_pic',
        ]

class board_update(ModelForm):

    class Meta:
            model = aptboards
            fields = [
                  'board_status', 'board_pic',
            ]

class activity_detail(ModelForm):

    def __init__(self, pk=None,*args, **kwargs):
        super(activity_detail, self).__init__(*args, **kwargs)
        self.fields['apt_code'].queryset = aptinfo.objects.filter(pk=pk)
        self.fields['ad_location'].queryset = aptboards.objects.filter(apt_code_id=pk)

    class Meta:

        model = aptactivity
        fields = [
            'emp_name', 'apt_code', 'proposed_date_of_activity', 'actual_date_of_activity', 'activity',
            'ad_location', 'activity_pic','activity_done_by', 'activity_details', 'status',
        ]
        widgets = {
            'proposed_date_of_activity':DateInput(),
            'actual_date_of_activity':DateInput(),
        }

class activity_update(ModelForm):

    class Meta:

        model = aptactivity
        fields = [
            'emp_name',
            'proposed_date_of_activity', 'actual_date_of_activity', 'activity',
            'activity_pic','activity_done_by', 'activity_details', 'status',
        ]
        widgets = {
            'proposed_date_of_activity':DateInput(),
            'actual_date_of_activity':DateInput(),
        }

class advt_detail(ModelForm):

    class Meta:

        model = advertiser_details
        fields = [
            'client_name','contact_person','contact_number','contact_email','preferred_date','preferred_time','status',
        ]
        widgets = {
            'preferred_date':DateInput(),
            'preferred_time':TimeInput(),
        }


class advt_update(ModelForm):

    class Meta:
        model = advertiser_details
        fields = [
             'preferred_date', 'preferred_time',
            'status',
        ]
        widgets = {
            'preferred_date': DateInput(),
            'preferred_time': TimeInput(),
        }

class client_cat(ModelForm):
    """def __init__(self, pk=None,*args, **kwargs):
        super(client_cat, self).__init__(*args, **kwargs)
        self.fields['client_name'].queryset = aptinfo.objects.filter(pk=pk)"""

    class Meta:
        model = client_categoery

        fields = [
            'client_name','product_categoery','product_name',
        ]

class campaign_detail(ModelForm):

    class Meta:

        model = campaign_details

        fields= [
            'client_name','product_name','campaign_id',    'campaign_poster',    'start_date',    'end_date',
        ]

        widgets = {
            'start_date':DateInput(),
            'end_date': DateInput(),
        }


class userform(forms.ModelForm):
    """docstring for userloginform"forms.Form def __init__(self, arg):
        super userloginform,forms.Form.__init__()
        self.arg = arg"""
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model = User
        fields = ['username', 'email', 'password']

class userloginform(forms.ModelForm):
    """docstring for userloginform"forms.Form def __init__(self, arg):
        super userloginform,forms.Form.__init__()
        self.arg = arg"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model = UserProfile
        fields = ['username', 'password']


        