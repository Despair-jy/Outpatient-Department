# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cost2017(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_2017'


class Cost2018(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_2018'


class Doc2017(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    doc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_2017'


class Doc2018(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    doc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_2018'


class OrgName2017(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_name_2017'


class OrgName2018(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_name_2018'


class OrgName2019(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_name_2019'


class Section(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'


class SectionYear(models.Model):
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section_year'


class ChronicDiseases(models.Model):
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Chronic_diseases'


class DiseaseYear(models.Model):
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.CharField(max_length=255,blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_year'


class HospitalDisease(models.Model):
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital_disease'


class Test2019(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    outpatient_num = models.CharField(max_length=255, blank=True, null=True)
    other_card_code = models.CharField(max_length=255, blank=True, null=True)
    clinic_emergency_mark_code = models.CharField(max_length=255, blank=True, null=True)
    falg_first_visit = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_code = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_all_cost = models.CharField(max_length=255, blank=True, null=True)
    org_code = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_code = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_doc_id_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_date = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_2019'


class Test2020(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    outpatient_num = models.CharField(max_length=255, blank=True, null=True)
    other_card_code = models.CharField(max_length=255, blank=True, null=True)
    clinic_emergency_mark_code = models.CharField(max_length=255, blank=True, null=True)
    falg_first_visit = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_code = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_all_cost = models.CharField(max_length=255, blank=True, null=True)
    org_code = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_code = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_doc_id_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_date = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_2020'


class Train2017(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    outpatient_num = models.CharField(max_length=255, blank=True, null=True)
    other_card_code = models.CharField(max_length=255, blank=True, null=True)
    clinic_emergency_mark_code = models.CharField(max_length=255, blank=True, null=True)
    falg_first_visit = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_code = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_all_cost = models.CharField(max_length=255, blank=True, null=True)
    org_code = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_code = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_doc_id_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_date = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_2017'


class Train2018(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    outpatient_num = models.CharField(max_length=255, blank=True, null=True)
    other_card_code = models.CharField(max_length=255, blank=True, null=True)
    clinic_emergency_mark_code = models.CharField(max_length=255, blank=True, null=True)
    falg_first_visit = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_code = models.CharField(max_length=255, blank=True, null=True)
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_all_cost = models.CharField(max_length=255, blank=True, null=True)
    org_code = models.CharField(max_length=255, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_code = models.CharField(max_length=255, blank=True, null=True)
    treatment_section_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_doc_id_name = models.CharField(max_length=255, blank=True, null=True)
    treatment_date = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_2018'

class DiseaseYear1(models.Model):
    admin_illness_name = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_year1'

class CostTotal2020(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_total2020'