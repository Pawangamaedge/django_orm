from .models import Musician, Book

mucisian_data = Musician.objects.create(
     first_name = "pawan",
     Last_name = "Dabi",
     instrument = "piano",
     place = "indore",
     charges = 20000
)

book_data = Book.objects.create(
     title = "data analytics handbook",
     author_name = "adam john rutherford",
     isbn_no = 122331213
)
