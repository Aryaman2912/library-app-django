from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    """ Model representing a book genre. """
    name = models.CharField(max_length=200,help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        """ String to represent the Model object. """
        return self.name

class Language(models.Model):
    """Model representing the language of the book."""
    name= models.CharField(max_length=200,help_text='Language in which the book is written')

    def __str__(self):
        """String to represent the Model object."""
        return self.name

class Book(models.Model):
    """ Model representing a book(but not a specific copy)."""

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13,help_text='13 character <a href = "https://www.isbn-international.org/content/what-isbn">ISBN Number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language',on_delete = models.SET_NULL,null=True)

    def __str__(self):
        """ String to represent the Model object. """
        return self.title

    def get_absolute_url(self):
        """Returns the URL for a detail record for this book. """
        return reverse('book-detail',args=[str(self.id)])

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

class BookInstance(models.Model):
    """Model representing a specific copy of a book(i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique id for this particular copy of the book')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',

    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    """Model representing an author. """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('died',null=True,blank=True)

    class Meta:
        ordering = ['first_name','last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author's instance."""
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object. """
        return f'{self.first_name} {self.last_name}'




