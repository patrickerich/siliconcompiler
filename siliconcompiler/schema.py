# Copyright 2020 Silicon Compiler Authors. All Rights Reserved.

###########################

def schema():
    '''Method for defining Chip configuration schema 
    All the keys defined in this dictionary are reserved words. 
    '''
    
    cfg = {}

    cfg = schema_defaults(cfg)
    
    cfg = schema_pdk(cfg)

    cfg = schema_pdk_custom(cfg)

    cfg = schema_pdk_pnr(cfg)

    cfg = schema_libs(cfg, 'stdcell')

    cfg = schema_libs(cfg, 'macro')

    cfg = schema_tools(cfg)

    cfg = schema_design(cfg)

    cfg = schema_mcmm(cfg)

    return cfg

############################################
# Parameters that deserve default values
#############################################

def schema_defaults(cfg):

    cfg['sc_mode'] = {
        'help' : 'Implementation mode (virtual, asic, or fpga)',
        'switch' : '-mode',
        'type' : ['string'],
        'defvalue' : ['virtual']
    }
    
    cfg['sc_debug'] = {
        'help' : 'Debug level (INFO/DEBUG/WARNING/ERROR/CRITICAL)',
        'switch' : '-debug',
        'type' : ['string'],
        'defvalue' : ['INFO']
    }

    cfg['sc_build'] = {
        'help' : 'Name of build directory',
        'switch' : '-build',
        'type' : ['string'],
        'defvalue' : ['build']
    }

    cfg['sc_effort'] = {
        'help' : 'Compilation effort (low,medium,high)',
        'switch' : '-effort',
        'type' : ['string'],
        'defvalue' : ['high']
    }

    cfg['sc_priority'] = {
        'help' : 'Optimization priority (timing, power, area)',
        'switch' : '-priority',
        'type' : ['string'],
        'defvalue' : ['timing']
    }

    cfg['sc_start'] = {
        'help' : 'Compilation starting stage',
        'type' : 'string',
        'switch' : '-start',
        'defvalue' : ['import']
    }

    cfg['sc_stop'] = {
        'help' : 'Compilation ending stage',
        'switch' : '-stop',
        'type' : ['string'],
        'defvalue' : ['export']
    }

    cfg['sc_cont'] = {
        'help' : 'Continues from last completed stage',
        'switch' : '-cont',
        'type' : ['bool'],
        'defvalue' : ['False']
    }
        
    cfg['sc_gui'] = {
        'help' : 'Launches GUI at every stage',
        'switch' : '-gui',
        'type' : ['bool'],
        'defvalue' : ['False']
    }

    cfg['sc_verbose'] = {
        'help' : 'Enables verbose printing to screen by EDA tools',
        'switch' : '-verbose',
        'type' : ['bool'],
        'defvalue' : ['False']
    }
    
    cfg['sc_lock'] = {
        'help' : 'Switch to lock configuration from further modification',
        'switch' : '-lock',
        'type' : ['bool'],
        'defvalue' : ['False']
    }

    return cfg




############################################
# Technology setup
#############################################

def schema_pdk(cfg):
    ''' Mandatory Process Design Technology Setup
    '''
      
    cfg['sc_pdkdir'] = {
        'help' : 'Root directory for PDK)',
        'switch' : '-pdkroot',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_ipdir'] = {
        'help' : 'Root directory fpr physical IP)',
        'switch' : '-pdkroot',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_foundry'] = {
        'help' : 'Foundry name (eg: virtual, tsmc, gf, samsung)',
        'switch' : '-foundry',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_process'] = {
        'help' : 'Process name',
        'switch' : '-process',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_node'] = {
        'help' : 'Process node in nm (180, 90, 22, 12, 7 etc)',
        'switch' : '-node',
        'type' : ['int'],
        'defvalue' : []
    }
    
    cfg['sc_pdkguide'] = {
        'help' : 'Process Manual (PDF)',
        'switch' : '-pdkguide',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_pdkdrm'] = {
        'help' : 'Process Design Rule Manual (PDF)',
        'switch' : '-pdkdrm',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    
    #vendor
    cfg['sc_device_model'] = {}
    cfg['sc_device_model']['default'] = {
        'help' : 'Device model directory (per vendor)',
        'switch' : '-device_model',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    #stackup, corner, vendor
    cfg['sc_wire_model'] = {}
    cfg['sc_wire_model']['default'] = {}
    cfg['sc_wire_model']['default']['default'] = {}
    cfg['sc_wire_model']['default']['default']['defult'] = {
        'help' : 'Wire RC/PEX model file (per stackup, corner)',
        'switch' : '-wire_model',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    return cfg

############################################
# Custom Design Environment Setup
#############################################

def schema_pdk_custom(cfg):

    cfg['sc_custom_display'] = {}
    cfg['sc_custom_display']['default'] = {}
    cfg['sc_custom_display']['default']['default'] = {
        'help' : 'Custom design display configuration',
        'switch' : '-custom_display',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_custom_init'] = {}
    cfg['sc_custom_init']['default'] = {}
    cfg['sc_custom_init']['default']['default'] = {
        'help' : 'Custom design init file',
        'switch' : '-custom_init',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    #Name Purpose Layer#  Data-Type
    #RX   drawing 1       0                     
    #stackup, vendor
    cfg['sc_custom_layermap'] = {}
    cfg['sc_custom_layermap']['default'] = {}
    cfg['sc_custom_layermap']['default']['default'] = {
        'help' : 'GDS layer map',
        'switch' : '-layermap',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    #objname   subtype name Layer#  Datatype
    #m1block   routing M1   15      61 
    #stackup, vendor
    cfg['sc_custom_objectmap'] = {}
    cfg['sc_custom_objectmap']['default'] = {}
    cfg['sc_custom_objectmap']['default']['default'] = {
        'help' : 'GDS object map',
        'switch' : '-objectmap',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    # stackup, vendor
    cfg['sc_custom_libs'] = {}
    cfg['sc_custom_libs']['default'] = {}
    cfg['sc_custom_libs']['default']['default'] = {
        'help' : 'Custom library list file',
        'switch' : '-custom_libs',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }
    
    return cfg

                              
############################################
# Automated Place and Route Setup
#############################################

def schema_pdk_pnr(cfg):
    '''Automated Place and Route Setup
    Format1: cfg['sc_pnr_techdir']['libtag']['eda-vendor']
    Libtag would generally be the library track-height

    '''

    cfg['sc_pnr_techdir'] = {}
    cfg['sc_pnr_techdir']['default'] = {}    
    cfg['sc_pnr_techdir']['default']['default'] = {
        'help' : 'Place and route technology setup directory',
        'switch' : '-pnr_techdir',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_pnr_techfile'] = {}
    cfg['sc_pnr_techfile']['default'] = {}    
    cfg['sc_pnr_techfile']['default']['default'] = {
        'help' : 'Place and route tehnology file',
        'switch' : '-pnr_techfile',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_pnr_pexfile'] = {}
    cfg['sc_pnr_pexfile']['default'] = {}    
    cfg['sc_pnr_pexfile']['default'] = {
        'help' : 'Place and route tehnology file',
        'switch' : '-pnr_techfile',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    
    cfg['sc_pnr_layermap'] = {}
    cfg['sc_pnr_layermap']['default'] = {}    
    cfg['sc_pnr_layermap']['default']['default'] = {
        'help' : 'Place and route layer mapping file',
        'switch' : '-pnr_layermap',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_tapmax'] = {
        'help' : 'Tap cell max distance rule',
        'switch' : '-tapmax',
        'type' : ['float'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_tapoffset'] = {
        'help' : 'Tap cell offset rule',
        'switch' : '-tapoffset',
        'type' : ['float'],
        'defvalue' : [],
        'hash' : []
    }
    
    return cfg

############################################
# Design Specific Parameters
#############################################

def schema_design(cfg):
    ''' Design setup schema
    '''

    # Mapping Target
    cfg['sc_target'] = {
        'help' : 'Single name target (nangate45, asap7)',
        'switch' : '-target',
        'type' : ['string'],
        'defvalue' : []
    }

    # RTL Design Parameters
    cfg['sc_source'] = {
        'help' : 'Source files (.v/.vh/.sv/.vhd)',
        'switch' : 'None',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_design'] = {
        'help' : 'Design top module name',
        'switch' : '-design',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_nickname'] = {
        'help' : 'Design nickname',
        'switch' : '-nickname',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_clk'] = {
        'help' : 'Clock defintion (<name period uncertainty>)',
        'switch' : '-clk',
        'type' : ['string', 'float', 'float'],
        'defvalue' : []
    }

    cfg['sc_supplies'] = {
        'help' : 'Supply voltages (<name pin voltage>)',
        'switch' : '-supply',
        'type' : ['string', 'string', 'float'],

        'defvalue' : []
    }
    
    cfg['sc_define'] = {
        'help' : 'Define variables for Verilog preprocessor',
        'switch' : '-D',
        'type' : ['string'],
        'defvalue' : []
    }
    
    cfg['sc_ydir'] = {
        'help' : 'Directory to search for modules',
        'switch' : '-y',
        'type' : ['string'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_idir'] = {
        'help' : 'Directory to search for inclodes',
        'switch' : '-I',
        'type' : ['string'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_vlib'] = {
        'help' : 'Library file',
        'switch' : '-v',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_libext'] = {
        'help' : 'Extension for finding modules',
        'switch' : '+libext',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_readscript'] = {
        'help' : 'Source file read script',
        'switch' : '-f',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    cfg['sc_wall'] = {
        'help' : 'Enable all lint style warnings',
        'switch' : '-Wall',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_wno'] = {
        'help' : 'Disables a warning -Woo-<message>',
        'switch' : '-Wno',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_diesize'] = {
        'help' : 'Die size (x0 y0 x1 y1) for automated floor-planning (um)',
        'switch' : '-diesize',
        'type' : ['float', 'float', 'float', 'float'],
        'defvalue' : []
    }

    cfg['sc_coresize'] = {
        'help' : 'Core size (x0 y0 x1 y1) for automated floor-planning (um)',
        'switch' : '-coresize',
        'type' : ['float', 'float', 'float', 'float'],
        'defvalue' : []
    }

    cfg['sc_floorplan'] = {
        'help' : 'User supplied python based floorplaning script',
        'switch' : '-floorplan',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    
    cfg['sc_def'] = {
        'help' : 'User supplied hard-coded floorplan (DEF)',
        'switch' : '-def',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    
    cfg['sc_ndr'] = {
        'help' : 'Non-default net routing file',
        'switch' : '-ndr',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_vcd'] = {
        'help' : 'Value Change Dump (VCD) file for power analysis',
        'switch' : '-vcd',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_saif'] = {
        'help' : 'Switching activity (SAIF) file for power analysis',
        'switch' : '-saif',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_cfgfile'] = {
        'help' : 'Loads configurations from a json file',
        'switch' : '-cfgfile',
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_custom'] = {
        'help' : 'Custom EDA pass through variables',
        'switch' : '-custom',
        'type' : ['string'],
        'defvalue' : []
    }
    
    cfg['sc_remote'] = {
        'help' : 'Name of remote server address (https://acme.com:8080)',
        'switch' : '-remote',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_ref'] = {
        'help' : 'Reference methodology name',
        'switch' : '-ref',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_pdkdir'] = {
        'help' : 'PDK root directory',
        'switch' : '-pdkdir',
        'type' : ['string'],
        'defvalue' : []
    }
    
    cfg['sc_ipdir'] = {
        'help' : 'IP root directory',
        'switch' : '-ipdir',
        'type' : ['string'],
        'defvalue' : []
    }
    
    cfg['sc_trigger'] = {
        'help' : 'Stage completion that triggers message to <sc_contact>',
        'switch' : '-trigger',
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_contact'] = {
        'help' : 'Trigger event contact (phone#/email)',
        'switch' : '-contact',
        'type' : ['string'],
        'defvalue' : []
    }
    

    cfg['sc_minlayer'] = {
        'help' : 'Minimum routing layer (integer)',
        'switch' : '-minlayer',
        'type' : ['int'],
        'defvalue' : []
    }

    cfg['sc_maxlayer'] = {
        'help' : 'Maximum routing layer (integer)',
        'switch' : '-maxlayer',
        'type' : ['int'],
        'defvalue' : []
    }
    
    cfg['sc_maxfanout'] = {
        'help' : 'Maximum fanout',
        'switch' : '-maxfanout',
        'type' : ['int'],
        'defvalue' : []
    }

 cfg['sc_density'] = {
        'help' : 'Target density for density driven floor-planning (percent)',
        'switch' : '-density',
        'type' : ['int'],
        'defvalue' : []
    }

    cfg['sc_coremargin'] = {
        'help' : 'Margin around core for density driven floor-planning (um)',
        'switch' : '-coremargin',
        'type' : ['float'],
        'defvalue' : []
    }

    cfg['sc_aspectratio'] = {
        'help' : 'Aspect ratio for density driven floor-planning',
        'switch' : '-aspectratio',
        'type' : ['float'],
        'defvalue' : []
    }
    

    
    return cfg

############################################
# MMCM Configuration
#############################################   

def schema_mcmm(cfg):
    
    cfg['sc_mcmm'] = {}
    cfg['sc_mcmm']['default'] = {}

    #Library corner name (needs to match sc_stdlib)
    cfg['sc_mcmm']['default']['lib_corner'] = {
        'help' : 'MMCM Library corner name',
        'switch' : '-mcmm_lib_corner',
        'type' : ['string'],
        'defvalue' : []
    }

    #Wire parastitics corner name
    cfg['sc_mcmm']['default']['rc_corner'] = {
        'help' : 'MMCM Wire Parasticics (RC) corner name',
        'switch' : '-mcmm_rc_corner',
        'type' : ['string'],
        'defvalue' : []
    }

    #Constraints
    cfg['sc_mcmm']['default']['constraints'] = {
        'help' : 'MMCM Constraints (SDC)',
        'switch' : '-mcmm_constraints',
        'type' : ['file'],
        'defvalue' : []
    }

    #Optimization Objectives
    cfg['sc_mcmm']['default']['objectives'] = {
        'help' : 'MMCM Objectives (setup, hold, leakge, dynamic,..)',
        'switch' : '-mcmm_objectives',
        'type' : ['string'],
        'defvalue' : []
    }

    

    
    return cfg

############################################
# Library Configuration
#############################################   

def schema_libs(cfg, group):

    cfg['sc_'+group] = {}  

    cfg['sc_'+group]['default'] = {}

    cfg['sc_'+group]['default']['userguide'] = {
        'help' : 'Library userguide (PDF or TXT)',
        'switch' : '-'+group+'_userguide',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    
    # Userguide
    cfg['sc_'+group]['default']['userguide'] = {
        'help' : 'Library userguide (PDF or TXT)',
        'switch' : '-'+group+'_userguide',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    # Datasheets
    cfg['sc_'+group]['default']['datasheet'] = {
        'help' : 'Library datasheet (PDF, TXT, or HTML directory)',
        'switch' : '-'+group+'_datasheet',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    # Non linear delay models (timing only)
    cfg['sc_'+group]['default']['nldm'] = {}
    cfg['sc_'+group]['default']['nldm']['default'] = {
        'help' : 'Library non-linear delay timing model',
        'switch' : '-'+group+'_nldm',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_'+group]['default']['nldmdb'] = {}
    cfg['sc_'+group]['default']['nldmdb']['default'] = {
        'help' : 'Library NLDM compiled database',
        'switch' : '-'+group+'_nldmdb',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_'+group]['default']['ccs'] = {}
    cfg['sc_'+group]['default']['ccs']['default'] = {
        'help' : 'Library composite current source (ccs) model',
        'switch' : '-'+group+'_ccs',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_'+group]['default']['ccsdb'] = {}
    cfg['sc_'+group]['default']['ccsdb']['default'] = {
        'help' : 'Library CCS compiled databse',
        'switch' : '-'+group+'_ccsdb',
        'type' : ['file'],
        'defvalue' : [],
        'hash' : []
    }

    cfg['sc_'+group]['default']['lef'] = {
        'help' : 'Library layout exchange file (LEF)',
        'switch' : '-'+group+'_lef',      
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_'+group]['default']['libdb'] = {
        'help' : 'Library layout compiled database',
        'switch' : '-'+group+'_libdb',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }
    cfg['sc_'+group]['default']['gds'] = {
        'help' : 'Library GDS file',
        'switch' : '-'+group+'_gds',        
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    } 

    cfg['sc_'+group]['default']['cdl'] = {
        'help' : 'Library CDL file',
        'switch' : '-'+group+'_cdl',        
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_'+group]['default']['spice'] = {
        'help' : 'Library Spice file',
        'switch' : '-'+group+'_spice',        
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    } 

    cfg['sc_'+group]['default']['verilog'] = {
        'help' : 'Library Verilog file',
        'switch' : '-'+group+'_verilog',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_'+group]['default']['atpg'] = {
        'help' : 'Library ATPG file',
        'switch' : '-'+group+'_atpg',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    }

    cfg['sc_'+group]['default']['setup'] = {
        'help' : 'Library TCL setup file',
        'switch' : '-'+group+'_setup',     
        'type' : ['file'],
        'defvalue' : [],
        'hash'   : []
    } 
           
    cfg['sc_'+group]['default']['site'] = {
        'help' : 'Library placement site',
        'switch' : '-'+group+'_site',     
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_'+group]['default']['pgmetal'] = {
        'help' : 'Library power rail metal layer',
        'switch' : '-'+group+'_pgmetal',     
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_'+group]['default']['vt'] = {
        'help' : 'Library Transistor Threshold',
        'switch' : '-'+group+'_vt',     
        'type' : ['string'],
        'defvalue' : [],
        'hash'   : []
    } 

    cfg['sc_'+group]['default']['tag'] = {
        'help' : 'Library indentifier tags',
        'switch' : '-'+group+'_tag',     
        'type' : ['string'],
        'defvalue' : []
    }

    cfg['sc_'+group]['default']['driver'] = {
        'help' : 'Library default driver cell',
        'switch' : '-'+group+'_driver',     
        'type' : ['string'],
        'defvalue' : []
    }

    #Cell lists are many and dynamic (so one more level of nesting)
    cfg['sc_'+group]['default']['cells'] = {}
    cfg['sc_'+group]['default']['cells']['default'] = {
            'help' : 'Library cell type list',
            'switch' : '-'+group+'_cells',
            'type' : ['string'],
            'defvalue' : []
        } 

    return cfg

############################################
# Tool Configuration
#############################################

def schema_tools(cfg):

    cfg['sc_stages'] = {
        'help' : 'List of all compilation stages',
        'switch' : '-stages',
        'type' : ['string'],
        'defvalue' : ['import',
                      'syn',
                      'floorplan',
                      'place',
                      'cts',
                      'route',
                      'signoff',
                      'export',
                      'lec',
                      'pex',
                      'sta',
                      'pi',
                      'si',
                      'drc',
                      'density',
                      'erc',                    
                      'lvs',
                      'tapeout',
                      'display']
    }

    cfg['sc_tool'] = {}
   
    # Defaults and config for all stages
    for stage in cfg['sc_stages']['defvalue']:        
        cfg['sc_tool'][stage] = {}
        for key in ('exe', 'opt', 'refdir', 'script', 'copy', 'format', 'jobid', 'np', 'keymap','vendor'):
            cfg['sc_tool'][stage][key] = {}
            cfg['sc_tool'][stage][key]['switch'] = '-tool_'+key
            
        # Help
        cfg['sc_tool'][stage]['exe']['help'] = 'Stage executable'
        cfg['sc_tool'][stage]['opt']['help'] = 'Stage executable options'
        cfg['sc_tool'][stage]['refdir']['help'] = 'Stage reference Flow Directory'
        cfg['sc_tool'][stage]['script']['help'] = 'Stage entry point script'
        cfg['sc_tool'][stage]['copy']['help'] = 'Stage copy-to-local option'
        cfg['sc_tool'][stage]['format']['help'] = 'Stage configuration format'
        cfg['sc_tool'][stage]['jobid']['help'] = 'Stage job index'
        cfg['sc_tool'][stage]['np']['help'] = 'Stage thread parallelism'
        cfg['sc_tool'][stage]['keymap']['help'] = 'Stage keyword translation'
        cfg['sc_tool'][stage]['vendor']['help'] = 'Stage tool vendor'
        
        # Types
        cfg['sc_tool'][stage]['exe']['type'] = ['string']
        cfg['sc_tool'][stage]['opt']['type'] = ['string']
        cfg['sc_tool'][stage]['refdir']['type'] = ['file']
        cfg['sc_tool'][stage]['script']['type'] = ['file']
        cfg['sc_tool'][stage]['copy']['type'] = ['string']
        cfg['sc_tool'][stage]['format']['type'] = ['string']
        cfg['sc_tool'][stage]['jobid']['type'] = ['int']
        cfg['sc_tool'][stage]['np']['type'] = ['int']
        cfg['sc_tool'][stage]['keymap']['type'] = ['string', 'string']
        cfg['sc_tool'][stage]['keymap']['vendor'] = ['string']

        # Hash
        cfg['sc_tool'][stage]['refdir']['hash'] = []
        cfg['sc_tool'][stage]['script']['hash'] = []

        # Default value
        cfg['sc_tool'][stage]['exe']['defvalue'] = []
        cfg['sc_tool'][stage]['opt']['defvalue'] = []
        cfg['sc_tool'][stage]['refdir']['defvalue'] = []
        cfg['sc_tool'][stage]['script']['defvalue'] = []
        cfg['sc_tool'][stage]['copy']['defvalue'] = []
        cfg['sc_tool'][stage]['format']['defvalue'] = []
        cfg['sc_tool'][stage]['np']['defvalue'] = []
        cfg['sc_tool'][stage]['keymap']['defvalue'] = []
        cfg['sc_tool'][stage]['defvalue']['defvalue'] = []
        cfg['sc_tool'][stage]['jobid']['defvalue'] = ['0']

    return cfg


