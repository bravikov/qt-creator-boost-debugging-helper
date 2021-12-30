# The article "Using Debugging Helpers":
# https://doc.qt.io/qtcreator/creator-debugging-helpers.html

# https://github.com/ruediger/Boost-Pretty-Printer/

try:
    from dumper import *
except ModuleNotFoundError:
    pass


def vector_helper(d, value):
    m_holder = value['m_holder']
    size = m_holder['m_size'].integer()
    d.putItemCount(size)
    if d.isExpanded():
        with Children(d):
            for i in range(size):
                d.putSubItem(f"[{i}]", m_holder['m_start'][i])


def qdump__boost__container__vector(d, value):
    vector_helper(d, value)


def qdump__boost__container__small_vector(d, value):
    vector_helper(d, value)


def qdump__boost__container__static_vector(d, value):
    m_holder = value['m_holder']
    size = m_holder['m_size'].integer()
    d.putItemCount(size)
    d.putArrayData(m_holder['storage']['dummy'].address(), size, value.type[0])


def qdump__boost__container__flat_set(d, value):
    d.putItem(value['m_data']['m_seq'])


def qdump__boost__container__flat_map(d, value):
    d.putItem(value['m_flat_tree']['m_data']['m_seq'])
