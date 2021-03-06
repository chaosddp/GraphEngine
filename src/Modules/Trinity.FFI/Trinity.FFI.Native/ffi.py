# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ffi')).lstrip('.')
        return importlib.import_module(mname)
    _ffi = swig_import_helper()
    del swig_import_helper
elif version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ffi', [dirname(__file__)])
        except ImportError:
            import _ffi
            return _ffi
        if fp is not None:
            try:
                _mod = imp.load_module('_ffi', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ffi = swig_import_helper()
    del swig_import_helper
else:
    import _ffi
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def Init():
    return _ffi.Init()
Init = _ffi.Init
class Cell(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, cell):
        this = _ffi.new_Cell(cell)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    m_cell = _swig_property(_ffi.Cell_m_cell_get, _ffi.Cell_m_cell_set)

    def GetField(self, field):
        return _ffi.Cell_GetField(self, field)

    def SetField(self, field, content):
        return _ffi.Cell_SetField(self, field, content)

    def AppendField(self, field, content):
        return _ffi.Cell_AppendField(self, field, content)

    def RemoveField(self, field):
        return _ffi.Cell_RemoveField(self, field)

    def HasField(self, field):
        return _ffi.Cell_HasField(self, field)

    def GetID(self):
        return _ffi.Cell_GetID(self)

    def SetID(self):
        return _ffi.Cell_SetID(self)
    __swig_destroy__ = _ffi.delete_Cell
    __del__ = lambda self: None

    def GetFieldNames(self):
        return _ffi.Cell_GetFieldNames(self)
Cell_swigregister = _ffi.Cell_swigregister
Cell_swigregister(Cell)
cvar = _ffi.cvar


def LoadCell(cellId):
    return _ffi.LoadCell(cellId)
LoadCell = _ffi.LoadCell

def SaveCell_1(cellId, pcell):
    return _ffi.SaveCell_1(cellId, pcell)
SaveCell_1 = _ffi.SaveCell_1

def SaveCell_2(cellId, pcell, options):
    return _ffi.SaveCell_2(cellId, pcell, options)
SaveCell_2 = _ffi.SaveCell_2

def NewCell_1(cellType):
    return _ffi.NewCell_1(cellType)
NewCell_1 = _ffi.NewCell_1

def NewCell_2(cellId, cellType):
    return _ffi.NewCell_2(cellId, cellType)
NewCell_2 = _ffi.NewCell_2

def NewCell_3(cellType, cellContent):
    return _ffi.NewCell_3(cellType, cellContent)
NewCell_3 = _ffi.NewCell_3


