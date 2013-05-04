# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def challenges_manage():
    form = SQLFORM.smartgrid(db.t_challenges,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def submissions_manage():
    form = SQLFORM.smartgrid(db.t_submissions,onupdate=auth.archive)
    return locals()

