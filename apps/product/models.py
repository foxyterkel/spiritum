from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)
    sku = models.CharField(max_length=250, editable=False)

    def save(self):
        if not self.id:
            self.sku = making_sku(self.name, Brand)
        super(Brand, self).save()


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    sku = models.CharField(max_length=250, editable=False)

    def save(self):
        if not self.id:
            self.sku = making_sku(self.name, Category)
        super(Category, self).save()


class Product(models.Model):
    name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    sku = models.CharField(max_length=250, editable=False)
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)

    def save(self):
        if not self.id:
            self.sku = making_sku_final(self, Product)
        super(Product, self).save()


def making_sku(name, cl):
    k = 0
    m = 1
    res = name[k]+name[m]
    should_restar = True
    while should_restar:
        should_restar = False
        for i in cl.objects.all():
            done = False
            while not done:
                if res == i.sku:
                    if m < len(name)-1:
                        m += 1
                        res = name[k]+name[m]
                        should_restar = True
                    else:
                        k += 1
                        m = k + 1
                        res = name[k]+name[m]
                        should_restar = True
                else:
                    done = True
    print(res)
    return res


def making_sku_final(self, cl):
    res = self.brand.sku + '-' + self.category.sku + '-'
    k = 1
    should_restar = True
    while should_restar:
        should_restar = False
        for i in cl.objects.all():
            if res+str(k).zfill(6) == i.sku:
                k += 1
                should_restar = True
    res += str(k).zfill(6)
    print(res)
    return res
