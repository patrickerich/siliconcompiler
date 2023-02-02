import siliconcompiler
from siliconcompiler import Library

############################################################################
# DOCS
############################################################################

def make_docs():
    '''
    A configurable constrained random stimulus DV flow.

    The verification pipeline includes the followins teps:

    * **import**: Sources are collected and packaged for compilation
    * **compile**: RTL sources are compiled into object form (once)
    * **testgen**: A random seed is used to generate a unique test
    * **refsim**: A golden trace of test is generated using a reference sim.
    * **sim**: Compiled RTL is exercised using generated test
    * **compare**: The outputs of the sim and refsim are compared
    * **signoff**: Parallel verification pipelines are merged and checked

    The dvflow can be parametrized using a single 'np' parameter.
    Setting 'np' > 1 results in multiple independent verificaiton
    pipelines to be launched.

    '''

    chip = siliconcompiler.Chip('<topmodule>')
    chip.set('option', 'flow', 'dvflow')
    return setup(chip, np=5)

#############################################################################
# Flowgraph Setup
#############################################################################
def setup(chip, np=1):
    '''
    Setup function for 'dvflow'
    '''

    # Definting a flow
    flowname = 'dvflow'
    flow = Library(chip, flowname)

    # A simple linear flow
    flowpipe = ['import',
                'compile',
                'testgen',
                'refsim',
                'sim',
                'compare',
                'signoff']

    tools = {
        'import': ('verilator', 'import'),
        'compile': ('verilator', 'compile'),
        'testgen': ('verilator', 'testgen'),
        'refsim': ('verilator', 'refsim'),
        'sim': ('verilator', 'sim'),
        'compare': ('verilator', 'compare'),
        'signoff': ('verify', 'signoff')
    }

    # Flow setup
    for step in flowpipe:
        tool, task = tools[step]
        #start
        if step == 'import':
            flow.node(flowname, step, tool, task)
        #serial
        elif step == 'compile':
            flow.node(flowname, step, tool, task)
            flow.edge(flowname, prevstep, step)
        #fork
        elif step == 'testgen':
            for index in range(np):
                flow.node(flowname, step, tool, task, index=index)
                flow.edge(flowname, prevstep, step, head_index=index)
        #join
        elif step == 'signoff':
            flow.node(flowname, step, tool, task)
            for index in range(np):
                flow.edge(flowname, prevstep, step, tail_index=index)
        else:
            for index in range(np):
                flow.node(flowname, step, tool, task, index=index)
                flow.edge(flowname, prevstep, step, head_index=index, tail_index=index)

        prevstep = step

    return flow

##################################################
if __name__ == "__main__":
    chip = make_docs()
    chip.write_flowgraph("dvflow.png")
