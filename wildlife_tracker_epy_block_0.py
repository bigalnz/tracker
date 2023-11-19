"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, threshold=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Tags',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.threshold = threshold
        self.timer = 0
        self.readyForTag = True
        self.previousValue = None

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        in0 = input_items[0]
        
        for index in range(len(input_items[0])):
        
            #print(self.previousValue)
            #print(input_items[0][index])
            if self.previousValue is not None and input_items[0][index] >= 1.8:
                print(f" index {input_items[0][index]} index +1 {input_items[0][index+1]} index-1 {input_items[0][index-1]}")
                if input_items[0][index] > input_items[0][index-1] and input_items[0][index] > input_items[0][index+1]:
                    print(f"peak at {input_items[0][index]}")
                    key = pmt.intern("detect")
                    value = pmt.from_float(np.round(float(input_items[0][index]),2))
                    writeIndex = self.nitems_written(0) + index
                    print(f"Index:{writeIndex}")
                    print(f"Value:{value}")
                    
                    self.add_item_tag(0, writeIndex, key, value )          
        self.previousValue = input_items[0][index]
                
        output_items[0][:] = in0
        return len(output_items[0])
