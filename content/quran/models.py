from django.db import models

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, blank=False)
    iso_code = models.CharField(max_length=50, blank=False)
    direction = models.IntegerField(blank=False)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=False)
    country = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    alang = models.ForeignKey(Language, related_name='author_language', on_delete=models.CASCADE, blank=True)
    translation_type = models.CharField(max_length=50, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass


class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=False, blank=False)
    english_name = models.CharField(max_length=1000, blank=False)
    arabic_name = models.CharField(max_length=1000, blank=False)
    transliteration = models.CharField(max_length=1000, blank=False)
    total_verses = models.IntegerField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.number) + " - " + str(self.transliteration)

    class Meta:
        pass


class Verse(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(null=False, blank=False)

    vtext = models.CharField(max_length=10000, blank=False)

    chapter = models.ForeignKey(Chapter, related_name='chapter', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE, null=True)
    vlang = models.ForeignKey(Language, related_name='verse_language', on_delete=models.CASCADE, null=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.chapter.number) + ":" + str(self.number) + " - " + str(self.vlang) + " - " + str(self.author)

    class Meta:
        pass

