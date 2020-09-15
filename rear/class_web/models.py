"""
    @author: common
    @describe: 数据库模型文件
    @date: 2020/3/12
"""


from class_web.extensions import db


# 个人账号信息表
class Account(db.Model):
    study_id = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    portrait = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    web_url = db.Column(db.String(255), nullable=False)


# 公告信息表
class Announce(db.Model):
    announce_id = db.Column(db.String(255), primary_key=True, nullable=False)
    time = db.Column(db.String(255), nullable=False)
    headline = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    writer = db.Column(db.String(255), nullable=False)


# 留言表
class Message(db.Model):
    msg_id = db.Column(db.String(255), primary_key=True, nullable=False)
    user = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    like = db.Column(db.Integer, nullable=False, default=0)
    view = db.Column(db.Integer, nullable=False, default=0)


# 评论表
class Discuss(db.Model):
    discuss_id = db.Column(db.String(255), primary_key=True, nullable=False)
    user = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    target_type = db.Column(db.Boolean, nullable=False)
    target_id = db.Column(db.String(255), nullable=False)
    like = db.Column(db.Integer, nullable=False, default=0)