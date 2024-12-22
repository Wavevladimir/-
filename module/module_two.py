import module_one as m_one
print(type(m_one))
print(dir(m_one))
m_one.print_name('Vova')
from module_one import print_name 