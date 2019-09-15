from django.db import models


# Create your models here.


# class Test(models.Model):
#     # 自增长 默认int
#     Auto = models.AutoField(primary_key=True)
#     BigAuto = models.BigAutoField()
#
#     # 二进制
#     Binary = models.BinaryField()
#
#     # 布尔
#     Boolean = models.BooleanField()
#     NullBoolean = models.NullBooleanField()
#
#     # 整型
#     PositiveSmallInteger = models.PositiveSmallIntegerField()  # 5字节
#     SmallInteger = models.SmallIntegerField()  # 6字节
#     PositiveInteger = models.PositiveIntegerField()  # 10字节
#     Integer = models.IntegerField()  # 11字节
#     BigInteger = models.BigIntegerField()  # 20字节
#
#     # 字符串
#     Char = models.CharField()  # varchar
#     Text = models.TextField()  # longtext
#
#     # 时间日期
#     Date = models.DateField()
#     DateTime = models.DateTimeField()
#     Duration = models.DurationField()  # int python timedelta实现
#
#     # 浮点型
#     Float = models.FloatField()
#     Decimal = models.DecimalField()
#
#     # 其他
#     Email = models.EmailField()  # 邮箱
#     Image = models.ImageField()
#     File = models.FileField()
#     FilePath = models.FilePathField()
#     URL = models.URLField()
#     UUID = models.UUIDField()
#     GenericIPAddress = models.GenericIPAddressField()
#

class AddressInfo(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    # note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name="自关联", on_delete=models.SET_NULL)

    def __str__(self):
        return self.address

    class Meta:
        # db_table = "address"  # 自定义表名
        ordering = ["pid_id"]  # 指定排序字段
        verbose_name = "地址"  # 单数
        verbose_name_plural = verbose_name  # 复数
        # abstract = True  # 设置为基类
        # permissions = (("定义好的权限", "权限说明"),)
        # managed = False  # 按照Django默认方式管理数据表
        # unique_together = ("address", "note")  # 联合唯一键，单元组或多元组
        # app_label = "ormdemo"  # 定义模型类属于哪个应用
        # db_tablespace = "" # 定义数据库表空间


"""
讲师 - 助教 一对一
讲师 - 课程表 一对多
课程表 - 学生 多对多
"""


class Teacher(models.Model):
    """讲师信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    introduction = models.TextField(default="这位同学很懒，木有签名的说~", verbose_name="简介")
    fans = models.PositiveIntegerField(default=0, verbose_name="粉丝数")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    type = models.CharField(choices=((0, "其他"), (1, "实战课"), (2, "免费课")), max_length=1, default=0, verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    # 删除级联
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE, verbose_name="讲师")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "课程信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"


class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="学生姓名")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((0, "保密"), (1, "男"), (2, "女")), max_length=1, default=0, verbose_name="性别")
    study_time = models.PositiveIntegerField(default=0, verbose_name="学习时长(h)")
    course = models.ManyToManyField(Course, verbose_name="课程")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name
        get_latest_by = "created_at"

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    hobby = models.CharField(max_length=10, null=True, blank=True, verbose_name="爱好")
    # 删除置空
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="讲师")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "助教信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class GroupConcat(models.Aggregate):
    """自定义聚合函数"""
    function = "GROUP_CONCAT"
    template = "%(function)s%(distinct)s%(expressions)s%(ordering)s%(separator)s"

    def __init__(self, expression, distinct=False, ordering=None, separator=",", **extra):
        super(GroupConcat, self).__init__(
            expression,
            distinct="DISTINCT" if distinct else "",
            ordering=" ORDER BY %s" % ordering if ordering is not None else "",
            separator=' SEPARATOR "%s"' % separator,
            output_field=models.CharField(), **extra
        )

