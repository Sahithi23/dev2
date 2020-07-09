from django.db import models

# Create your models here.

class Doctor_Master(models.Model):
    UID = models.CharField(max_length=15, null=True, unique=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    doctor_status = models.CharField(max_length=20, null=True, default='Active')
    designation = models.CharField(max_length=50, null=True)
    contract_details = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=50, null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Doctor_Contract(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    contract_date = models.DateTimeField(blank=True, null=True)
    percentage_flag = models.CharField(max_length=10, null=True, default='InActive')
    rate_flag = models.CharField(max_length=10, null=True, default='InActive')
    multi_rate_flag = models.CharField(max_length=10, null=True, default='InActive')
    percentage_rate = models.DecimalField(max_digits=25, decimal_places=5, default="0", null=True)
    hourly_rate = models.DecimalField(max_digits=25, decimal_places=5, default="0", null=True)
    superannuation_rate = models.CharField(max_length=10, null=True)
    superannuation_flag = models.CharField(max_length=10, null=True, default='InActive')
    contract_status = models.CharField(max_length=10, null=True, default='Active')
    gst_rate = models.DecimalField(max_digits=10, decimal_places=5, default="10", null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)
    updated_by = models.CharField(max_length=20, null=True)


    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Multi_Rates(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    multi_rates_date = models.DateTimeField(blank=True, null=True)
    multi_rate_status = models.CharField(max_length=10, null=True, default='InActive')
    from_time = models.DateTimeField(blank=True, null=True)
    to_time = models.DateTimeField(blank=True, null=True)
    multi_rate = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.__str__()


class Commencement_Period(models.Model):
    commencement_period_id = models.IntegerField(null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Txn_Report(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    commencement_period = models.ForeignKey(Commencement_Period, db_column='commencement_period_id', on_delete=models.SET_NULL, null=True)
    txn_date = models.DateTimeField(blank=True, null=True)
    txn_amount = models.DecimalField(max_digits=15, decimal_places=5, default="0", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Payment_Report(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    commencement_period = models.ForeignKey(Commencement_Period, db_column='commencement_period_id', on_delete=models.SET_NULL, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=5, default="0", null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Sessionsdata_Raw(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    work_date = models.DateTimeField(blank=True, null=True)
    time_of_day = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()

class Sessionsdata_Updated(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    sessions_status = models.CharField(max_length=10, null=True, default='InActive')
    work_date = models.DateTimeField(blank=True, null=True)
    time_of_day = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()

# OPERATOR = (
#     ('1', 'Addition'),
#     ('2', 'Subtraction')
# )

class Special_Instructions(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    specialinstruction_date = models.DateTimeField(blank=True, null=True)
    specialinstruction_status = models.CharField(max_length=10, null=True, default='InActive')
    decription = models.CharField(max_length=20, blank=True, null=True)
    specialinstruction_operator = models.CharField(max_length=10, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5, default="0", null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Daily_Calculation(models.Model):
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    # commencement = models.ForeignKey(commencement_period, related_name='commence', on_delete=models.CASCADE, null=True)
    commencement_period = models.ForeignKey(Commencement_Period, db_column='commencement_period_id', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(blank=True, null=True)
    txn_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    payment_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    gross_total = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    percentage = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    hour_rate = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    No_of_hours = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    percent_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    hourly_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    specialinstruction_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    # gst_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    superannuation_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()

class Wage_Calculation(models.Model):
    # doctor = models.ForeignKey(Doctor_Master, related_name='doctor', on_delete=models.CASCADE, null=True)
    # commencement = models.ForeignKey(commencement_period, related_name='commence', on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor_Master, db_column='UID', on_delete=models.SET_NULL, null=True)
    commencement_period = models.ForeignKey(Commencement_Period, db_column='commencement_period_id', on_delete=models.SET_NULL, null=True)
    gross_pay = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    hourly_pay = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    service_pay = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    min_pay = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    super_annuation = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    special_instruction_amount = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    gst_amount = models.DecimalField(max_digits=30, decimal_places=5, default="0", null=True)
    net_pay = models.DecimalField(max_digits=20, decimal_places=5, default='0', null=True)
    remarks = models.TextField(max_length=100, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()


class Status_Check(models.Model):
    contract_flag = models.CharField(max_length=10, null=True, default='Inactive')
    rates_flag = models.CharField(max_length=10, null=True, default='Inactive')
    hours_flag = models.CharField(max_length=10, null=True, default='Inactive')
    superannuation_flag = models.CharField(max_length=10, null=True, default='Inactive')
    special_instructions_flag = models.CharField(max_length=10, null=True, default='Inactive')
    daily_wage_flag = models.CharField(max_length=10, null=True, default='Inactive')

    # def __str__(self):
    #     return self.code

    def __unicode__(self):
        return self.__str__()