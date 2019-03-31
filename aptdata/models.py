from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms.widgets import Select
from datetime import datetime
from collections import namedtuple
import re
from django.contrib.auth.models import User
from django.db.models.signals import post_save


area_codes=(
        ('ASRN','A S Rao Nagar'),
        ('ABDP','Abdullapurmet'),
        ('ABID','Abids'),
        ('ADRS','Adarsh Nagar'),
        ('ADBT','Adibatla'),
        ('ADKM','Adikmet'),
        ('AFZG','Afzal Gunj'),
        ('AMSG','Almasguda'),
        ('ALWL','Alwal'),
        ('AMBR','Amberpet'),
        ('AMNP','Ameenpur'),
        ('AMRP','Ameerpet'),
        ('ANBG','Anandbagh'),
        ('APPJ','Appa Junction'),
        ('ATPU','Attapur'),
        ('BCHP','Bachupally'),
        ('BDNG','Badangpet'),
        ('BDPL','Bahadurpally'),
        ('BDPR','Bahadurpura'),
        ('BIRG','Bairagiguda'),
        ('BLNG','Bala Nagar'),
        ('BLPR','Balapur'),
        ('BNDG','Bandlaguda'),
        ('BNJH','Banjara Hills'),
        ('BSBG','Basheerbagh'),
        ('BRMG','Beeramguda'),
        ('BGMP','Begumpet'),
        ('BHNR','Bhanur'),
        ('BGRM','Bhogaram'),
        ('BOGD','Bhoiguda'),
        ('BNGR','Bhongir'),
        ('BUNG','Bhuvanagiri'),
        ('BBNG','Bibinagar'),
        ('BNRG','BN Reddy Nagar'),
        ('BDUP','Boduppal'),
        ('BLRM','Bolaram'),
        ('BRBD','Borabanda'),
        ('BWNP','Bowenpally'),
        ('BWRM','Bowrampet'),
        ('BDVL','Budvel'),
        ('BRGL','Burgul'),
        ('CHMP','Champapet'),
        ('CHND','Chanda Nagar'),
        ('CHNG','Chandrayanagutta'),
        ('CHRL','Cherlapally'),
        ('CHVL','Chevalla'),
        ('CKDP','Chikkadapally'),
        ('CHLK','Chilkur'),
        ('CHNT','Chintal'),
        ('CNTK','Chintalkunta'),
        ('CNPG','Chintapallyguda'),
        ('CWDG','Chowdhariguda'),
        ('DMGD','Dammaiguda'),
        ('DSRL','Dasarlapally'),
        ('DYRA','Dayara'),
        ('DOLP','Dhoolpet'),
        ('DSNR','Dilsukhnagar'),
        ('DMLG','Domalguda'),
        ('DLAP','Dullapally'),
        ('DNIG','Dundigal'),
        ('EMAR','East Marredpally'),
        ('ECIL','ECIL'),
        ('EDLG','Edulanagulapalle'),
        ('ERGA','Erragadda'),
        ('FLKN','Falaknuma'),
        ('FLMN','Film Nagar'),
        ('FIND','Financial District'),
        ('GCHB','Gachibowli'),
        ('GGLP','Gagillapur'),
        ('GJLR','Gajularamaram'),
        ('GNDN','Gandhi Nagar'),
        ('GMIS','Gandi Maisamma'),
        ('GNDP','Gandipet'),
        ('GHBZ','Ghansi Bazar'),
        ('GHKS','Ghatkesar'),
        ('GLKN','Golkonda'),
        ('GPNP','Gopanpally'),
        ('GDMA','Gudimalkapur'),
        ('GLIC','Gulshan-e-Iqbal Colony'),
        ('GPCP','Gundlapochampally'),
        ('GNRE','Gunrock Enclave'),
        ('GRGD','Gurram Guda'),
        ('HBSG','Habsiguda'),
        ('HFZP','Hafeezpet'),
        ('HKMP','Hakimpet'),
        ('HNMN','Hanuman Nagar Colony'),
        ('HSMT','Hasmathpet'),
        ('HSTN','Hastinapuram'),
        ('HYTN','Hayat Nagar'),
        ('HITC','Hi Tech City'),
        ('HMYT ','Himayath Nagar'),
        ('HUMY','Humayun Nagar'),
        ('HYDN','Hyder Nagar'),
        ('HYDG','Hyderguda'),
        ('IBHP','Ibrahimpatnam'),
        ('INDR','Indresham'),
        ('ISNA','Isnapur'),
        ('JLPL','Jalpally'),
        ('JMBG','Jam Bagh'),
        ('JWHR','Jawahar Nagar'),
        ('JDMT','Jeedimetla'),
        ('JERA','Jeera'),
        ('JUBL','Jubilee Hills'),
        ('KCHG','Kachiguda'),
        ('KKGD','Kakaguda'),
        ('KLSD','Kalasiguda'),
        ('KNCB','Kanchan Bagh'),
        ('KNDK','Kandukur'),
        ('KPRA','Kapra'),
        ('KRKN','Karkhana'),
        ('KRMN','Karmanghat'),
        ('KRWN','Karwan'),
        ('KTDN','Katedan'),
        ('KVDG','Kavadiguda'),
        ('KVRH','Kavuri Hills'),
        ('KZPL','Kazipally'),
        ('KESR','Keesara'),
        ('KRTB','Khairatabad'),
        ('KSMT','Kismatpur'),
        ('KKPT','Kokapet'),
        ('KLUR','Kollur'),
        ('KMPL','Kompally'),
        ('KNDP','Kondapur'),
        ('KNGK','Kongara Kalan'),
        ('KTGD','Kothaguda'),
        ('KTPT','Kothapet'),
        ('KTUR','Kothur'),
        ('KOTI','Koti'),
        ('KWKR','Kowkur'),
        ('KPHB','KPHB'),
        ('KKTP','Kukatpally'),
        ('KSHG','Kushaiguda'),
        ('LKDP','Lakdi Ka Pul'),
        ('LDRZ','Lal Darwaza'),
        ('LLPT','Lalapet'),
        ('LLGD','Lallaguda'),
        ('LNGH','Langar Houz'),
        ('LBNG','LB Nagar'),
        ('LGMP','Lingampally'),
        ('LTKN','Lothkunta'),
        ('MDHP','Madhapur'),
        ('MDRN','Madhura Nagar'),
        ('MDNG','Madinaguda'),
        ('MHSW','Maheshwaram'),
        ('MSRP','Maisireddipalle'),
        ('MJRG','Majarguda'),
        ('MLKP','Malakpet'),
        ('MLKG','Malkajgiri'),
        ('MLMP','Mallampet'),
        ('MLPR','Mallapur'),
        ('MCHR','Manchirevula'),
        ('MNKD','Manikonda'),
        ('MNGD','Manneguda'),
        ('MNSB','Mansoorabad'),
        ('MRTN','Maruti Nagar'),
        ('MSBT','Masab Tank'),
        ('MZDP','Mazidpur'),
        ('MDKR','Medak Road'),
        ('MDCH','Medchal'),
        ('MDPL','Medipalli'),
        ('MERP','Meerpet'),
        ('MHDP','Mehadipatnam'),
        ('MTUG','Mettuguda'),
        ('MYPR','Miyapur'),
        ('MGLP','Moghalpura'),
        ('MINB','Moinabad'),
        ('MKLA','Mokila'),
        ('MSPT','Moosapet'),
        ('MSRB','Moosarambagh'),
        ('MTGP','Moti Ganpur'),
        ('MTIN','Moti Nagar'),
        ('MOLA','Moula Ali'),
        ('MSHB','Musheerabad'),
        ('MTNG','Muthangi'),
        ('MLRG','Mylargada'),
        ('NCRM','Nacharam'),
        ('NDRG','Nadergul'),
        ('NGRM','Nagaram'),
        ('NGSR','Nagarjuna Sagar Road'),
        ('NGLE','Nagole'),
        ('NLAG','Nallagandla'),
        ('NLKT','Nallakunta'),
        ('NMPL','Nampally'),
        ('NNKR','Nanakramguda'),
        ('NNIG','Nandigama'),
        ('NRYG','Narayanguda'),
        ('NRKT','Narketpalli'),
        ('NRSP','Narsapur'),
        ('NRSI','Narsingi'),
        ('NWSK','Nawab Saheb Kunta'),
        ('NLDR ','Neeladri Nagar'),
        ('NRDM','Neredmet'),
        ('NMLK','New Malakpet'),
        ('NMLP','New Mallepally'),
        ('NNLA','New Nallakunta'),
        ('NZMP','Nizampet'),
        ('NZMP ','Nizampet Road'),
        ('NTRN','NTR Nagar'),
        ('OBWN','Old Bowenpally'),
        ('OSMN','Osman Nagar'),
        ('OSSG','Osman Sagar Road'),
        ('PDMR','Padma Rao Nagar'),
        ('PHDS','Pahadi Shareef'),
        ('PTNC','Patancheru'),
        ('PTGP','Patighanpur'),
        ('PRCH','Peerancheru'),
        ('PRZG','Peerzadiguda'),
        ('PCHM','Pochampally'),
        ('PCHR','Pocharam'),
        ('PRGN ','Pragathi Nagar'),
        ('PRSN','Prashanth Nagar'),
        ('PLMA','Pulimamidi'),
        ('PNJG','Punjagutta'),
        ('PPAL','Puppalaguda'),
        ('QTBP','Quthbullapur'),
        ('QTST','Qutub Shahi Tombs'),
        ('RIDG','Rai Durg'),
        ('RIKL','Raikal'),
        ('RAJB','Raj Bhavan Road'),
        ('RJVN','Rajeev Nagar'),
        ('RJDN','Rajendra Nagar'),
        ('RMNG','Ram Nagar'),
        ('RKPM','Ramakrishnapuram'),
        ('RMTP','Ramanthapur'),
        ('RCPM','Ramchandra Puram'),
        ('RMGP','Ramgopalpet'),
        ('RMFC','Ramoji Film City'),
        ('RMPL','Rampally'),
        ('RGNJ','Rani Gunj'),
        ('RSLP','Rasoolpura'),
        ('RNDG','Rendlagadda'),
        ('RDRM','Rudraram'),
        ('SDRD','S D Road'),
        ('SIDB','Saidabad'),
        ('SIFB','Saifabad'),
        ('SNKP','Sainikpuri'),
        ('SLMN','Saleem Nagar'),
        ('SNTN','Sanath Nagar'),
        ('SNGR','Sangareddy'),
        ('SNJR','Sanjeeva Reddy Nagar'),
        ('STNG','Santosh Nagar'),
        ('SRRN','Saroor Nagar'),
        ('SCBD','Secunderabad'),
        ('SLNG','Serilingampally'),
        ('SHDN','Shadnagar'),
        ('SHBD','Shahbaad'),
        ('SHKP','Shaikpet'),
        ('SMRP','Shamirpet'),
        ('SMSB','Shamshabad'),
        ('SKRP','Shankarpalli'),
        ('SHNT','Shanthi Nagar'),
        ('SERG','Sheriguda'),
        ('SDRT','Siddhartha Nagar'),
        ('SNDC','Sindhi Colony'),
        ('STPH','Sitaphalmandi'),
        ('SVRM','Sivarampalli'),
        ('SMJG','Somajiguda'),
        ('SRNC','Sri Nagar Colony'),
        ('SRNG','Srinagar Colony'),
        ('SBSN','Subhash Nagar'),
        ('SCHT','Suchitra Road'),
        ('SRRM','Suraram'),
        ('TRNK','Tarnaka'),
        ('TLPR','Tellapur'),
        ('TMPR','Thimmapur'),
        ('TLCH','Toli Chowki'),
        ('TRMG','Trimulgherry'),
        ('TKGD','Tukkuguda'),
        ('TPRN','Tupran'),
        ('TRKM','Turkayamjal'),
        ('UPGD','Uppaguda'),
        ('UPPL','Uppal'),
        ('UPRP','Upparpally'),
        ('VNST','Vanasthalipuram'),
        ('VTPL','Vattepally'),
        ('VLML','Velimela'),
        ('VNKR','Venkat Reddy Colony'),
        ('VNKP','Venkatapuram'),
        ('VVKN','Vivekananda Nagar'),
        ('WLKT','Walker Town'),
        ('WMRP','West Marredpally'),
        ('WFLD','Whitefields'),
        ('YKTP','Yakhutpura'),
        ('YPRL','Yapral'),
        ('YSFG','Yousufguda'),
        ('ZHRB','Zahirabad'),
)


apt_stat=(
    ('ead','Lead'),
    ('cted','Contacted'),
    ('Not Ccted','Not Contacted'),
    ('Meg Followup','Meeting Followup'),
    ('Aggnt Submitted','Aggrement Submitted'),
    ('Aggrent Followup','Aggrement Followup'),
    ('Agnt Signed','Aggrement Signed'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    photo = models.FileField(null=True, blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class Emp(models.Model):

    emp = (
        ('Permanent','Permanent'),('Contactor','Contractor'),
    )
    dept = (
        ('AD Posting','AD Posting'),('ADMIN','ADMIN'),
    )
    emp_name = models.CharField(max_length=30, unique=True,)
    emp_type = models.CharField(max_length=10, choices=emp, default='Permanent')
    emp_join_date = models.DateField()
    emp_pic = models.FileField()
    emp_dept = models.CharField(max_length=20,choices=dept, default='ADMIN')
    emp_blood_group = models.CharField(max_length=5,default='', null=True, blank=True)
    emp_designation = models.CharField(max_length=20,default='', null=True, blank=True)
    emp_dob = models.DateField(default='', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('aptdata:empdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.emp_name

class aptinfo(models.Model):
    apt_code = models.CharField(max_length=20,unique=True)
    aptname = models.CharField(max_length=50)
    area = models.CharField(max_length=100, choices=area_codes)
    address = models.TextField(max_length=300, help_text="Please enter the address")
    landmark = models.CharField(max_length=50)
    apt_pic = models.FileField()
    record_owner = models.CharField(max_length=30)
    sales_remainder_date = models.DateField()
    sales_remainder_time = models.TimeField()
    apt_status = models.CharField(max_length=20, choices=apt_stat)
    no_of_flats = models.IntegerField(null=True, blank=True, default=1,validators=[MaxValueValidator(10000), MinValueValidator(1)])
    apt_categoery = models.CharField(max_length=3)
    no_of_blocks = models.IntegerField(null=True, blank=True, default=1,validators=[MaxValueValidator(10000), MinValueValidator(1)])
    primary_contact = models.CharField(max_length=30)
    primary_contact_number = models.BigIntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(9999999999),MinValueValidator(7000000000)])
    secondary_contact = models.CharField(max_length=30,default='', null=True, blank=True)
    secondary_contact_number = models.BigIntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(9999999999),MinValueValidator(7000000000)])
    watchman_name = models.CharField(max_length=30,default='', null=True, blank=True)
    watchman_contact = models.BigIntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(9999999999), MinValueValidator(7000000000)])
    total_board_count = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    distance_from_mainroad_in_km = models.FloatField(default='', null=True, blank=True)
    aggrement_sign_date = models.DateField(default='', null=True, blank=True)
    aggrement_start_date = models.DateField(default='', null=True, blank=True)
    aggrement_end_date = models.DateField(default='', null=True, blank=True)
    bank_name = models.CharField(max_length=30, default='', null=True, blank=True)
    bank_account_name = models.CharField(max_length=30, default='', null=True, blank=True)
    account_number = models.CharField(max_length=30, default='', null=True, blank=True)
    ifsc_code = models.CharField(max_length=10, default='', null=True, blank=True)
    cost_of_A2 = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(10000), MinValueValidator(0)])
    cost_of_A3 = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(10000), MinValueValidator(0)])
    cost_of_2X4 = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(10000), MinValueValidator(0)])
    cost_of_3X6 = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(10000), MinValueValidator(0)])
    # the below field requires validation for max value. it should be compared with number of flats
    owner_flats = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    rented_flats = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    total_male_count = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    total_female_count = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_5_15_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_16_26_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_27_50_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_above_50_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_5_15_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_16_26_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_27_50_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_above_50_years = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    families_with_cars = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    num_of_families_participate_activity = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    people_into_industry_count = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_software = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_civil = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_business = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_telecom = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_construction = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_sales = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_education = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_manufacturing = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_media = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    male_household = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_software = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_civil = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_business = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_telecom = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_construction = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_sales = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_education = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_manufacturing = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_media = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    female_household = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])
    avg_maintenance_cost_per_house = models.IntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(1000), MinValueValidator(0)])


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:

            self.apt_code = self.aptname.replace(" ", "")[:4] + '_' + self.area
            self.apt_code = str.upper(str(self.apt_code))
            code_list = aptinfo.objects.filter(apt_code__startswith=self.apt_code).values_list('apt_code',flat=True)
            code_num=0
            if code_list :
                max_code = max(code_list)
            else:
                max_code = self.apt_code
            if max_code[-1:].isdigit():
                code_num = re.match('.*?([0-9]+)$',max_code).group(1)
            if code_num == 0:
                code_num = 1
            else:
                code_num=int(code_num)+1

            if self.no_of_flats < 15:
                self.apt_categoery = 'a'
            else:# self.no_of_flats < 20:
                self.apt_categoery = 'b'
            self.apt_code=self.apt_code+str(code_num)

        super(aptinfo, self).save()


    def get_absolute_url(self):
        return reverse('aptdata:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.apt_code

class aptboards(models.Model):
    board_stat = (
        ('Occupied','Occupied'),('Reserved','Reserved'),('Vacant','Vacant'),
    )
    board_loc = (
        ('ENTrance','Entrance'),('EXIt','Exit'),('LIFt','Lift'),('COMmon Area','Common Area'),
    )
    board_typ = (
        ('Permanent','Permanent'),('Extra Board','Extra Board'),
    )
    board_siz = (
        ('A2','A2'),('A3','A3'),('2X4','2X4'),('3X6','3X6'),
    )
    apt_code = models.ForeignKey(aptinfo, on_delete=models.CASCADE)#, to_field='apt_code')
    board_location = models.CharField(max_length=15,choices = board_loc)
    block_name = models.CharField(max_length=30, null=True, blank=True, default=None)
    board_type = models.CharField(max_length=15, choices=board_typ, default='Permanent')
    board_size = models.CharField(max_length=5, choices=board_siz, default='A3')
    board_code=models.CharField(max_length=30, unique=True)
    board_status=models.CharField(max_length=15, choices=board_stat,default='Vacant')
    board_pic = models.FileField()
    def save(self, force_insert=True, force_update=False, using=None, update_fields=None):

        aptcode = aptinfo.objects.get(pk=self.apt_code_id)
        #self.apt_code = self.apt_code_id

        locd = self.board_location[:3]
        #locd = self.get_board_location_display()[:3]
        if not self.id:
            #self.apt_code=self.apt_code_id
            #self.apt_code = aptinfo.objects.filter(pk=self.apt_code_id).values_list('id')
            self.block_name = str.upper(str(self.block_name))
            self.board_code = str(aptcode)+'_'+str(self.block_name)+'_'+str(locd)
            code_list = aptboards.objects.filter(board_code__startswith=self.board_code).values_list('board_code',flat=True)
            code_num=0
            if code_list :
                max_code = max(code_list)
            else:
                max_code = self.board_code
            if max_code[-1:].isdigit():
                code_num = re.match('.*?([0-9]+)$',max_code).group(1)
            if code_num == 0:
                code_num = 1
            else:
                code_num=int(code_num)+1

            self.board_code=self.board_code+str(code_num)+'['+str(self.board_type)[:1]+']'

        super(aptboards, self).save()

    def get_absolute_url(self):
            return reverse('aptdata:boardlist', kwargs={'pk': self.apt_code_id})
    def __str__(self):
        return self.board_code

#    def __str__(self):
#        return str(self.board_code)

#need to create another table for board calander

class board_calander(models.Model):

    board_code = models.ForeignKey(aptboards, on_delete=models.CASCADE,to_field='board_code')
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()

class aptactivity(models.Model):
    stat_value = (
                ('Assigned','Assigned'),
                ('In Progress','In Progress'),
                ('Completed','Completed'),
                )
    act = (
        ('PostingAdd','Posting Add'),
        ('VisitingPremisis','Visiting Premisis'),
        ('ExtraBoard','Extra Board'),
    )
    emp_name = models.ForeignKey(Emp, on_delete=models.CASCADE)
    apt_code=models.ForeignKey(aptinfo, on_delete=models.CASCADE)
    proposed_date_of_activity = models.DateField()
    actual_date_of_activity = models.DateField(default='', null=True, blank=True)
    activity=models.CharField(max_length=100, choices=act)
    ad_location = models.ForeignKey(aptboards, on_delete=models.CASCADE,default='', null=True, blank=True)
    activity_pic=models.FileField()
    activity_done_by=models.CharField(max_length=30)
    activity_details=models.TextField(max_length=500)
    status = models.CharField(max_length=30, choices=stat_value)
    """
        Here the company details and campaign details to be incorporated.
        """
    def get_absolute_url(self):
            return reverse('aptdata:activitylist', kwargs={'pk': self.apt_code_id})

class advertiser_details(models.Model):

    client_status = (
        ('Lead', 'Lead'),
        ('Contacted', 'Contacted'),
        ('Not Contacted', 'Not Contacted'),
        ('Meeting Followup', 'Meeting Followup'),
        ('Proposal Accepted', 'Proposal Accepted'),
        ('Proposal Followup', 'Proposal Followup'),
    )

    client_name = models.CharField(max_length=30, unique=True)
    contact_person = models.CharField(max_length=30)
    contact_number = models.BigIntegerField(default='', null=True, blank=True,validators=[MaxValueValidator(9999999999),MinValueValidator(7000000000)])
    contact_email = models.EmailField(max_length=50)
    preferred_date = models.DateField()
    preferred_time =models.TimeField()
    status = models.CharField(max_length=30, choices=client_status)

    def get_absolute_url(self):
        return reverse('aptdata:advtdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.client_name

class client_categoery(models.Model):

    prod_cat = (
        ('Telecom','Telecom'),('FMCG','FMCG'),
        ('Electricals','Electricals'),
        ('Electronics','Electronics'),
        ('Furniture','Furniture'),
        ('Interiors','Interiors'),
        ('Movies','Movies'),
        ('Automobile','Automobile'),
        ('Educational Institute','Educational Institute'),
        ('Medical','Medical'),
        ('Sports','Sports'),
    )

    client_name = models.ForeignKey(advertiser_details, on_delete=models.CASCADE)
    product_categoery = models.CharField(max_length=50, choices=prod_cat)
    product_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('aptdata:categoerylist', kwargs={'pk':self.pk})


class campaign_details (models.Model):

    client_name = models.ForeignKey(advertiser_details, on_delete=models.CASCADE)
    product_name =models.ForeignKey(client_categoery, on_delete=models.CASCADE)
    campaign_id = models.CharField(max_length=30, unique=True)
    campaign_poster =models.FileField()
    start_date = models.DateField()
    end_date = models.DateField()

    def get_absolute_url(self):
        return reverse('aptdata:categoerylist', kwargs={'pk':self.pk})


class UserProfile(models.Model):
        # This field is required.
        user = models.OneToOneField(User)
        # These fields are optional
        #website = models.URLField(blank=True)
        #picture = models.ImageField(upload_to='imgs', blank=True)

        def __unicode__(self):
                return self.user.username



class apt_deals(models.Model):

    """duration = (
        ('7','7'),('15','15'),('30','30'),
    )"""

    apt_code = models.ForeignKey(aptinfo, on_delete=models.CASCADE)#, to_field='apt_code')
    board_code = models.ForeignKey(aptboards, on_delete=models.CASCADE)#, to_field='board_code')
    campaign_id = models.ForeignKey(campaign_details, on_delete=models.CASCADE)#, to_field='campaign_id')
    #deal_duration = models.IntegerField(choices=duration)
    deal_start_date = models.DateField()
    deal_end_date = models.DateField()
    #estimated_cost = models.IntegerField()
    final_cost = models.IntegerField(null=True, blank=True, default=1,validators=[MaxValueValidator(10000), MinValueValidator(1)])


    """
        there should be 2 triggers here.
        1. after insert into this table for every board code, a corresponding row should be inserted into apt activity table.
        2. after insert into this table for every board code, it should verify board availability in board calander and if
            available then it should block the calanderby making an entry into that table.
    """


    """
    need to generate a report for knowing the proposed cost report. may be an email can be helpful.

    """