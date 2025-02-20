import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__ ( self ) : # only default arguments here
        gr. sync_block . __init__ (
            self ,
            name ="bloq_diff", # will show up in GRC
            in_sig =[np.float32],
            out_sig =[np.float32]
        )
        self.acum_anterior=0

    def work (self , input_items , output_items ):
        x = input_items[0] # Senial de entrada .
        y0 = output_items[0]#Senial acumulada diferencial

        X_LIMITED = x[:3]

        cumsum = np.cumsum(X_LIMITED)
    
        diff =np.cumsum(x) - self.acum_anterior
        self.acum_anterior = cumsum[-1] if len(cumsum) > 0 else 0
        
        y0[:len(diff)] = diff
        return len(output_items[0])