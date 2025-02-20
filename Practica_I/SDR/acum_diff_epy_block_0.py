"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__ (self): # only default arguments here
        gr.sync_block.__init__(
            self ,
            name ="bloq_acum", # will show up in GRC
            in_sig =[np.float32],
            out_sig =[np.float32]
        )

    def work (self, input_items, output_items ):
        x = input_items[0] # Senial de entrada .
        y0 = output_items[0] # Senial acumulada

        X_LIMITED = x[:3]
        
        y0[:3] = np.cumsum(X_LIMITED)
        return len(y0)
