#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'

# =====================================================================
# 将一个类写入文件中
import pickle
# d=dict(name='Bob',get=20,score=88)
# f=open('student.dump','wb')
# pickle.dump(d,f)
# f.close
# =====================================================================
f=open('student.dump','rb')
d=pickle.load(f)
f.close
print(d)
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================
# =====================================================================