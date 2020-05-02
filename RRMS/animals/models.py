from django.db import models
from ckeditor.fields import RichTextField

from .choices import Species, Canine, Sex, YorN, Dispostions

class PetStats(models.Model):
    '''
    Base Pet information
    '''
    # Intial Species Information
    rescueId = models.PositiveIntegerField(
        verbose_name='Animal Rescue ID',
        help_text='Enter the Rescue Tag Number. <em>Only Numbers</em>',)

    species = models.CharField(
        max_length=1, 
        verbose_name='Species', 
        help_text='Select the main species of the animal.',
        choices=Species,)

    subspecies = models.CharField(
        max_length=100,
        verbose_name='Subspecies',
        help_text='Select the subspecies of the animal.',
        choices=Canine)

    other = models.CharField(
        max_length=100,
        verbose_name='Other',
        help_text='Enter any other subspecie information.',
        blank=True,
        null=True)

    sex = models.CharField(
        max_length=1,
        verbose_name='Sex',
        help_text='Choose Male or Female.',
        choices=Sex)

    # Colors(Eyes and Coat) along with weight
    coatColor = models.CharField(
        max_length=100,
        verbose_name='Color',
        help_text='Enter the animals color of their coat. If multiple use / to seperate the colors. i.e. Black/Brown/White.',
        blank=True,
        null=True)

    intakeWeight = models.IntegerField(
        verbose_name='Intake Weight',
        help_text='Enter intake weight in US Lbs.',
        blank=True,
        null=True)

    eyecolor = models.CharField(
        max_length=100,
        verbose_name='Eye Color',
        help_text='Enter the color of the animals eyes.',
        blank=True,
        null=True)

    # Estimated Birthdate, Intake Date, and Death Date
    birthdate = models.DateField(
        verbose_name='Birthdate',
        help_text='Enter the animals birthdate or estimated birthdate.',
        blank=True,
        null=True)

    intakeDate = models.DateField(
        verbose_name='Intake Date',
        auto_now_add=True)

    deathDate = models.DateField(
        verbose_name='Deathdate',
        help_text='Enter when the animal passed away.',
        blank=True,
        null=True)

    # Booleans on Several Questions
    shelter = models.CharField(
        max_length=1,
        verbose_name='Came from a Shelter?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')
    
    adopted = models.CharField(
        max_length=1,
        verbose_name='Adopted?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    microchipped = models.CharField(
        max_length=1,
        verbose_name='Is the animal Microchipped?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    name = models.CharField(
        max_length=100,
        verbose_name='Intake Name',
        help_text='Enter the intake name of the animal.')

    class Meta:
        unique_together = ('name', 'rescueId',)
        verbose_name = 'Pet Stats'
        verbose_name_plural = 'Pet Stats'

    def __str__(self):
        return str(self.rescueId) +'-'+ self.name
    
class NameAlias(models.Model):
    petID = models.ForeignKey(
        PetStats,
        on_delete=models.CASCADE,
        verbose_name='Rescue ID')

    name = models.CharField(
        max_length=100,
        verbose_name='Name or Alias',
        help_text='Enter the animals name or alias.')

    dateEntered = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Name or Alias'
        verbose_name_plural = 'Name or Alias'

    def __str__(self):
        return str(self.petID.rescueId) +'-'+ self.petID.name +'('+ self.name +')'

class IntakeStory(models.Model):
    petID = models.ForeignKey(
        PetStats,
        on_delete=models.CASCADE,
        verbose_name='Rescue ID')

    story = RichTextField(
        verbose_name='Intake Story',
        help_text='Enter my story.')

    dateEntered = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Intake Story'
        verbose_name_plural = 'Intake Stories'

    def __str__(self):
        return str(self.petID.rescueId) +'-'+ self.petID.name

class BehavorialHealthIssues(models.Model):

    dateEntered = models.DateField(auto_now_add=True)
    petID = models.ForeignKey(
        PetStats,
        on_delete=models.CASCADE,
        verbose_name='Rescue ID')

    foodIssues = models.CharField(
        max_length=1,
        verbose_name='Food Issues?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    spayedNeutered = models.CharField(
        max_length=1,
        verbose_name='Spayed or Neutured?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    handicapped = models.CharField(
        max_length=1,
        verbose_name='Handicapped?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    adoptable = models.CharField(
        max_length=1,
        verbose_name='Adoptable?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    aggressive = models.CharField(
        max_length=1,
        verbose_name='Aggressive?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithKidsSmall = models.CharField(
        max_length=1,
        verbose_name='Good With Small Kids?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithKidsLarge = models.CharField(
        max_length=1,
        verbose_name='Good With Large Kids?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithMen = models.CharField(
        max_length=1,
        verbose_name='Good With Men?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithWomen = models.CharField(
        max_length=1,
        verbose_name='Good With Women?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithCats = models.CharField(
        max_length=1,
        verbose_name='Good With Cats?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    goodwithDogs = models.CharField(
        max_length=1,
        verbose_name='Good With Dogs?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    preydrive = models.CharField(
        max_length=1,
        verbose_name='Prey Drive?',
        help_text='Choose Yes or No.',
        choices=YorN,
        default='N')

    dispostion = models.IntegerField(
        verbose_name='Dispostion',
        help_text='Select the dispostion that best suits the animal.',
        choices=Dispostions)

    notes = RichTextField(
        verbose_name='Notes',
        help_text='Enter any notes on the animal.')

    healthBio = RichTextField(
        verbose_name='Health Bio',
        help_text='Enter any notes on the health of the animal.')


    class Meta:
        verbose_name = 'Health & Behavioral'
        verbose_name_plural = 'Health & Behavioral'

    def __str__(self):
        return str(self.petID.rescueId) +'-'+ self.petID.name


