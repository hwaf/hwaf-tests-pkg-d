# -*- python -*-

import waflib.Logs as msg

def pkg_deps(ctx):
    ctx.use_pkg('rootcomps')
    return

def configure(ctx):


    if not ctx.env.HEPWAF_FOUND_ROOT:
        ctx.fatal("load a ROOT environment first!")
        pass
    
    ctx.start_msg("ROOT-CONFIG")
    ctx.end_msg(ctx.env['ROOT-CONFIG'])

    return

def build(ctx):

    if not ctx.env.PYTHON:
        ctx.fatal("load a python environment first!")
        pass

    if not ctx.env.HEPWAF_FOUND_ROOT:
        ctx.fatal("load a ROOT environment first!")
        pass
    
    if not ctx.env.HEPWAF_FOUND_LIBXML2:
        ctx.fatal("load a libxml2 environment first!")
        pass
    
    ctx(
        features="cxx cxxshlib",
        name="rootcomps-d",
        source="src/th1d.cxx",
        target="rootcomps-d",
        use="ROOT rootcomps",
        )

    return

def install(ctx):
    return
