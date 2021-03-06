# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 06:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='advertiser_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30, unique=True)),
                ('contact_person', models.CharField(max_length=30)),
                ('contact_number', models.BigIntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(7000000000)])),
                ('contact_email', models.EmailField(max_length=50)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('status', models.CharField(choices=[('Lead', 'Lead'), ('Contacted', 'Contacted'), ('Not Contacted', 'Not Contacted'), ('Meeting Followup', 'Meeting Followup'), ('Proposal Accepted', 'Proposal Accepted'), ('Proposal Followup', 'Proposal Followup')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='apt_deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_start_date', models.DateField()),
                ('deal_end_date', models.DateField()),
                ('final_cost', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='aptactivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_date_of_activity', models.DateField()),
                ('actual_date_of_activity', models.DateField(blank=True, default='', null=True)),
                ('activity', models.CharField(choices=[('PostingAdd', 'Posting Add'), ('VisitingPremisis', 'Visiting Premisis'), ('ExtraBoard', 'Extra Board')], max_length=100)),
                ('activity_pic', models.FileField(upload_to=b'')),
                ('activity_done_by', models.CharField(max_length=30)),
                ('activity_details', models.TextField(max_length=500)),
                ('status', models.CharField(choices=[('Assigned', 'Assigned'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='aptboards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_location', models.CharField(choices=[('ENTrance', 'Entrance'), ('EXIt', 'Exit'), ('LIFt', 'Lift'), ('COMmon Area', 'Common Area')], max_length=15)),
                ('block_name', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('board_type', models.CharField(choices=[('Permanent', 'Permanent'), ('Extra Board', 'Extra Board')], default='Permanent', max_length=15)),
                ('board_size', models.CharField(choices=[('A2', 'A2'), ('A3', 'A3'), ('2X4', '2X4'), ('3X6', '3X6')], default='A3', max_length=5)),
                ('board_code', models.CharField(max_length=30, unique=True)),
                ('board_status', models.CharField(choices=[('Occupied', 'Occupied'), ('Reserved', 'Reserved'), ('Vacant', 'Vacant')], default='Vacant', max_length=15)),
                ('board_pic', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='aptinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt_code', models.CharField(max_length=20, unique=True)),
                ('aptname', models.CharField(max_length=50)),
                ('area', models.CharField(choices=[('ASRN', 'A S Rao Nagar'), ('ABDP', 'Abdullapurmet'), ('ABID', 'Abids'), ('ADRS', 'Adarsh Nagar'), ('ADBT', 'Adibatla'), ('ADKM', 'Adikmet'), ('AFZG', 'Afzal Gunj'), ('AMSG', 'Almasguda'), ('ALWL', 'Alwal'), ('AMBR', 'Amberpet'), ('AMNP', 'Ameenpur'), ('AMRP', 'Ameerpet'), ('ANBG', 'Anandbagh'), ('APPJ', 'Appa Junction'), ('ATPU', 'Attapur'), ('BCHP', 'Bachupally'), ('BDNG', 'Badangpet'), ('BDPL', 'Bahadurpally'), ('BDPR', 'Bahadurpura'), ('BIRG', 'Bairagiguda'), ('BLNG', 'Bala Nagar'), ('BLPR', 'Balapur'), ('BNDG', 'Bandlaguda'), ('BNJH', 'Banjara Hills'), ('BSBG', 'Basheerbagh'), ('BRMG', 'Beeramguda'), ('BGMP', 'Begumpet'), ('BHNR', 'Bhanur'), ('BGRM', 'Bhogaram'), ('BOGD', 'Bhoiguda'), ('BNGR', 'Bhongir'), ('BUNG', 'Bhuvanagiri'), ('BBNG', 'Bibinagar'), ('BNRG', 'BN Reddy Nagar'), ('BDUP', 'Boduppal'), ('BLRM', 'Bolaram'), ('BRBD', 'Borabanda'), ('BWNP', 'Bowenpally'), ('BWRM', 'Bowrampet'), ('BDVL', 'Budvel'), ('BRGL', 'Burgul'), ('CHMP', 'Champapet'), ('CHND', 'Chanda Nagar'), ('CHNG', 'Chandrayanagutta'), ('CHRL', 'Cherlapally'), ('CHVL', 'Chevalla'), ('CKDP', 'Chikkadapally'), ('CHLK', 'Chilkur'), ('CHNT', 'Chintal'), ('CNTK', 'Chintalkunta'), ('CNPG', 'Chintapallyguda'), ('CWDG', 'Chowdhariguda'), ('DMGD', 'Dammaiguda'), ('DSRL', 'Dasarlapally'), ('DYRA', 'Dayara'), ('DOLP', 'Dhoolpet'), ('DSNR', 'Dilsukhnagar'), ('DMLG', 'Domalguda'), ('DLAP', 'Dullapally'), ('DNIG', 'Dundigal'), ('EMAR', 'East Marredpally'), ('ECIL', 'ECIL'), ('EDLG', 'Edulanagulapalle'), ('ERGA', 'Erragadda'), ('FLKN', 'Falaknuma'), ('FLMN', 'Film Nagar'), ('FIND', 'Financial District'), ('GCHB', 'Gachibowli'), ('GGLP', 'Gagillapur'), ('GJLR', 'Gajularamaram'), ('GNDN', 'Gandhi Nagar'), ('GMIS', 'Gandi Maisamma'), ('GNDP', 'Gandipet'), ('GHBZ', 'Ghansi Bazar'), ('GHKS', 'Ghatkesar'), ('GLKN', 'Golkonda'), ('GPNP', 'Gopanpally'), ('GDMA', 'Gudimalkapur'), ('GLIC', 'Gulshan-e-Iqbal Colony'), ('GPCP', 'Gundlapochampally'), ('GNRE', 'Gunrock Enclave'), ('GRGD', 'Gurram Guda'), ('HBSG', 'Habsiguda'), ('HFZP', 'Hafeezpet'), ('HKMP', 'Hakimpet'), ('HNMN', 'Hanuman Nagar Colony'), ('HSMT', 'Hasmathpet'), ('HSTN', 'Hastinapuram'), ('HYTN', 'Hayat Nagar'), ('HITC', 'Hi Tech City'), ('HMYT ', 'Himayath Nagar'), ('HUMY', 'Humayun Nagar'), ('HYDN', 'Hyder Nagar'), ('HYDG', 'Hyderguda'), ('IBHP', 'Ibrahimpatnam'), ('INDR', 'Indresham'), ('ISNA', 'Isnapur'), ('JLPL', 'Jalpally'), ('JMBG', 'Jam Bagh'), ('JWHR', 'Jawahar Nagar'), ('JDMT', 'Jeedimetla'), ('JERA', 'Jeera'), ('JUBL', 'Jubilee Hills'), ('KCHG', 'Kachiguda'), ('KKGD', 'Kakaguda'), ('KLSD', 'Kalasiguda'), ('KNCB', 'Kanchan Bagh'), ('KNDK', 'Kandukur'), ('KPRA', 'Kapra'), ('KRKN', 'Karkhana'), ('KRMN', 'Karmanghat'), ('KRWN', 'Karwan'), ('KTDN', 'Katedan'), ('KVDG', 'Kavadiguda'), ('KVRH', 'Kavuri Hills'), ('KZPL', 'Kazipally'), ('KESR', 'Keesara'), ('KRTB', 'Khairatabad'), ('KSMT', 'Kismatpur'), ('KKPT', 'Kokapet'), ('KLUR', 'Kollur'), ('KMPL', 'Kompally'), ('KNDP', 'Kondapur'), ('KNGK', 'Kongara Kalan'), ('KTGD', 'Kothaguda'), ('KTPT', 'Kothapet'), ('KTUR', 'Kothur'), ('KOTI', 'Koti'), ('KWKR', 'Kowkur'), ('KPHB', 'KPHB'), ('KKTP', 'Kukatpally'), ('KSHG', 'Kushaiguda'), ('LKDP', 'Lakdi Ka Pul'), ('LDRZ', 'Lal Darwaza'), ('LLPT', 'Lalapet'), ('LLGD', 'Lallaguda'), ('LNGH', 'Langar Houz'), ('LBNG', 'LB Nagar'), ('LGMP', 'Lingampally'), ('LTKN', 'Lothkunta'), ('MDHP', 'Madhapur'), ('MDRN', 'Madhura Nagar'), ('MDNG', 'Madinaguda'), ('MHSW', 'Maheshwaram'), ('MSRP', 'Maisireddipalle'), ('MJRG', 'Majarguda'), ('MLKP', 'Malakpet'), ('MLKG', 'Malkajgiri'), ('MLMP', 'Mallampet'), ('MLPR', 'Mallapur'), ('MCHR', 'Manchirevula'), ('MNKD', 'Manikonda'), ('MNGD', 'Manneguda'), ('MNSB', 'Mansoorabad'), ('MRTN', 'Maruti Nagar'), ('MSBT', 'Masab Tank'), ('MZDP', 'Mazidpur'), ('MDKR', 'Medak Road'), ('MDCH', 'Medchal'), ('MDPL', 'Medipalli'), ('MERP', 'Meerpet'), ('MHDP', 'Mehadipatnam'), ('MTUG', 'Mettuguda'), ('MYPR', 'Miyapur'), ('MGLP', 'Moghalpura'), ('MINB', 'Moinabad'), ('MKLA', 'Mokila'), ('MSPT', 'Moosapet'), ('MSRB', 'Moosarambagh'), ('MTGP', 'Moti Ganpur'), ('MTIN', 'Moti Nagar'), ('MOLA', 'Moula Ali'), ('MSHB', 'Musheerabad'), ('MTNG', 'Muthangi'), ('MLRG', 'Mylargada'), ('NCRM', 'Nacharam'), ('NDRG', 'Nadergul'), ('NGRM', 'Nagaram'), ('NGSR', 'Nagarjuna Sagar Road'), ('NGLE', 'Nagole'), ('NLAG', 'Nallagandla'), ('NLKT', 'Nallakunta'), ('NMPL', 'Nampally'), ('NNKR', 'Nanakramguda'), ('NNIG', 'Nandigama'), ('NRYG', 'Narayanguda'), ('NRKT', 'Narketpalli'), ('NRSP', 'Narsapur'), ('NRSI', 'Narsingi'), ('NWSK', 'Nawab Saheb Kunta'), ('NLDR ', 'Neeladri Nagar'), ('NRDM', 'Neredmet'), ('NMLK', 'New Malakpet'), ('NMLP', 'New Mallepally'), ('NNLA', 'New Nallakunta'), ('NZMP', 'Nizampet'), ('NZMP ', 'Nizampet Road'), ('NTRN', 'NTR Nagar'), ('OBWN', 'Old Bowenpally'), ('OSMN', 'Osman Nagar'), ('OSSG', 'Osman Sagar Road'), ('PDMR', 'Padma Rao Nagar'), ('PHDS', 'Pahadi Shareef'), ('PTNC', 'Patancheru'), ('PTGP', 'Patighanpur'), ('PRCH', 'Peerancheru'), ('PRZG', 'Peerzadiguda'), ('PCHM', 'Pochampally'), ('PCHR', 'Pocharam'), ('PRGN ', 'Pragathi Nagar'), ('PRSN', 'Prashanth Nagar'), ('PLMA', 'Pulimamidi'), ('PNJG', 'Punjagutta'), ('PPAL', 'Puppalaguda'), ('QTBP', 'Quthbullapur'), ('QTST', 'Qutub Shahi Tombs'), ('RIDG', 'Rai Durg'), ('RIKL', 'Raikal'), ('RAJB', 'Raj Bhavan Road'), ('RJVN', 'Rajeev Nagar'), ('RJDN', 'Rajendra Nagar'), ('RMNG', 'Ram Nagar'), ('RKPM', 'Ramakrishnapuram'), ('RMTP', 'Ramanthapur'), ('RCPM', 'Ramchandra Puram'), ('RMGP', 'Ramgopalpet'), ('RMFC', 'Ramoji Film City'), ('RMPL', 'Rampally'), ('RGNJ', 'Rani Gunj'), ('RSLP', 'Rasoolpura'), ('RNDG', 'Rendlagadda'), ('RDRM', 'Rudraram'), ('SDRD', 'S D Road'), ('SIDB', 'Saidabad'), ('SIFB', 'Saifabad'), ('SNKP', 'Sainikpuri'), ('SLMN', 'Saleem Nagar'), ('SNTN', 'Sanath Nagar'), ('SNGR', 'Sangareddy'), ('SNJR', 'Sanjeeva Reddy Nagar'), ('STNG', 'Santosh Nagar'), ('SRRN', 'Saroor Nagar'), ('SCBD', 'Secunderabad'), ('SLNG', 'Serilingampally'), ('SHDN', 'Shadnagar'), ('SHBD', 'Shahbaad'), ('SHKP', 'Shaikpet'), ('SMRP', 'Shamirpet'), ('SMSB', 'Shamshabad'), ('SKRP', 'Shankarpalli'), ('SHNT', 'Shanthi Nagar'), ('SERG', 'Sheriguda'), ('SDRT', 'Siddhartha Nagar'), ('SNDC', 'Sindhi Colony'), ('STPH', 'Sitaphalmandi'), ('SVRM', 'Sivarampalli'), ('SMJG', 'Somajiguda'), ('SRNC', 'Sri Nagar Colony'), ('SRNG', 'Srinagar Colony'), ('SBSN', 'Subhash Nagar'), ('SCHT', 'Suchitra Road'), ('SRRM', 'Suraram'), ('TRNK', 'Tarnaka'), ('TLPR', 'Tellapur'), ('TMPR', 'Thimmapur'), ('TLCH', 'Toli Chowki'), ('TRMG', 'Trimulgherry'), ('TKGD', 'Tukkuguda'), ('TPRN', 'Tupran'), ('TRKM', 'Turkayamjal'), ('UPGD', 'Uppaguda'), ('UPPL', 'Uppal'), ('UPRP', 'Upparpally'), ('VNST', 'Vanasthalipuram'), ('VTPL', 'Vattepally'), ('VLML', 'Velimela'), ('VNKR', 'Venkat Reddy Colony'), ('VNKP', 'Venkatapuram'), ('VVKN', 'Vivekananda Nagar'), ('WLKT', 'Walker Town'), ('WMRP', 'West Marredpally'), ('WFLD', 'Whitefields'), ('YKTP', 'Yakhutpura'), ('YPRL', 'Yapral'), ('YSFG', 'Yousufguda'), ('ZHRB', 'Zahirabad')], max_length=100)),
                ('address', models.TextField(help_text='Please enter the address', max_length=300)),
                ('landmark', models.CharField(max_length=50)),
                ('apt_pic', models.FileField(upload_to=b'')),
                ('record_owner', models.CharField(max_length=30)),
                ('sales_remainder_date', models.DateField()),
                ('sales_remainder_time', models.TimeField()),
                ('apt_status', models.CharField(choices=[('ead', 'Lead'), ('cted', 'Contacted'), ('Not Ccted', 'Not Contacted'), ('Meg Followup', 'Meeting Followup'), ('Aggnt Submitted', 'Aggrement Submitted'), ('Aggrent Followup', 'Aggrement Followup'), ('Agnt Signed', 'Aggrement Signed')], max_length=20)),
                ('no_of_flats', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
                ('apt_categoery', models.CharField(max_length=3)),
                ('no_of_blocks', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
                ('primary_contact', models.CharField(max_length=30)),
                ('primary_contact_number', models.BigIntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(7000000000)])),
                ('secondary_contact', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('secondary_contact_number', models.BigIntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(7000000000)])),
                ('watchman_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('watchman_contact', models.BigIntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(7000000000)])),
                ('total_board_count', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('distance_from_mainroad_in_km', models.FloatField(blank=True, default='', null=True)),
                ('aggrement_sign_date', models.DateField(blank=True, default='', null=True)),
                ('aggrement_start_date', models.DateField(blank=True, default='', null=True)),
                ('aggrement_end_date', models.DateField(blank=True, default='', null=True)),
                ('bank_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('bank_account_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('account_number', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('ifsc_code', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('cost_of_A2', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('cost_of_A3', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('cost_of_2X4', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('cost_of_3X6', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('owner_flats', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('rented_flats', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('total_male_count', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('total_female_count', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_5_15_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_16_26_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_27_50_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_above_50_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_5_15_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_16_26_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_27_50_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_above_50_years', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('families_with_cars', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('num_of_families_participate_activity', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('people_into_industry_count', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_software', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_civil', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_business', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_telecom', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_construction', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_sales', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_education', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_manufacturing', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_media', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('male_household', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_software', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_civil', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_business', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_telecom', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_construction', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_sales', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_education', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_manufacturing', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_media', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('female_household', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('avg_maintenance_cost_per_house', models.IntegerField(blank=True, default='', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='board_calander',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_start_date', models.DateField()),
                ('booking_end_date', models.DateField()),
                ('board_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptboards', to_field='board_code')),
            ],
        ),
        migrations.CreateModel(
            name='campaign_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_id', models.CharField(max_length=30, unique=True)),
                ('campaign_poster', models.FileField(upload_to=b'')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.advertiser_details')),
            ],
        ),
        migrations.CreateModel(
            name='client_categoery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_categoery', models.CharField(choices=[('Telecom', 'Telecom'), ('FMCG', 'FMCG'), ('Electricals', 'Electricals'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Interiors', 'Interiors'), ('Movies', 'Movies'), ('Automobile', 'Automobile'), ('Educational Institute', 'Educational Institute'), ('Medical', 'Medical'), ('Sports', 'Sports')], max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.advertiser_details')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=30, unique=True)),
                ('emp_type', models.CharField(choices=[('Permanent', 'Permanent'), ('Contactor', 'Contractor')], default='Permanent', max_length=10)),
                ('emp_join_date', models.DateField()),
                ('emp_pic', models.FileField(upload_to=b'')),
                ('emp_dept', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('emp_blood_group', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('emp_designation', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('emp_dob', models.DateField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campaign_details',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.client_categoery'),
        ),
        migrations.AddField(
            model_name='aptboards',
            name='apt_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptinfo'),
        ),
        migrations.AddField(
            model_name='aptactivity',
            name='ad_location',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptboards'),
        ),
        migrations.AddField(
            model_name='aptactivity',
            name='apt_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptinfo'),
        ),
        migrations.AddField(
            model_name='aptactivity',
            name='emp_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.Emp'),
        ),
        migrations.AddField(
            model_name='apt_deals',
            name='apt_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptinfo'),
        ),
        migrations.AddField(
            model_name='apt_deals',
            name='board_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.aptboards'),
        ),
        migrations.AddField(
            model_name='apt_deals',
            name='campaign_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aptdata.campaign_details'),
        ),
    ]
