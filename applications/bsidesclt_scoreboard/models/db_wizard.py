### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_challenges',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_description', type='text',
          label=T('Description')),
    Field('f_solution', type='string',
          label=T('Solution')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_challenges_archive',db.t_challenges,Field('current_record','reference t_challenges',readable=False,writable=False))

########################################
db.define_table('t_submissions',
    Field('f_solution', type='string',
          label=T('Solution')),
    auth.signature,
    format='%(f_solution)s',
    migrate=settings.migrate)

db.define_table('t_submissions_archive',db.t_submissions,Field('current_record','reference t_submissions',readable=False,writable=False))
