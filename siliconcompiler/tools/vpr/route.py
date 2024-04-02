import os
import shutil

from siliconcompiler.tools.vpr import vpr


def setup(chip, clobber=True):
    '''
    Perform automated place and route with VPR
    '''

    tool = 'vpr'
    step = chip.get('arg', 'step')
    index = chip.get('arg', 'index')
    task = chip._get_task(step, index)

    vpr.setup_tool(chip, clobber=clobber)

    chip.set('tool', tool, 'task', task, 'threads', os.cpu_count(),
             step=step, index=index, clobber=clobber)

    # TO-DO: PRIOROTIZE the post-routing packing results?
    design = chip.top()
    chip.add('tool', tool, 'task', task, 'output', design + '.route', step=step, index=index)


def runtime_options(chip, tool='vpr'):
    '''Command line options to vpr for the route step
    '''

    options = vpr.runtime_options(chip, tool=tool)

    if chip.get('tool', tool, 'task', 'route', 'var', 'enable_images')[0] == 'true':
        design = chip.top()

        graphics_commands = vpr.get_common_graphics(chip)

        # set_draw_block_text 0 hides the label for various blocks in the design
        # set_draw_block_outlines 0 removes the outline/boundary for various blocks in the design
        # set_routing_util 1 displays the routing utilization as a heat map
        # set_routing_util 4 displays the routing utilization as a heat map over placed blocks
        # Refer: https://github.com/verilog-to-routing/vtr-verilog-to-routing/blob/master/
        # vpr/src/draw/draw_types.h#L89
        # save_graphics saves the block diagram as a png/svg/pdf
        # Refer:
        # https://docs.verilogtorouting.org/en/latest/vpr/command_line_usage/#graphics-options
        graphics_commands.append("set_draw_block_text 0; " +
                                 "set_draw_block_outlines 0; " +
                                 "set_routing_util 1; " +
                                 "save_graphics "
                                 f"reports/{design}_route_utilization_with_placement.png;")
        graphics_commands.append("set_draw_block_text 0; " +
                                 "set_draw_block_outlines 0; " +
                                 "set_routing_util 4; " +
                                 "save_graphics "
                                 f"reports/{design}_route_utilization.png;")

        graphics_command_str = " ".join(graphics_commands)

        options.append("--graphics_commands")
        options.append(f"\"{graphics_command_str}\"")

    return options


################################
# Post_process (post executable)
################################


def post_process(chip):
    ''' Tool specific function to run after step execution
    '''
    vpr.vpr_post_process(chip)

    design = chip.top()
    # Forward all of the prior step inputs forward for bitstream generation
    shutil.copy(f'inputs/{design}.blif', 'outputs')
    shutil.copy(f'inputs/{design}.net', 'outputs')
    shutil.copy(f'inputs/{design}.place', 'outputs')
