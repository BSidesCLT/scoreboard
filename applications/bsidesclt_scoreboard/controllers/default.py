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
@auth.requires_membership('admins')
def challenges_manage():
    form = SQLFORM.smartgrid(db.t_challenges,onupdate=auth.archive)
    return locals()

def challenges_view():
    record = db.t_challenges(request.args(0)) or redirect(URL('error'))
    form=crud.read(db.t_challenges,record)
    return dict(form=form)

@auth.requires_login()
def submissions_manage():
    form = SQLFORM.smartgrid(db.t_submissions,onupdate=auth.archive)
    return locals()

