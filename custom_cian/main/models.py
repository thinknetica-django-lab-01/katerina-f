from pytils import translit

from django.db import models


class Realty(models.Model):

    name = models.CharField(verbose_name='Название', max_length=100)
    price = models.IntegerField(verbose_name='Цена')
    space = models.IntegerField(verbose_name='Площадь')
    published_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    description = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField('Tag', related_name="tags")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    saller = models.ForeignKey('Saller', on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='Ссылка', max_length=100, unique=True, editable=False)

    class Meta:
        verbose_name = "Объект недвижимости"
        verbose_name_plural = "Объекты недвижимости"
        ordering = ["-published_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(f"{self.category} {self.name}")
        super(Realty, self).save(*args, **kwargs)


class Saller(models.Model):

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    registered_at = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):

    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Ссылка', max_length=100, unique=True, editable=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(f"category-{self.name}")
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Ссылка', max_length=100, unique=True, editable=False)
    realty_list = models.ManyToManyField(Realty, related_name="realty_list")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(f"tag-{self.name}")
        super(Tag, self).save(*args, **kwargs)