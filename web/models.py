from django.db import models

# Create your models here.

class recordOfInvention(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    name_of_invention = models.TextField()
    problem_it_solves = models.TextField()

    def __str__(self):
        return str(self.teamId)

class Inventor(models.Model):
    inventor = models.TextField()
    schoolnamegrade = models.TextField()
    sig = models.TextField()
    date = models.TextField()
    
class statementOfOriginality(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    
    inventors=models.ManyToManyField(Inventor, related_name='statement_of_originality')

    def __str__(self):
        return str(self.teamId)


class stepOne(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    identify_problems = models.TextField()

    def __str__(self):
        return str(self.teamId)
    
class Problem(models.Model):
    problem=models.TextField()
    name1=models.TextField()
    name2=models.TextField()
    name3=models.TextField()
    name4=models.TextField()
    age1=models.TextField()
    age2=models.TextField()
    age3=models.TextField()
    age4=models.TextField()
    comment1=models.TextField()
    comment2=models.TextField()
    comment3=models.TextField()
    comment4=models.TextField()


class stepTwo(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    problems=models.ManyToManyField(Problem, related_name='step_two')

    problem_title = models.TextField()
    problem_description = models.TextField()
    describe_problem = models.TextField()
    specific_solution = models.TextField()

    def __str__(self):
        return str(self.teamId)


class stepThree(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    factors = models.TextField()
    ways_to_solve = models.TextField()
    research = models.TextField()
    difference = models.TextField()

    def __str__(self):
        return str(self.teamId)

class Issue(models.Model):
    expert=models.TextField()
    credentials=models.TextField()
    identified=models.TextField()
    problemface=models.TextField()
class stepFour(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    blueprint = models.ImageField(null=True, blank=True,upload_to='images/')
    teacher_name = models.TextField()
    teacher_sign = models.TextField()
    date = models.TextField()
    
    issues=models.ManyToManyField(Issue,related_name='step_four')

    sol_design_problem = models.TextField()
    green_sol = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.blueprint.url
        except:
            url = ""
        return url
    
    def __str__(self):
        return str(self.teamId)


class stepFive(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    materials = models.TextField()
    findings = models.TextField()
    credit = models.TextField()

    def __str__(self):
        return str(self.teamId)


class stepSix(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    notes = models.TextField()
    prototype_pic = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.prototype_pic.url
            print(url)
        except:
            url = ""
            print(url)
        return url
    
    def __str__(self):
        return str(self.teamId)


class stepSeven(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    testing = models.TextField()
    positive = models.TextField()
    negative = models.TextField()

    def __str__(self):
        return str(self.teamId)


class stepEight(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    nameinvention = models.TextField()
    benefits = models.TextField()
    price = models.TextField()
    buy = models.TextField()
    customer_age = models.TextField()
    customer_gender = models.TextField()
    customer_education = models.TextField()
    customer_house = models.TextField()
    customer_marital = models.TextField()
    other_notes = models.TextField()

    def __str__(self):
        return str(self.teamId)


class surveyLogbook(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    things_enjoyed = models.TextField()
    thanking = models.TextField()
    difficulty = models.TextField()
    future = models.TextField()

    def __str__(self):
        return str(self.teamId)

class Note(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    
    note_title= models.TextField()
    note_desc= models.TextField()

    def __str__(self):
        return str(self.teamId)
