## 📚 Bölüm 2 Hızlı Başvuru: ORM: Gerçek Dünya ile İlişkisel Model Arasındaki Köprü

**Paket/Yöntem**

**Açıklama**

**Kod Örneği**

---

### `django.db.models.Model`

Bir model tanımlayın.

```python
from django.db import models


class MyModel(models.Model):

    field1 = models.CharField(max_length=100)

    field2 = models.IntegerField()
```

---

### `makemigrations/migrate`

Modellere dayalı veritabanı tabloları oluşturun.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### `all()`

Veritabanından `MyModel` modelinin tüm örneklerini getirir.

```python
MyModel.objects.all()
```

---

### `filter()`

Koşulları kullanarak nesneleri filtreleyin.

```python
MyModel.objects.filter(field1="value")
MyModel.objects.filter(field2__gt=5)
```

---

### `get()`

`field1` özniteliğinin değeri "value" olan `MyModel` modelinin veritabanındaki tek bir örneğini getirir.

```python
MyModel.objects.get(field1="value")
```

---

```python
obj = MyModel(field1="value", field2=5)

obj.save()
```

`field1` için "value" ve `field2` için 5 değerleriyle `MyModel` modelinin yeni bir örneğini oluşturur ve ardından bu örneği veritabanına kaydeder.

```python
obj = MyModel(field1="value", field2=5)

obj.save()
```

```python
obj.field1 = "new value"

obj.save()
```

`obj` örneğinin `field1` değerini "new value" olarak günceller ve değişiklikleri veritabanına kaydeder.

```python
obj.field1 = "new value"

obj.save()
```

---

### `delete()`

Bir nesneyi siler.

```python
obj.delete()
```

---

### `obj.related_model`

`obj` örneğiyle ilişkili modeli getirir. İlgili nesnelere erişir (*ForeignKey* veya  *OneToOneField* ).

```python
obj.related_model
```

```python
obj.related_model
```

---

### `obj.model_set.all()`

`obj` örneğiyle ilişkili tüm nesneleri getirir. İlgili nesnelere ters yönden erişir ( *ForeignKey* ).

```python
obj.model_set.all()
```

```python
obj.model_set.all()
```

---

### `field`

İlgili bir modelin alan değerine göre `MyModel` modelinin örnekleri üzerinde bir filtreleme işlemi gerçekleştirir.

```python
MyModel.objects.filter(related_model__field="value")
```

---

### `exact`

`field` özniteliğinin değeri tam olarak "value" olan `MyModel` modelinin örneklerini veritabanından getirir.

```python
MyModel.objects.filter(field__exact="value")
```

---

### `iexact`

`iexact` araması büyük/küçük harf duyarsızdır; yani değerler büyük ya da küçük harf olmasına bakılmaksızın eşleşir ve *case-insensitive* bir eşleşme sağlar.

```python
MyModel.objects.filter(field__iexact="value")
```

---

### `contains`

Değerin alan içinde bir alt dizge ( *substring* ) olup olmadığını denetler.

```python
MyModel.objects.filter(field__contains="value")
```

---

### `startswith`

Bir dizgenin, belirtilen bir dizgenin karakterleriyle başlayıp başlamadığını belirler.

```python
MyModel.objects.filter(field__startswith="value")
```

---

### `endswith`

Bir dizgenin, belirtilen sonekle bitip bitmediğini belirler.

```python
MyModel.objects.filter(field__endswith="value")
```

---

### `in`

Alan değerinin verilen değerler listesinin içinde olup olmadığını denetler.

```python
MyModel.objects.filter(field__in=["value1", "value2"])
```

---

### `gt`

`field` değerinin sayısal olarak 5’ten büyük olup olmadığını denetler.

```python
MyModel.objects.filter(field__gt=5)
```

---

### `lt`

`field` değerinin sayısal olarak 10’dan küçük olup olmadığını denetler.

```python
MyModel.objects.filter(field__lt=10)
```
