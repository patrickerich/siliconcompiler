set sc_partname  [dict get $sc_cfg fpga partname]

#TODO: add logic that remaps yosys built in name based on part number

# Run this first to handle module instantiations in generate blocks -- see
# comment in syn_asic.tcl for longer explanation.
yosys hierarchy -top $sc_design

if {[string match {ice*} $sc_partname]} {
    yosys synth_ice40 -top $sc_design -json "${sc_design}_netlist.json"
} else {

    set lutsize 3
    set output_blif "outputs/$topmodule.blif"
 
    yosys proc
    
    yosys techmap -map +/adff2dff.v
    yosys techmap

    # LUT mapping
    yosys abc -lut $lutsize

    #Flatten the design
    yosys flatten

    # Check
    yosys synth -run check

    # Clean and output blifver      
    yosys opt_clean -purge
}
