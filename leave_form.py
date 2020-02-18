frm = list(map(int, input('leave apply from: ').split("-")))
to = list(map(int, input('to: ').split("-")))
leave_days = [i for i in range(frm[2], to[2] + 1)]
week_offs = ['2020-2-1','2020-2-2','2020-2-8','2020-2-9','2020-2-15','2020-2-16','2020-2-22','2020-2-23','2020-2-29','2020-2-13','2020-2-14','2020-2-15']
applied_leaves = ['2020-2-7','2020-2-21','2020-2-12']
week_offs2 = []
applied_leaves2 = []
total_leave = 0
for date in week_offs:
    spl = date.split('-')
    week_offs2.append(int(spl[2]))
for app in applied_leaves:
    sp = app.split('-')
    applied_leaves2.append(int(sp[2]))

for i in applied_leaves2:
    if (i+1 in week_offs2) and (int(frm[2])-1 in week_offs2):
        l = list(*range(i,frm[],1)))
        total_leave +=




print(total_leave)









